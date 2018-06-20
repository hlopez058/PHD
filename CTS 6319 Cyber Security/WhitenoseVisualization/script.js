

$(function() {
    
        var probeflow = GetProbe_RadarData("vertical");
        
        $( "#slider-range" ).slider({
          range: true,
          min: 0,
          max: probeflow.axistotal,
          values: [ 0, Math.round(probeflow.axistotal/10)],
          slide: function( event, ui ) {
            $( "#amount" ).val(  ui.values[ 0 ] + " - " + ui.values[ 1 ] );
            //change the index and redraw the plots
            DrawRadarChart_ProbeFlow(probeflow,ui.values[ 0 ],ui.values[ 1]);
          }
        });
    
        $( "#amount" ).val( $( "#slider-range" ).slider( "values", 0 ) +
          " - " + $( "#slider-range" ).slider( "values", 1 ) );
    
          //load for the first time the radar chart
          DrawRadarChart_ProbeFlow(probeflow,0,Math.round(probeflow.axistotal/10));

          CreateProbeTable(probeflow.ftuples);
      });

function CreateProbeTable(ftuples){
    var myList = [];
for(var f in ftuples){
    var ftuple = ftuples[f].split(",");
    myList.push({
        "DstIP" : ftuple[0],
        "DstPort" : ftuple[1],
        "SrcIP" : ftuple[2],
        "SrcPort" : ftuple[3],
        "Protocol" : ftuple[4],
    });
}

      buildHtmlTable('#excelDataTable',myList);
      
}

// Builds the HTML Table out of myList.
function buildHtmlTable(selector,myList) 
{
    var columns = addAllColumnHeaders(myList, selector);
    for (var i = 0; i < myList.length; i++) {
        var row$ = $('<tr/>');
        for (var colIndex = 0; colIndex < columns.length; colIndex++) {
        var cellValue = myList[i][columns[colIndex]];
        if (cellValue == null) cellValue = "";
        row$.append($('<td/>').html(cellValue));
        }
        $(selector).append(row$);
    }
}

// Adds a header row to the table and returns the set of columns.
// Need to do union of keys from all records as some records may not contain
// all records.
function addAllColumnHeaders(myList, selector) {
    var columnSet = [];
    var headerTr$ = $('<tr/>');

    for (var i = 0; i < myList.length; i++) {
        var rowHash = myList[i];
        for (var key in rowHash) {
        if ($.inArray(key, columnSet) == -1) {
            columnSet.push(key);
            headerTr$.append($('<th/>').html(key));
        }
        }
    }
    $(selector).append(headerTr$);

    return columnSet;
}


function DrawRadarChart_ProbeFlow(probeflow,start,end){
    var w = 500,
    h = 500;

    var colorscale = d3.scale.category10();

    //Legend titles
    var LegendOptions = [probeflow.label];

    var rangedData = probeflow.data.slice(start,end);

    //Data
    var d =[
        rangedData
        ];

    //Options for the Radar chart, other than default
    var mycfg = {
    w: w,
    h: h,
    maxValue: probeflow.max,
    levels: probeflow.count,
    ExtraWidthX: 300,
    labels:probeflow.yaxislabels
    }

    //Call function to draw the Radar chart
    //Will expect that data is in %'s
    RadarChart.draw("#chart", d, mycfg);

    ////////////////////////////////////////////
    /////////// Initiate legend ////////////////
    ////////////////////////////////////////////

    var svg = d3.select('#body')
    .selectAll('svg')
    .append('svg')
    .attr("width", w+300)
    .attr("height", h)

    //Create the title for the legend
    var text = svg.append("text")
    .attr("class", "title")
    .attr('transform', 'translate(90,0)') 
    .attr("x", w - 70)
    .attr("y", 10)
    .attr("font-size", "12px")
    .attr("fill", "#404040")
    .text("Flows");
        
    //Initiate Legend	
    var legend = svg.append("g")
    .attr("class", "legend")
    .attr("height", 100)
    .attr("width", 200)
    .attr('transform', 'translate(90,20)') 
    ;
    //Create colour squares
    legend.selectAll('rect')
    .data(LegendOptions)
    .enter()
    .append("rect")
    .attr("x", w - 65)
    .attr("y", function(d, i){ return i * 20;})
    .attr("width", 10)
    .attr("height", 10)
    .style("fill", function(d, i){ return colorscale(i);})
    ;
    //Create text next to squares
    legend.selectAll('text')
    .data(LegendOptions)
    .enter()
    .append("text")
    .attr("x", w - 52)
    .attr("y", function(d, i){ return i * 20 + 9;})
    .attr("font-size", "11px")
    .attr("fill", "#737373")
    .text(function(d) { return d; })  ;	
}

  

function GetProbe_RadarData(type){
    var xhr = new XMLHttpRequest();
//    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&attacker="+attacker, false);
xhr.open("GET", "http://localhost:8090/probes?type="+type, false);

xhr.send();
    console.log(xhr.status);
    console.log(xhr.statusText);
    
    if (xhr.status == 200) 
    {

            myObj = JSON.parse(xhr.responseText);
            if(myObj.length==0){
                return null;
            }
            var dstPorts = [];
            for(var ftuple in myObj[0].ftuples){
                dstport = myObj[0].ftuples[ftuple].split(',')[1];
                dstPorts.push(dstport);                
            }


            var maxport =Math.max.apply(null, dstPorts);
            var uniquePortCount = countUnique(dstPorts);

            var uniquePorts = dstPorts.filter(onlyUnique).sort(function(a, b){return a-b});

            var uPortValList = [];
            for(var i=0 ; i<uniquePorts.length ; i++){
                uPortValList.push({key:uniquePorts[i],
                    val:((i+1)/uniquePorts.length)})
            }
            
            var radarArr = [];
            for(var ftuple in myObj[0].ftuples){
                dstip = myObj[0].ftuples[ftuple].split(',')[0];
                dstport = myObj[0].ftuples[ftuple].split(',')[1];
                var obj = uPortValList.find(function (obj) { return obj.key === dstport; })
                radarArr.push({axis:dstip,value:obj.val});
            }
            
            var distinctRadarArr = radarArr.filter(onlyUnique);

            var resp = {
                label:myObj[0].attacker,
                data : distinctRadarArr,
                axistotal: distinctRadarArr.length,
                max: 1,
                count:uniquePortCount,
                yaxislabels:uniquePorts,
                lat:myObj[0].geoData.lat,
                lng:myObj[0].geoData.lon,
                ftuples:myObj[0].ftuples
            };

            return resp;
    }
    
}

function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}

function countUnique(iterable) {
    return new Set(iterable).size;
  }
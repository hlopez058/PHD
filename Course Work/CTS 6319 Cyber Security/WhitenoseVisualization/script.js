

$(function() {


    SELECTED_PROBE = GetProbe_RadarData("strobe");


    $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: SELECTED_PROBE.axistotal,
        values: [ 0, Math.round(SELECTED_PROBE.axistotal/2)],
        slide: function( event, ui ) {
        $( "#amount" ).val(  ui.values[ 0 ] + " - " + ui.values[ 1 ] );
        //change the index and redraw the plots
        DrawRadarChart_ProbeFlow(SELECTED_PROBE,ui.values[ 0 ],ui.values[ 1]);
        }
    });

    $( "#amount" ).val( $( "#slider-range" ).slider( "values", 0 ) +
        " - " + $( "#slider-range" ).slider( "values", 1 ) );
        
    //load for the first time the radar chart
    DrawRadarChart_ProbeFlow(SELECTED_PROBE,0,Math.round(SELECTED_PROBE.axistotal/2));

    CreateProbeTable(GetProbes(100));  
    SelectionFromTable();     

});

var SELECTED_ROW_DATA = ""; 
var SELECTED_PROBE = "";

function CreateProbeTable(probeflows){
    buildHtmlTable('#excelDataTable',probeflows);    
}
    
function CreateFlowTable(ftuples){
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


function GetProbes(count){
    var xhr = new XMLHttpRequest();
    //    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&attacker="+attacker, false);
    xhr.open("GET", "http://localhost:8090/probes?count="+count, false);

    xhr.send();
    console.log(xhr.status);
    console.log(xhr.statusText);
    
    if (xhr.status == 200) 
    {

            myObj = JSON.parse(xhr.responseText).slice(0,count);
            if(myObj.length==0){
                return null;
            }
            var resp=[];

            for(var o in myObj){
            
                resp.push({
                    source:myObj[o].attacker,
                    start:myObj[o].startTime,
                    end:myObj[o].endTime,
                    rate:myObj[o].rate,
                    target:myObj[o].target,
                    type:myObj[o].type,
                    
                });
            }

            return resp;
    }
    
}
  

function GetProbe_RadarData(type){
    var xhr = new XMLHttpRequest();
    //    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&attacker="+attacker, false);
    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&count=1", false);

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
                //lat:myObj[0].geoData.lat,
                //lng:myObj[0].geoData.lon,
                ftuples:myObj[0].ftuples
            };

            return resp;
    }
    
}

function GetSingleProbe_RadarData(ip){
    var xhr = new XMLHttpRequest();
    //    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&attacker="+attacker, false);
    xhr.open("GET", "http://localhost:8090/probes?attacker="+ip+"&count=1", false);

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
                //lat:myObj[0].geoData.lat,
                //lng:myObj[0].geoData.lon,
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

  
  function SearchableTable() {
    // Declare variables 1
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    input2 = document.getElementById("myInputType");
    filter = input.value.toUpperCase();
    filter2 = input2.value.toUpperCase();
    
    table = document.getElementById("excelDataTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
       
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1 ){
          tr[i].style.display = "";
        } else {
            if (td.innerHTML.toUpperCase().indexOf(filter2) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }    
        }
      } 
    }
  }


 
  function SelectionFromTable(){
    document.getElementById('excelDataTable').onclick = function(event){
        event = event || window.event; //for IE8 backward compatibility
        var target = event.target || event.srcElement; //for IE8 backward compatibility
        while (target && target.nodeName != 'TR') {
            target = target.parentElement;
        }
        var cells = target.cells; //cells collection
        //var cells = target.getElementsByTagName('td'); //alternative
        if (!cells.length || target.parentNode.nodeName == 'THEAD') { // if clicked row is within thead
            return;
        }
        var resp =  
            { source: cells[0].innerHTML,
                start: cells[1].innerHTML,
                end: cells[2].innerHTML,
                rate:cells[3].innerHTML,
                target:cells[4].innerHTML}


        SELECTED_PROBE = GetSingleProbe_RadarData(resp.source);
                    
        //load for the first time the radar chart
        DrawRadarChart_ProbeFlow(SELECTED_PROBE,0,Math.round(SELECTED_PROBE.axistotal/2));
    
    }
}
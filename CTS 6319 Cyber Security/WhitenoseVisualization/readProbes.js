

function GetProbe_RadarData(attacker,type){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:8090/probes?type="+type+"&attacker="+attacker, false);
    xhr.send();
    console.log(xhr.status);
    console.log(xhr.statusText);
    
    if (xhr.status == 200) 
    {

        myObj = JSON.parse(xhr.responseText);
        var text = "";
        for(var k in myObj){
            text += myObj[0].attacker + "\n";   
        }
        document.getElementById("text").innerHTML = text;

        var protocol ="";
        if(myObj[0].target.includes("TCP")){
            protocol = "TCP";
        }
        if(myObj[0].target.includes("UDP")){
            protocol = "UDP";
        }
        var ports = myObj[0].target.split(' ')[1].remove(0,3).split(',');
        
        console.write(ports);
        ports.sort(function(a, b){return b-a}); 
        var maxPort = ports[0];
        
        var probeRadarData = {
            source :myObj[0].attacker,
            protocol : protocol,
            destinations : myObj[0].dstIP,

        }
        

        //return IP list 
        //return ports
    
    }
    
}

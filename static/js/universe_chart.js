$(function () {
    const movevixlibor = document.getElementById("movevixlibor").value;
    const movevixlibor_json = JSON.parse(movevixlibor);
    
    var dataPoint_move = [];
    for (var i = 0; i < movevixlibor_json.length; i++) {
        dataPoint_move.push({
            x: new Date(movevixlibor_json[i].date),
            y: parseFloat(movevixlibor_json[i].move)
        });
    }


    var dataPoint_vix = [];
    for (var i = 0; i < movevixlibor_json.length; i++) {
        dataPoint_vix.push({
            x: new Date(movevixlibor_json[i].date),
            y: parseFloat(movevixlibor_json[i].vix)
        });
    }


    var dataPoint_libor = [];
    for (var i = 0; i < movevixlibor_json.length; i++) {
        dataPoint_libor.push({
            x: new Date(movevixlibor_json[i].date),
            y: parseFloat(movevixlibor_json[i].libor)
        });
    }
    
    
    
    var market_chart = new CanvasJS.Chart("market_chart", {
        animationEnabled: true,
        theme: "dark2",
        title:{
            text: "Volatility Index",
            fontSize:13,
        },
        	zoomEnabled:true,
        toolTip: {
            enabled: true,       
            animationEnabled: true 
        },
        legend: {
            cursor: "pointer",
            horizontalAlign: "left", // "center" , "right"
            verticalAlign: "top",
            dockInsidePlotArea: false,
        },
        axisX:{
            crosshair: {
                enabled: true
            }
        },
        axisY: {
            title:"비율",
            includeZero: false,
            gridColor:"white",
            gridThickness: 0.3,
            gridDashType: "dot",

        },
        axisY2: {
            title:"US",
            includeZero: false,
            gridColor:"white",
            gridThickness: 0.3,
            gridDashType: "dot",

        },
        backgroundColor : "rgb(43,62,80)",
        data: [
            {
                name:"MOVE",
                showInLegend: true,
                axisYType: "secondary",
                markerType: "none",
                type: "spline",
                indexLabelFontSize: 16,
                //데이터 넣는 곳
                dataPoints: dataPoint_move
            },

            {
                name:"VIX",
                showInLegend: true,
                axisYType: "secondary",
                markerType: "none",
                type: "spline",
                indexLabelFontSize: 16,
                //데이터 넣는 곳
                dataPoints: dataPoint_vix
            },

            {
                name:"LIBOR",
                showInLegend: true,
                markerType: "none",
                type: "spline",
                indexLabelFontSize: 16,
                //데이터 넣는 곳
                dataPoints:dataPoint_libor
            },


        ]
    });


    market_chart.render();


});
window.onload = function () {

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = mm + '/' + dd + '/' + yyyy;

    //// MAS VENCIDOS
    var prod_1 = document.getElementById("prod_ven_1").value;
    var cant_1 = parseInt(document.getElementById("cant_ven_1").value); 
    var prod_2 = document.getElementById("prod_ven_2").value;
    var cant_2 = parseInt(document.getElementById("cant_ven_2").value);
    var prod_3 = document.getElementById("prod_ven_3").value;
    var cant_3 = parseInt(document.getElementById("cant_ven_3").value);
    var prod_4 = document.getElementById("prod_ven_4").value;
    var cant_4 = parseInt(document.getElementById("cant_ven_4").value);
    var prod_5 = document.getElementById("prod_ven_5").value;
    var cant_5 = parseInt(document.getElementById("cant_ven_5").value);
    //// FIN MAS VENCIDOS

    //// MEJOR VENDIDOS
    var prod_vendidos_1 = document.getElementById("prod_vendidos_1").value;
    var cant_vendidos_1 = parseInt(document.getElementById("cant_vendidos_1").value); 
    var prod_vendidos_2 = document.getElementById("prod_vendidos_2").value;
    var cant_vendidos_2 = parseInt(document.getElementById("cant_vendidos_2").value);
    var prod_vendidos_3 = document.getElementById("prod_vendidos_3").value;
    var cant_vendidos_3 = parseInt(document.getElementById("cant_vendidos_3").value);
    var prod_vendidos_4 = document.getElementById("prod_vendidos_4").value;
    var cant_vendidos_4 = parseInt(document.getElementById("cant_vendidos_4").value);
    var prod_vendidos_5 = document.getElementById("prod_vendidos_5").value;
    var cant_vendidos_5 = parseInt(document.getElementById("cant_vendidos_5").value);
    //// FIN MEJOR VENDIDOS

    var chart1 = new CanvasJS.Chart("grafico_mas_vencidos", {
        theme: "light1", // "light1", "light2", "dark1", "dark2"
        animationEnabled: true,
        exportEnabled: true,
        exportFileName: "Top_5_productos_que_mas_vencen_"+today,
        title: {
            text: "Top 5 productos que mas vencen"
        },
        axisX: {
            margin: 10,
            labelPlacement: "inside",
            tickPlacement: "inside"
        },
        axisY2: {
            title: "Cantidad (en kilos)",
            titleFontSize: 14,
            includeZero: true,
            suffix: " Kilos"
        },
        data: [{
            type: "bar",
            axisYType: "secondary",
            yValueFormatString: "# Kilos",
            indexLabel: "{y}",
            dataPoints: [
                { label: prod_1, y: cant_1 },
                { label: prod_2, y: cant_2 },
                { label: prod_3, y: cant_3 },
                { label: prod_4, y: cant_4 },
                { label: prod_5, y: cant_5 },
            ]
        }]
    });

    var chart2 = new CanvasJS.Chart("grafico_mejor_vendidos_minorista", {
        theme: "light1", // "light1", "light2", "dark1", "dark2"
        animationEnabled: true,
        exportEnabled: true,
        exportFileName: "Top_5_productos_mejor_vendidos_minorista_"+today,
        title: {
            text: "Top 5 productos mejor vendidos minorista"
        },
        axisX: {
            margin: 10,
            labelPlacement: "inside",
            tickPlacement: "inside"
        },
        axisY2: {
            title: "Cantidad (en kilos)",
            titleFontSize: 14,
            includeZero: true,
            suffix: " Kilos"
        },
        data: [{
            type: "bar",
            axisYType: "secondary",
            yValueFormatString: "# Kilos",
            indexLabel: "{y}",
            dataPoints: [
                { label: prod_vendidos_1, y: cant_vendidos_1 },
                { label: prod_vendidos_2, y: cant_vendidos_2 },
                { label: prod_vendidos_3, y: cant_vendidos_3 },
                { label: prod_vendidos_4, y: cant_vendidos_4 },
                { label: prod_vendidos_5, y: cant_vendidos_5 },
            ]
        }]
    });

    chart1.render();
    chart2.render();
}

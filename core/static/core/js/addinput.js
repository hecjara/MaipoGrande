function incrementValue() {
    var value = parseInt(document.getElementById('contador').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('contador').value = value;
}



function crearInputs() {
    // var prod = document.createElement('select');
    // var cant = document.createElement('input');
    var contador = document.getElementById("contador").value;


    // var container1 = document.getElementById("container1");
    // var container2 = document.getElementById("container2");

    // prod.setAttribute("type", "select");
    // prod.setAttribute("id", "id_prod");
    // prod.setAttribute("name", "id_prod");
    // prod.setAttribute("class", "form-control");
    // cant.setAttribute("type", "number");
    // cant.setAttribute("id", "id_cant");
    // cant.setAttribute("name", "id_cant");
    // cant.setAttribute("class", "form-control");

    // while (container1.hasChildNodes() && container2.hasChildNodes()) {
    //     container1.removeChild(container1.lastChild);
    //     container2.removeChild(container2.lastChild);
    // }

    // for (i=0;i<contador;i++) {
        // Append a node with a random text
        // container1.appendChild(document.createTextNode("producto " + (contador+1)));
        // container2.appendChild(document.createTextNode("cantidad " + (contador+1)));
        // Create an <input> element, set its type and name attributes
        var prod = document.createElement('select');
        var cant = document.createElement('input');
        

        prod.type = "select";
        prod.name = "producto" + contador;
        // prod.value = "{{ p.id_producto }}";
        // prod.options = "{{ p.nombre }}";
        // prod.id = "producto "+ contador;
        prod.setAttribute("class", "form-control w-50 p-3");
        cant.type = "number";
        cant.name = "cantidad" + contador;
        // cant.id = "cantidad" + contador;
        cant.setAttribute("class", "form-control w-25 p-3");
        container1.appendChild(prod);
        container2.appendChild(cant);
        // Append a line break 
        container1.appendChild(document.createElement("br"));
        container2.appendChild(document.createElement("br"));
    // }
}




// function addFields(){
//     // Number of inputs to create
//     var number = document.getElementById("member").value;
//     // Container <div> where dynamic content will be placed
//     var container = document.getElementById("container");
//     // Clear previous contents of the container
//     while (container.hasChildNodes()) {
//         container.removeChild(container.lastChild);
//     }
//     for (i=0;i<number;i++){
//         // Append a node with a random text
//         container.appendChild(document.createTextNode("Member " + (i+1)));
//         // Create an <input> element, set its type and name attributes
//         var input = document.createElement("input");
//         input.type = "text";
//         input.name = "member" + i;
//         container.appendChild(input);
//         // Append a line break 
//         container.appendChild(document.createElement("br"));
//     }
// }



// function crearInputT() {
//     var s = document.createElement('select');
//     var x = document.createElement('input');
//     var container = document.getElementById("container1");
//     var container = document.getElementById("container2");
//     s.setAttribute("type", "select");
//     s.setAttribute("id", "idp");
//     s.setAttribute("name", "idp");
//     s.setAttribute("class", "form-control");
//     x.setAttribute("type", "number");
//     x.setAttribute("id", "idc");
//     x.setAttribute("name", "idc");
//     x.setAttribute("class", "form-control");

//     // document.body.appendChild(s);
//     // document.body.appendChild(x);
//     container1.appendChild(s)
//     container2.appendChild(x)
// }

// function EliminarInputT(idc, idp) {
//     var x = document.getElementById(idc);
//     var s = document.getElementById(idp);
//     if (!x && !s) {
//         alert("elementos no definido!");
//     } else {
//         var padre1 = x.parentNode;
//         var padre2 = s.parentNode;
//         padre1.removeChild(x);
//         padre2.removeChild(s);
//     }
// }



var mytextbox = document.getElementById('cant_lote');
var mydropdown = document.getElementById('cboprodbod');

mydropdown.onchange = function(){
      mytextbox.value = mytextbox.value  + this.value; //to appened
     //mytextbox.innerHTML = this.value;-
}
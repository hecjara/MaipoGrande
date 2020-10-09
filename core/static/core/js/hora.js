function myFunc() {
    var now = new Date();
    var time = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
    document.getElementById('display-time').innerHTML = time;
}
myFunc();
setInterval(myFunc, 1000);
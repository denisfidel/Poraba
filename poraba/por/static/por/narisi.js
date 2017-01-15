
    var c = document.getElementById("graf");
    var ctx = c.getContext("2d");
    ctx.font = "10px Arial";
    ctx.fillText("Jan  Feb  Mar  Apr  Maj  Jun  Jul  Avg  Sept  Oct  Nov  Dec", 10, 10);
    ctx.moveTo(10,10);
    ctx.lineTo(100,100);
    ctx.stroke();
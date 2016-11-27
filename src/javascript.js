function initMap() {
    var uluru = {lat: 46.052948, lng: 14.462825};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: uluru
    });
    var markesr = new google.maps.Marker({
        position: uluru,
        map: map
	});
}
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("izrac1").addEventListener("click", izpisiRezultat);
});
function izpisiRezultat (event) {
    var para = document.createElement("p");
    var node = document.createTextNode("This is new.");
    para.appendChild(node);

    var element = document.getElementById("rezultat_iskanja1");
    element.appendChild(para);
}

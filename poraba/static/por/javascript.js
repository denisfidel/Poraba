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
document.getElementById("izrac1").addEventListener("submit", izpisiRezultat, true);
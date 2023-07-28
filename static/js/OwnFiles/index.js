let map = L.map('map').setView([-33.457, -70.6], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let other_marker = L.icon({
  iconUrl: '/static/media/marker.png',
  iconSize: [25, 41], // Icon size in pixels
  iconAnchor: [12, 41],
});

let comDonationsData = document.getElementById('com_donations_data').value;
let comDonations = JSON.parse(comDonationsData);
let comRequestsData = document.getElementById('com_requests_data').value;
let comRequests = JSON.parse(comRequestsData);

// Cluster to avoid error with makers in the same commune
let Markers = L.markerClusterGroup();

// Markers are added to the map
fetch("/static/json/comunas-Chile.json")
  .then((response) => response.json())
  .then((parsedData) => {
    parsedData.forEach((commune) => {
      // Filter donations & requests for the actual commune, then adapt it to a right codification
      let donationsCom = comDonations.filter((donation) => {
        let donationNormalized = donation[6].normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        let communeNameNormalized = commune.name.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        return donationNormalized === communeNameNormalized;
      });
      let RequestsCom = comRequests.filter((request) => {
        let RequestNormalized = request[4].normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        let communeNameNormalized = commune.name.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        return RequestNormalized === communeNameNormalized;
      });

      let lat = parseFloat(commune.lat);
      let lng = parseFloat(commune.lng);

      if (donationsCom.length > 0) {
        donationsCom.forEach((donation) => {
            let donation_id = donation[0];
            let donation_calle = donation[1];
            let donation_tipo = donation[2];
            let donation_cantidad = donation[3];
            let donation_fecha = donation[4];
            let donation_email = donation[5];
            let marker = L.marker([lat, lng]);
            marker.bindPopup('<h4> Id de donacion: ' + donation_id + '</h4>' + 
                             '<i>Calle y número: ' + donation_calle + '</i><br>'+
                             '<i>Tipo: ' + donation_tipo + '</i><br>'+
                             '<i>Cantidad: ' + donation_cantidad + '</i><br>'+
                             '<i>Fecha diponibilidad: ' + donation_fecha + '</i><br>'+
                             '<i>Email donante: ' + donation_email + '</i><br>');
            Markers.addLayer(marker);
        });
      }
      if (RequestsCom.length > 0) {
        RequestsCom.forEach((request) => {
            let request_id = request[0];
            let request_tipo = request[1];
            let request_cantidad = request[2];
            let request_email = request[3];
            let marker = L.marker([lat, lng], {icon:other_marker});
            marker.bindPopup('<h4> Id de pedido: ' + request_id + '</h4>' + 
                             '<i>Tipo: ' + request_tipo + '</i><br>'+
                             '<i>Cantidad: ' + request_cantidad + '</i><br>'+
                             '<i>Email solicitante: ' + request_email + '</i><br>');
            Markers.addLayer(marker);
        });
      }
    });
    map.addLayer(Markers);
});
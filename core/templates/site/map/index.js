let map = null;

const center = { lat: 0.0, lng: 0.0 };
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 2,
    center: center,
  });
}

function toggleBounce() {
  if (marker.getAnimation() !== null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}

function getRandomFloat(min, max, decimals) {
  const str = (Math.random() * (max - min) + min).toFixed(decimals);

  return parseFloat(str);
}

window.initMap = initMap;

$(document).ready(function($){
	resize_map();
	get_location();
	$(window).resize(function(){
		resize_map();
	});
});
function resize_map(){
	var windowHeight = $(window).height();
	$('body').css("height", windowHeight)
}

function get_location(){
	if ("geolocation" in navigator) {
		navigator.geolocation.getCurrentPosition(location_success);
	} else {

	}
}

function location_success(position){
	var lat=position.coords.latitude;
	var lon=position.coords.longitude;
	var myLocation = new google.maps.LatLng(lat, lon);
	var map = draw_map(map, myLocation);
	map = add_marker(map, myLocation, 'Voce');
	var positioning = $.post("/update/location",{
		'lat':lat, 
    	'lon':lon
    });
    positioning.done(function (data){
    	$.each(data, function() {
    		var location = new google.maps.LatLng(this['latitude'], this['longitude']);
		    add_marker(map, location, this['name'])
		});
    })
}

function update_location(lat, lon){
	$.ajax({
    type: "POST",
    url: "/update/location",
    data: {
    	'lat':lat, 
    	'lon':lon
    },
    dataType: 'json',
    success: function(data){ 
    	$.each(data, function() {
    		var location = new google.maps.LatLng(this['latitude'], this['longitude']);
		    add_marker(map, location, this['name'])
		});
    }
});
}


function draw_map(map, myLocation){
	var mapOptions = {
		center: myLocation,
		zoom: 20,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	return map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
}

function add_marker(map, myLocation, title){
	var marker = new google.maps.Marker({
		position: myLocation,
		map: map,
		title: title
	});
}
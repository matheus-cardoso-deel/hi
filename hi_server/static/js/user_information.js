$('#request_button').onclick = function full_profile_request(id){
	var profile_request = $.post("/fullProfileRequest/"+id);
	profile_request.done(function (data){
		alert(data);
	})
}
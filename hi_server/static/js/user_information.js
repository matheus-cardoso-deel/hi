function request_full_profile(id){
	var profile_request = $.post("/fullProfileRequest/"+id);
	profile_request.done(function (data){
		if (data == 'success')
			window.location = '/home'
	})
}
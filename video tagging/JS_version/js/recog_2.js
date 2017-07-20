function watson_input() {

	var myImage = new Image(100, 200);
	myImage.src = 'car.jpg';
	
	
	$.ajax({
  	type: "POST",
  	url: "https://watson-api-explorer.mybluemix.net/visual-recognition/api/v3/classify?version=2016-05-20",
  	data: myImage,
  	success: success,
  	dataType: dataType
	}
	
	success: function(response){
        console.log(response);
    }
	
	);
}
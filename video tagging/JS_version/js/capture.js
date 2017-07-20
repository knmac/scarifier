//REQUIRE ACCESS CONTROL EXPOSE

var i = 0;
var video = document.createElement("video");
var thumbs = document.getElementById("thumbs");
video.preload = "auto";

video.src = "http://www.w3schools.com/html/mov_bbb.mp4";
video.crossOrigin = "anonymous";

video.addEventListener('loadeddata', function() {
    thumbs.innerHTML = "";
    video.currentTime = i;
}, false);

video.addEventListener('seeked', function() {
    // now video has seeked and current frames will show
    // at the time as we expect
    generateThumbnail();
    console.log("Hello");

    // when frame is captured, increase
    i = i+1;
    // if we are not passed end, seek to next interval
    if (i <= video.duration) {
        // this will trigger another seeked event
        video.currentTime = i;
    }
    else {
        // DONE!, next action
        //alert("done!")
    }

}, false);

function generateThumbnail() {

    var c = document.createElement("canvas");
    var ctx = c.getContext("2d");
    c.width = 320;
    c.height = 180;
    ctx.drawImage(video, 0, 0, 320, 180);
    var img    = c.toDataURL("image/png");
    console.log(img);
    document.write('<img src="'+img+'"/>');



}
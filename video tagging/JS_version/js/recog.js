
var watson = require('watson-developer-cloud');
var fs = require('fs');

var visual_recognition = watson.visual_recognition({
    api_key: 'e91e544b63aca2f6717c428c7dc20b8af601cd2a',
    version: 'v3',
    version_date: '2016-05-20'
});

var params = {
    images_file: fs.createReadStream('car.jpg')
};

visual_recognition.classify(params, function(err, res) {
    if (err)
        console.log(err);
    else
        console.log(JSON.stringify(res, null, 2));
});


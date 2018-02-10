var watson = require('watson-developer-cloud');
var play = require('play');

//var fs = require('fs');
//var cred = JSON.parse(fs.readFileSync('bluemix_credentials.json', 'utf8'));

   // username: "",//cred.conversation.username,
   // password: "",//cred.conversation.password,

var conversation = new watson.ConversationV1({
  username: '64ecf24d-2e82-4ca0-ab86-f5ed91362a31',
  password: 'Ymb7nREur1SM',
    version_date: '2017-05-26'
});


  //username: cred.text_to_speech.username,
  //password: cred.text_to_speech.password
var text_to_speech = new watson.TextToSpeechV1 ({
  username: '5b914f5b-7f36-4ac7-8eed-5a7d882a105e',
  password: 'fmPCfziE48ri'
});


speak("Hello World");

/*
conversation.message(
  {
    workspace_id: 'f73eeffe-b9e0-4209-be8f-08e2610452dc',
    input: {'text': 'hello'}
  },  
  function(err, response) {
    if (err)
      console.log('error:', err);
    else
    console.log("trying to speak");
    console.log(response.output.text);
      //convert to speech

      
      speak(response.output.text);
    }
);
*/


function speak(msg){
  var fs = require('fs');
  var params = {
    text: msg,
    voice: 'en-US_AllisonVoice',
    accept: 'audio/wav'
  };
  

  console.log("testing speak");

  // Pipe the synthesized text to a file.
  text_to_speech.synthesize(params)
  .pipe(fs.createWriteStream('./PHD/Hackathon/output.wav'))
  .on('close', function() {

    play.sound('./PHD/Hackathon/output.wav');

    });
  
}
/*
User-specific configuration
    ** IMPORTANT NOTE ********************
    * Please ensure you do not interchange your username and password.
    * Hint: Your username is the lengthy value ~ 36 digits including a hyphen
    * Hint: Your password is the smaller value ~ 12 characters
*/ 

var fs = require('fs');
var cred = JSON.parse(fs.readFileSync('bluemix_credentials.json', 'utf8'));

exports.conversationWorkspaceId = cred.conversationWorkspaceId; // replace with the workspace identifier of your conversation

// Create the credentials object for export
exports.credentials = {};

// Watson Conversation
// https://www.ibm.com/watson/developercloud/conversation.html
exports.credentials.conversation = {
	password: cred.conversation.password,
	username: cred.conversation.username
};

// Watson Speech to Text
// https://www.ibm.com/watson/developercloud/speech-to-text.html
exports.credentials.speech_to_text = {
	password: cred.speech_to_text.password,
	username: cred.speech_to_text.username
};

// Watson Text to Speech
// https://www.ibm.com/watson/developercloud/text-to-speech.html
exports.credentials.text_to_speech = {
	password: cred.text_to_speech.password,
	username: cred.text_to_speech.username
};

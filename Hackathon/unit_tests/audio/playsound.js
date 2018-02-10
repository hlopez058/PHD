var player = require('play-sound')(opts = {})
player.play('output.wav', function(err){
if (err) throw err
});
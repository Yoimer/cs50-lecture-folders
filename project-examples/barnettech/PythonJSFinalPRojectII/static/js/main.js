var player = {};
var alien = {};
var numAliens = 5
var pressed = 0;
var secondsPassed = 0;
var collisionOccured = false;
var saved_high_score = false;
var i = 0;

// spawn a new player from the player class
player= new Player(10, 10, 10);
// spawn a bunch of aliens or asteroids, or whatever you want to imagine them to be.
for (i = 0; i < numAliens; i++) {
  alien[i] = new Alien(500, 50, 50);
}

// set key movements to false, when true, the ship moves.
var keyW = false;
var keyA = false;
var keyS = false;
var keyD = false;
var spacebar = false;

// This snippet is provided in Django official documentation, it allows our ajax call
// to work.
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

// on loading of the page run the following JS code.
window.onload = function(){
if(document.querySelector("#authenticated").textContent == 'yes') {

// load up threejs.
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// add the player to the scene
scene.add( player.cube );

// add aliens to the scene (or asteroids, whatever they are they are deadly)
for (i = 0; i < numAliens; i++) {
  scene.add( alien[i].cube );
}

camera.position.z = 5;

// listen for keydown events to move the player around who
// will be running from the purple boxes, that are deadly dangerous.
document.addEventListener('keydown', (event) => {
  const keyCode = event.keyCode;
  if(collisionOccured == false) {
    document.onkeyup = player.movePlayer1(keyCode, pressed);
  }
  pressed = 1;
});

  setInterval(function(){
    if(collisionOccured == false) {
      secondsPassed = secondsPassed + 1;
    }
    if(collisionOccured == false) {
      // keep incrementing the game clock.
      document.querySelector("#game-clock").textContent = secondsPassed;
    }
  }, 1000);

// our main animation loop.
var animate = function () {
  if(collisionOccured == false) {
    // if no collision, run through players code cycle.
    player.updatePlayer();
    // if no collision update all the aliens.
    for (i = 0; i < numAliens; i++) {
      alien[i].updateAlien();
    }
  }
  // if there's a collision end the round and play a load screeching noise.
  if((player.collision(alien[0]) || player.collision(alien[1]) || player.collision(alien[2]) ||
    player.collision(alien[3])) && saved_high_score == false) {
    var audio = new Audio('static/audio/pickup.wav');
    audio.play();
    if(secondsPassed > 2) {  // don't log a collision in the first seconds of play.
    // else if a collision signal end of round, and freeze the clock this is the players
    // final score.
      collisionOccured = true;
      document.querySelector("#score-text").textContent
      = 'Game over, your final score:  ' + secondsPassed + ' (refresh the web page to restart)';
      if(saved_high_score == false) {
        // save the highscore to the database through this ajax call.
         $.ajax({
            type: "POST",
            dataType: "json",
            url: "/post_highscore",
            data: {
              "score": secondsPassed
            },
            success: function(data) {
                console.log(data);
            },
        });
        saved_high_score = true;
      }
    }
  }
  requestAnimationFrame( animate );

  renderer.render(scene, camera);
			};
  animate();
}

}
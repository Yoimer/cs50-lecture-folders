class Player {
  constructor(x, y, z) {
    Player.numInstances = (Player.numInstances || 0) + 1;
    this.x = x;
    this.y = y;
    this.z = z;
    this.width = 1
    this.height = 1
    this.geometry = new THREE.BoxGeometry( 1, 1, 1 );
    this.material = new THREE.MeshBasicMaterial( { color: 0x0B5394} );
    this.cube = new THREE.Mesh( this.geometry, this.material );
    this.cube.x = x
    this.cube.y = y
    this.cube.z = z

    //this.cube.position.set(10, 10, 10);
  }
  movePlayer1(keyCode, pressed) {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // code to broadcast flying data
    socket.on('on flyleftship', data => {
        let keyD = data.keyD;
        let keyS = data.keyS;
        let keyA = data.keyA;
        let keyW = data.keyW;
        console.log('flying the ship')
        pressed = 1;
        this.flyLeftShip(keyD, keyS, keyA, keyW);
    });

    switch (keyCode) {
      case 68: //d
        keyD = true;
        break;
      case 83: //s
        keyS = true;
        break;
      case 65: //a
        keyA = true;
        break;
      case 87: //w
        keyW = true;
        break;
      case 32:
        spacebar = true;
        keyW = true;
        break;
    }

    if(pressed == 0) {
    if (keyD) {
        // up
        socket.emit('on flyleftship', {'keyD': true, 'keyS': false, 'keyA': false, 'keyW': false});
        keyD = false;
        //this.cube.position.y = this.cube.position.y + .4;
    }
    else if (keyS) {
        // down arrow
        socket.emit('on flyleftship', {'keyD': false, 'keyS': true, 'keyA': false, 'keyW': false});
        keyS = false;

    }
    else if (keyA) {
       // left arrow
       socket.emit('on flyleftship', {'keyD': false, 'keyS': false, 'keyA': true, 'keyW': false});
       keyA = false;
       //this.cube.position.x = this.cube.position.x - .4;

    }
    else if (keyW) {
       // right arrow
       socket.emit('on flyleftship', {'keyD': false, 'keyS': false, 'keyA': false, 'keyW': true});
       // this.cube.position.x = this.cube.position.x + .4;
       keyW = false;
    }
    else if (spacebar == true) {
       // space bar
       socket.emit('on flyleftship', {'keyD': false, 'keyS': false, 'keyA': false, 'keyW': true});
       keyW = false;
       spacebar = false;
       console.log('spacebar');
       //this.cube.position.y = this.cube.position.y + .4;
    }
  }
  }

  updatePlayer(keyCode, pressed) {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    this.cube.rotation.x += 0.01;
    this.cube.rotation.y += 0.01;
    if(this.cube.position.y > -3) {
      this.cube.position.y = this.cube.position.y - .01;
    }
    //console.log(this.cube.position.x + ', ' + this.cube.position.y);

  }
  collision(target) {
    // first, check to see if the left edge of either is farther to the right
    // than the right edge of the other
    if(this.cube.position.x > target.cube.position.x + target.width || target.cube.position.x > this.cube.position.x + this.width) {
        return false
    }

    // then check to see if the bottom edge of either is higher than the top
    // edge of the other
   if(this.cube.position.y > target.cube.position.y + target.height || this.cube.position.y < target.cube.position.y - target.height) {
        return false;
   }

    // if the above aren't true, they're overlapping
    return true

  }

  flyLeftShip(keyD, keyS, keyA, keyW) {
  if (keyD == true && this.cube.position.x < 8.5) {
    this.cube.position.x = this.cube.position.x + .010;
  }
  if (keyS == true && this.cube.position.y > -3) {
    this.cube.position.y = this.cube.position.y - .010;
  }
  if (keyA == true && this.cube.position.x > -8.5) {
    this.cube.position.x = this.cube.position.x - .010;
  }
  if (keyW == true && this.cube.position.y < 3.5) {
    console.log('spacebar :119');
    this.cube.position.y = this.cube.position.y + .010;
  }
  pressed = 0;

}

}


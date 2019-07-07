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
  }

  // this is the main code to move the player around.
  movePlayer1(keyCode, pressed) {
    // code to broadcast flying data
    keyD = false;
    keyS = false;
    keyA = false;
    keyW = false;
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

    this.flyLeftShip(keyD, keyS, keyA, keyW);

  }

  updatePlayer(keyCode, pressed) {
    this.cube.rotation.x += 0.01;
    this.cube.rotation.y += 0.01;
    if(this.cube.position.y > -3) {
      this.cube.position.y = this.cube.position.y - .01;
    }

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

  // function to have the ship fly in the direction of keypressed.
  flyLeftShip(keyD, keyS, keyA, keyW) {
  if (keyD == true && this.cube.position.x < 8.5) {
    this.cube.position.x = this.cube.position.x + .5;
  }
  if (keyS == true && this.cube.position.y > -3) {
    this.cube.position.y = this.cube.position.y - .5;
  }
  if (keyA == true && this.cube.position.x > -8.5) {
    this.cube.position.x = this.cube.position.x - .5;
  }
  if (keyW == true && this.cube.position.y < 3.5) {
    this.cube.position.y = this.cube.position.y + .5;
  }
  pressed = 0;

}

}


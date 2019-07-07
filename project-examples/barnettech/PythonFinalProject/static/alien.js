class Alien {
  constructor(x, y, z) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.width = 1
    this.height = 1
    this.geometry = new THREE.BoxGeometry( 1, 1, 1 );
    this.material = new THREE.MeshBasicMaterial( { color: 0x9932CC} );
    this.cube = new THREE.Mesh( this.geometry, this.material );
    this.cube.x = x
    this.cube.y = y
    this.cube.z = z
    this.randomDirection = 'up';
    this.step = 1;
    this.step2 = 1;
    this.oldY = 0;
    this.newY = 1;
  }
  updateAlien(keyCode) {
    this.cube.rotation.x += 0.01;
    this.cube.rotation.y += 0.01;
    //console.log(this.cube.position.x + ', ' + this.cube.position.y);
    // collision on the top wall
    if(this.cube.position.y > 3.5 && this.cube.position.y < 4) {
      this.cube.position.y = this.cube.position.y - .08;
      this.step = Math.floor(Math.random() * 4);
      this.step2 = Math.floor(Math.random() * 4);
      console.log('1 collision on the top wall');
    }
    // collision on the bottom wall
    if(this.cube.position.y <  -3 && this.cube.position.y > -3.5) {
      this.cube.position.y = this.cube.position.y + .08;
      this.step = Math.floor(Math.random() * 4);
      this.step2 = Math.floor(Math.random() * 4);
      console.log('2 collision on the bottom wall');
    }
    // collision on the left wall
    if(this.cube.position.x < -8.5 && this.cube.position.x > -9.5) {
      this.cube.position.x = this.cube.position.x + .08;
      this.step = Math.floor(Math.random() * 4);
      this.step2 = Math.floor(Math.random() * 4);
      console.log('3 collision on the left wall');
    }
    // collision on the right wall
    if(this.cube.position.x > 8.5 && this.cube.position.x < 9 ) {
      this.cube.position.x = this.cube.position.x - .08;
      this.step = Math.floor(Math.random() * 4);
      this.step2 = Math.floor(Math.random() * 4);
      console.log('4 collision on the right wall');
    }
    console.log('step1 is ' + this.step + ' and step2 is ' + this.step2);

    // insert some randomness to keep the player on his toes.
    if(Math.floor(Math.random() * 100) == 10) {
      this.step = Math.floor(Math.random() * 4);
      this.step2 = Math.floor(Math.random() * 4);
    }

    if(this.step == 0) {
      this.cube.position.y = this.cube.position.y + .04;
    }
    else if(this.step == 1) {
      this.cube.position.y = this.cube.position.y - .04;
    }
    else if(this.step == 2) {
      this.cube.position.x = this.cube.position.x + .04;
    }
    else if(this.step == 3) {
      this.cube.position.x = this.cube.position.x - .04;
    }

    if(this.step2 == 0) {
      this.cube.position.y = this.cube.position.y + .04;
    }
    else if(this.step2 == 1) {
      this.cube.position.y = this.cube.position.y - .04;
    }
    else if(this.step2 == 2) {
      this.cube.position.x = this.cube.position.x + .04;
    }
    else if(this.step2 == 3) {
      this.cube.position.x = this.cube.position.x - .04;
    }


    /*if (keyCode == '38') {
        // up arrow
        this.cube.position.y = this.cube.position.y + .4;
    }
    else if (keyCode == '40') {
        // down arrow
        this.cube.position.y = this.cube.position.y - .4;

    }
    else if (keyCode == '37') {
       // left arrow
       this.cube.position.x = this.cube.position.x - .4;

    }
    else if (keyCode == '39') {
       // right arrow
       this.cube.position.x = this.cube.position.x + .4;
    }
    else if (keyCode == '32') {
       // space bar
       this.cube.position.y = this.cube.position.y + .4;
    }*/

  }
  renderAlien() {

  }
}


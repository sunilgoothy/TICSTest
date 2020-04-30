function setup() {
    createCanvas(1200, 480);
    // background(255,255,0)
  }
  
function draw() {
    if (mouseIsPressed) {
        fill(0);
    } else {
        fill(128);
    }
    fill(0);
    rect(500, 100, 40, 40);
    rect(550, 100, 40, 40);
}
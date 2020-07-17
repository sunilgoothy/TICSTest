function Saddle(saddleimg, coilimg) {
  this.coil_id = ''
  this.draw = function(x, y) {
    image(saddleimg, x, y, 75, 75);
    if (this.coil_id !== '') {
      image(coilimg, x, y, 75, 75);
      text(this.coil_id, x, y+100);
    };
  };
};

function preload() {
  saddle_img = loadImage('imgs/Saddle.svg');
  coil_img = loadImage('imgs/HRCoil.svg');
}

function setup() {
  createCanvas(1200, 480);

  saddle1 = new Saddle(saddle_img, coil_img);
  saddle2 = new Saddle(saddle_img, coil_img);
  saddle3 = new Saddle(saddle_img, coil_img);
  saddle4 = new Saddle(saddle_img, coil_img);
  saddle5 = new Saddle(saddle_img, coil_img);
  saddle6 = new Saddle(saddle_img, coil_img);
  saddle7 = new Saddle(saddle_img, coil_img);
  saddle8 = new Saddle(saddle_img, coil_img);
  saddle9 = new Saddle(saddle_img, coil_img);
  saddle10 = new Saddle(saddle_img, coil_img);

  // For Testing
  saddle2.coil_id = 'Coil202002';
  saddle5.coil_id = 'Coil202005';
  saddle7.coil_id = 'Coil202007';
  saddle9.coil_id = 'Coil202008';
  saddle10.coil_id = 'Coil202010';


};

function draw() {

  clear();
  fill(0, 0, 255, 30); //Background
  strokeWeight(2)
  rect(5, 90, 950, 120, 20);

  var start_xpos = 50;
  var start_ypos = 100;
  fill(255, 0, 0);    //Red Font
  saddle1.draw(start_xpos, start_ypos);
  saddle2.draw(start_xpos += 85 , start_ypos);
  saddle3.draw(start_xpos += 85, start_ypos);
  saddle4.draw(start_xpos += 85, start_ypos);
  saddle5.draw(start_xpos += 85, start_ypos);
  saddle6.draw(start_xpos += 85, start_ypos);
  saddle7.draw(start_xpos += 85, start_ypos);
  saddle8.draw(start_xpos += 85, start_ypos);
  saddle9.draw(start_xpos += 85, start_ypos);
  saddle10.draw(start_xpos += 85, start_ypos);

};
//generate_svg.js

function set_canvas_size(_object, _width, _height){
  _object.attr("width",_width).attr("height",_height);
}

var svg = d3.select("#d3canvas").append("svg");
set_canvas_size(svg,500,400);


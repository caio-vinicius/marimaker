var moveVariables = [{"Image":"imageStyle"},{"Star":"starStyle"},{"Rectangle":"retStyle"}];
var objectDisplacement = "";
for(var i = 0; i < 3; i++)
{
  var tmp = Object.entries(moveVariables[i]);
  objectDisplacement +=
  '<div id="'+ tmp[0][1] +'">\n' +
  ' <label for="Image_position">' + tmp[0][0] + ' Position:</label>\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢁" onclick="' + tmp[0][1] + '(\'y\', -10); "style="margin-left: 112px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢀" onclick="' + tmp[0][1] + '(\'x\', -10)">\n' +
  ' <input type="button" class=button value="🢂" onclick="' + tmp[0][1] + '(\'x\', 10); "style="margin-left: 116px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢃" onclick="' + tmp[0][1] + '(\'y\', 10); "style="margin-left: 112px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🞓 decrease size" onclick="' + tmp[0][1] + '(\'s\', -25);"style="padding: 1rem 5rem;">\n' +
  ' <input type="button" class=button value="🞑 increase size" onclick="' + tmp[0][1] + '(\'s\', 25);"style="padding: 1rem 5rem;">\n' +
  ' <br><br>\n' +
  '</div>\n'
}

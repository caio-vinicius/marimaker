var moveVariables = [{"Image":"imageStyle"},{"Star":"starStyle"},{"Rectangle":"retStyle"}];
var objectDisplacement = "";
function changeMoveObject(object) {
  var res = moveVariables.find(obj => Object.keys(obj).includes(object));
  var value = res[object];
  objectDisplacement =
  '<div id="'+ value +'">\n' +
  ' <label for="Image_position">' + object + ' Position:</label>\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢁" onclick="' + value + '(\'y\', -10); "style="margin-left: 112px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢀" onclick="' + value + '(\'x\', -10)">\n' +
  ' <input type="button" class=button value="🢂" onclick="' + value + '(\'x\', 10); "style="margin-left: 116px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🢃" onclick="' + value + '(\'y\', 10); "style="margin-left: 112px;">\n' +
  ' <br><br>\n' +
  ' <input type="button" class=button value="🞓 decrease size" onclick="' + value + '(\'s\', -25);"style="padding: 1rem 5rem;">\n' +
  ' <input type="button" class=button value="🞑 increase size" onclick="' + value + '(\'s\', 25);"style="padding: 1rem 5rem;">\n' +
  ' <br><br>\n' +
  '</div>\n'
}

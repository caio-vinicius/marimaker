var colorObject = ["Background", "Star", "Rectangle", "Shadow"];
var htmlString = "";
for(var i = 0; i < 4; i++)
{
  htmlString +=
  '<div id=\'' + colorObject[i] + '\'>\n' +
  colorObject[i] + '\n' +
  ' <select id="background_color" onclick="colorSelect(\'' + colorObject[i] + '\', value)">\n' +
  '   <option value="magenta">MAGENTA</option>\n' +
  '   <option value="yellow">YELLOW</option>\n' +
  '   <option value="cyan">CYAN</option>\n' +
  ' </select>' +
  '</div>';
}

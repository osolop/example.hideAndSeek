module.exports.function = function checkItem (item) {
  var http = require('http');
  var config = require('config');
  var response = http.getUrl("https://osolop.pythonanywhere.com/check/" + item.toLowerCase(), { format: "json", });
  return response;
}

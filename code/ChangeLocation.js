module.exports.function = function changeLocation (location) {
  var http = require('http');
  var config = require('config');
  var response = http.getUrl("https://osolop.pythonanywhere.com/move/" + location.toLowerCase(), { format: "json", });
  return response;
}

module.exports.function = function describe (location) {
  var http = require('http');
  var config = require('config');
  var response = http.getUrl("https://osolop.pythonanywhere.com/details/" + location.toLowerCase(), { format: "json", });
  return response;
}
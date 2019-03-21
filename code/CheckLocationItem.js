module.exports.function = function checkLocationItem (location, item) {
  var http = require('http');
  var config = require('config');
  var response = http.getUrl("https://osolop.pythonanywhere.com/check/" + location.toLowerCase() + '/' + item.toLowerCase(), { format: "json", });
  return response;
}

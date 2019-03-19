module.exports.function = function describe (location) {
  var http = require('http');
  var config = require('config');
  var response = http.getUrl(config.get('remote.url') + '/move/' + location, { format: 'json' });
  return response;
}
#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
  console.error('error:', error);
  console.log('code:', response.statusCode);
});

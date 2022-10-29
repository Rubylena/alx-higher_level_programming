#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  const result = JSON.parse(body).results;
  let counter = 0;
  result.map(data => {
    const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
    return (data.characters.includes(wedgeAntilles)) ? counter++ : counter;
  });
  console.log(counter);
});

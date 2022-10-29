#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  const result = JSON.parse(body).results;
  // let counter = 0;
  // result.map(data => {
  //   const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
  //   return (data.characters.includes(wedgeAntilles)) ? counter++ : counter;
  // }, 0);
  // console.log(counter);
  console.log(result.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});

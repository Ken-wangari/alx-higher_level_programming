#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];

if (parseInt(episodeId) < 8) {
  const url = `https://swapi-api.hbtn.io/api/films/${episodeId}`;

  request.get(url, (error, response, body) => {
    if (error) {
      return console.error(error);
    }
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  });
}


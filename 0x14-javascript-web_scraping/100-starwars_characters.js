#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodeId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});


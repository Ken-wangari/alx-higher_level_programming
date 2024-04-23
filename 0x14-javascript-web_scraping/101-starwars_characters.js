#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodeId}`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacters(characters);
  } else {
    console.error('Error fetching film data:', error);
  }
});

function printCharacters(characters) {
  let index = 0;

  function getNextCharacter() {
    if (index < characters.length) {
      request.get(characters[index], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
          index++;
          getNextCharacter();
        } else {
          console.error('Error fetching character data:', error);
        }
      });
    }
  }

  getNextCharacter();
}


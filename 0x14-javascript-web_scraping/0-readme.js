#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];

fs.promises.readFile(fileName, 'utf8')
  .then((content) => {
    console.log(content);
  })
  .catch((error) => {
    console.error('Error reading the file:', error);
  });


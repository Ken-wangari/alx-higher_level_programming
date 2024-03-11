#!/usr/bin/node

const inputNumber = process.argv[2];

if (!inputNumber || isNaN(inputNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(inputNumber));
}


#!/usr/bin/node

function converter(base) {
  return function convertToBase(num) {
    return num.toString(base);
  };
}

module.exports = converter;


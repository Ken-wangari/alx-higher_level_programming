#!/usr/bin/node

function countOccurrences(list, searchElement) {
  let occurrenceCount = 0;
  for (let item of list) {
    if (item === searchElement) {
      occurrenceCount++;
    }
  }
  return occurrenceCount;
}

module.exports = countOccurrences;


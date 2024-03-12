#!/usr/bin/node

exports.esrever = function (list) {
  const mid = Math.floor(list.length / 2);
  for (let i = 0; i < mid; i++) {
    const temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
  return list;
};


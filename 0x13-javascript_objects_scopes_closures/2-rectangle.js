#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w > 0 ? w : undefined;
    this.height = h > 0 ? h : undefined;
  }
}

module.exports = Rectangle;


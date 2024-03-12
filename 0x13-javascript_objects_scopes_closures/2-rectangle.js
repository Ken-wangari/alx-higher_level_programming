#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object if w or h is 0 or not a positive integer
      return {};
    } else {
      // Initialize the instance attributes
      this.width = w;
      this.height = h;
    }
  }
}


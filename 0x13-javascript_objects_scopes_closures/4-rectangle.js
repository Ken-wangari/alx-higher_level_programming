#!/usr/bin/node
class Rectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    } else {
      console.log("Invalid dimensions. Both width and height must be positive numbers.");
    }
  }

  print() {
    if (!this.width || !this.height) {
      console.log("Invalid dimensions. Both width and height must be defined.");
      return;
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate() {
    if (!this.width || !this.height) {
      console.log("Invalid dimensions. Both width and height must be defined.");
      return;
    }

    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    if (!this.width || !this.height) {
      console.log("Invalid dimensions. Both width and height must be defined.");
      return;
    }

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;


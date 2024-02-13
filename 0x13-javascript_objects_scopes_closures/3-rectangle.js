#!/usr/bin/node

/*
 * Creates an empty class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || w === undefined) && !(h <= 0 || h === undefined)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;

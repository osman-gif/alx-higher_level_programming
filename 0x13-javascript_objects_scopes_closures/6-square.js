#!/usr/bin/node

/*
 * class Square that defines a square and
 * inherits from Rectangle of 4-rectangle.js
 */

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size); this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          row += 'X';
        } else {
          row += c;
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;

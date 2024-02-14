#!/usr/bin/node

/*
 * class Square that defines a square and
 * inherits from Rectangle of 4-rectangle.js
 */

const Square1 = require('./5-square');
class Square extends Square1 {
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

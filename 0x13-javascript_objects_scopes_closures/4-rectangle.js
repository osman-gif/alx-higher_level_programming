#!/usr/bin/node

/*
 * class Rectangle that defines a rectangle
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

  rotate () {
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

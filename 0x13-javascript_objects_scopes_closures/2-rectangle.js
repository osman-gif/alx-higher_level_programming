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
}

module.exports = Rectangle;

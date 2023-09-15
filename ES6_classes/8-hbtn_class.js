export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() {
    return this._size; // Return size when cast to a number
  }

  toString() {
    return this._location; // Return location when cast to a string
  }
}

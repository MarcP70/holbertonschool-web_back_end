// 5-building.js
export default class Building {
  constructor(sqft) {
    // Verify the type of the 'sqft' attribute during object creation
    if (typeof sqft === 'number') {
      // Store the 'sqft' attribute in the underscore attribute version
      this._sqft = sqft;
    } else {
      throw TypeError('Sqft must be a number');
    }
  }

  // Getter for the 'sqft' attribute
  get sqft() {
    return this._sqft;
  }

  // Abstract method that must be implemented by subclasses
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

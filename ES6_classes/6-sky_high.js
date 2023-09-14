// 6-sky_high.js
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call the constructor of the parent class
    // Verify the type of the 'floors' attribute during object creation
    if (typeof floors === 'number') {
      // Store the 'floors' attribute in the underscore attribute version
      this._floors = floors;
    } else {
      throw TypeError('Floors must be a number');
    }
  }

  // Getter for the 'floors' attribute
  get floors() {
    return this._floors;
  }

  // Override the 'evacuationWarningMessage' method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

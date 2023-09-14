// 3-currency.js
export default class Currency {
  constructor(code, name) {
    // Verify the types of attributes during object creation
    if (typeof code === 'string') {
      // Store attributes in underscore attribute versions
      this._code = code;
    } else {
      throw TypeError('Code must be a string');
    }
    if (typeof name === 'string') {
      // Store attributes in underscore attribute versions
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  // Getter and setter for the 'code' attribute
  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode === 'string') {
      this._code = newCode;
    } else {
      throw TypeError('Code must be a string');
    }
  }

  // Getter and setter for the 'name' attribute
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  // Method to display the full currency in the specified format
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

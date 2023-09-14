// 4-pricing.js
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    // Verify the types of attributes during object creation
    if (typeof amount === 'number') {
      // Store attributes in underscore attribute versions
      this._amount = amount;
    } else {
      throw TypeError('Amount must be a number');
    }

    // Verify the types of attributes during object creation
    if (currency instanceof Currency) {
      // Store attributes in underscore attribute versions
      this._currency = currency;
    } else {
      throw TypeError('Currency must be an instance of Currency');
    }
  }

  // Getter and setter for the 'amount' attribute
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount === 'number') {
      this._amount = newAmount;
    } else {
      throw TypeError('Amount must be a number');
    }
  }

  // Getter and setter for the 'currency' attribute
  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (newCurrency instanceof Currency) {
      this._currency = newCurrency;
    } else {
      throw TypeError('Currency must be an instance of Currency');
    }
  }

  // Method to display the full price in the specified format
  displayFullPrice() {
    const { name, code } = this._currency;
    return `${this._amount} ${name} (${code})`;
  }

  // Static method to convert the price based on the conversion rate
  static convertPrice(amount, conversionRate) {
    if (typeof amount === 'number' && typeof conversionRate === 'number') {
      return amount * conversionRate;
    }
    throw TypeError('Amount and conversion rate must be numbers');
  }
}

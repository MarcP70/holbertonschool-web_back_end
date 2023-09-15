// 10-car.js
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }

  getBrand() {
    return this._brand;
  }

  getMotor() {
    return this._motor;
  }

  getColor() {
    return this._color;
  }
}

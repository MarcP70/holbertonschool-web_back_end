const chai = require('chai');
const { expect } = chai;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  it('should return the sum of rounded numbers', function() {
    expect(calculateNumber('SUM', 3, 3)).to.equal(6);
  });
  it('should handle decimals and return the sum of rounded numbers', function() {
    expect(calculateNumber('SUM', 3.7, 3)).to.equal(7);
  });
  it('should return the sum of rounded numbers with mixed decimals', function() {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('should return the sum of rounded numbers with mixed decimals', function() {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });
  it('should handle negative numbers and return the correct sum', function() {
    expect(calculateNumber('SUM', -3, 1.2)).to.equal(-2);
  });
  it('should handle negative numbers and return the correct sum', function() {
    expect(calculateNumber('SUM', -3.7, -3)).to.equal(-7);
  });

  it('should return the subtract of rounded numbers', function() {
    expect(calculateNumber('SUBTRACT', 3, 3)).to.equal(0);
  });
  it('should handle decimals and return the subtract of rounded numbers', function() {
    expect(calculateNumber('SUBTRACT', 3.7, 3)).to.equal(1);
  });
  it('should return the subtract of rounded numbers with mixed decimals', function() {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
  });
  it('should return the subtract of rounded numbers with mixed decimals', function() {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
  });
  it('should handle negative numbers and return the correct subtraction', function() {
    expect(calculateNumber('SUBTRACT', -3, 1.2)).to.equal(-4);
  });
  it('should handle negative numbers and return the correct subtraction', function() {
    expect(calculateNumber('SUBTRACT', -3.7, -3)).to.equal(-1);
  });

  it('should return the division of rounded numbers', function() {
    expect(calculateNumber('DIVIDE', 3, 3)).to.equal(1);
  });
  it('should handle decimals and return the division of rounded numbers', function() {
    expect(calculateNumber('DIVIDE', 3.5, 2.1)).to.equal(2);
  });

  it('should return the division of rounded numbers with mixed decimals', function() {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('should handle negative numbers and return the correct division', function() {
    expect(calculateNumber('DIVIDE', -3, 1.2)).to.equal(-3);
  });
  it('should return "Error" when dividing by 0', function() {
    expect(calculateNumber('DIVIDE', 6, 0)).to.equal('Error');
  });
});

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber('SUM', 3, 3), 6);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber('SUM', 3.7, 3), 7);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
    });
    it('should return the sum of rounded numbers', function() {
        assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
    });
    it('should return the sum of rounded numbers', function() {
      assert.equal(calculateNumber('SUM', -3, 1.2), -2);
    });
    it('should return the sum of rounded numbers', function() {
      assert.equal(calculateNumber('SUM', -3.7, -3), -7);
    });

    it('should return the subtract of rounded numbers', function() {
        assert.equal(calculateNumber('SUBTRACT', 3, 3), 0);
    });
    it('should return the subtract of rounded numbers', function() {
        assert.equal(calculateNumber('SUBTRACT', 3.7, 3), 1);
    });
    it('should return the subtract of rounded numbers', function() {
        assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });
    it('should return the subtract of rounded numbers', function() {
        assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    });
    it('should return the subtract of rounded numbers', function() {
      assert.equal(calculateNumber('SUBTRACT', -3, 1.2), -4);
    });
    it('should return the subtract of rounded numbers', function() {
      assert.equal(calculateNumber('SUBTRACT', -3.7, -3), -1);
    });

    it('should return the division of rounded numbers', function() {
      assert.equal(calculateNumber('DIVIDE', 3, 3), 1);
    });
    it('should handle decimals and return the division of rounded numbers', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 3.5, 2.1), 2);
    });

    it('should return the division of rounded numbers with mixed decimals', function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should handle negative numbers and return the correct division', function() {
        assert.equal(calculateNumber('DIVIDE', -3, 1.2), -3);
    });
    it('should return "Error" when dividing by 0', function() {
        assert.equal(calculateNumber('DIVIDE', 6, 0), 'Error');
    });
  });

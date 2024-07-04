// 0-calcul.test.js
const assert = require('assert').strict;
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return 4 when inputs are 1 and 3', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 when inputs are 1 and 3.7', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 when inputs are 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 when inputs are 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should return 0 when inputs are 0 and 0', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1, -1), -2);
    assert.strictEqual(calculateNumber(-1.5, -1.5), -2);
  });

  it('should handle large numbers correctly', function() {
    assert.strictEqual(calculateNumber(123456789, 987654321), 1111111110);
    assert.strictEqual(calculateNumber(123456789.5, 987654321.5), 1111111112);
  });
});

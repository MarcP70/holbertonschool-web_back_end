const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  let calculateNumberSpy;

  beforeEach(function() {
    // Create a spy for Utils.calculateNumber
    calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(function() {
    // Restore the original function
    calculateNumberSpy.restore();
  });

  it('should call Utils.calculateNumber with "SUM", 100, 20', function() {
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberSpy.calledOnceWith('SUM', 100, 20)).to.be.true;
  });
});

const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const Utils = require('./utils');
const expect = require('chai').expect;

describe('sendPaymentRequestToApi', function() {
	it('should use Utils.calculateNumber with the correct arguments', function() {
	  const spy = sinon.spy(Utils, 'calculateNumber');

	  sendPaymentRequestToApi(100, 20);

	  expect(spy.calledOnce).to.be.true;
	  expect(spy.calledWithExactly('SUM', 100, 20)).to.be.true;

	  spy.restore();
	});
  });

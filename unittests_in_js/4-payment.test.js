const sendPaymentRequestToApi = require('./4-payment');
const sinon = require('sinon');
const Utils = require('./utils');
const expect = require('chai').expect;

describe('sendPaymentRequestToApi', function() {
	it('should use Utils.calculateNumber with the correct arguments', function() {
		const stub = sinon.stub(Utils, "calculateNumber").returns(10);

		const consoleSpy = sinon.spy(console, 'log');

	  sendPaymentRequestToApi(100, 20);

	  expect(stub.calledOnce).to.be.true;
	  expect(stub.calledWithExactly('SUM', 100, 20)).to.be.true;
	  expect(consoleSpy.calledWithExactly('The total is: '+ 10)).to.be.true;

	  stub.restore();
	  consoleSpy.restore();
	});
  });

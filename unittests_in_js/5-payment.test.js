const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');
const Utils = require('./utils');
const expect = require('chai').expect;

describe('sendPaymentRequestToApi', function() {
	let consoleSpy;

	beforeEach(() => {
		consoleSpy = sinon.spy(console, 'log');
	});

	afterEach(() => {
		consoleSpy.restore();
	  });

	it('should log "The total is: 120" and be called once when called with 100 and 20', function() {
	  sendPaymentRequestToApi(100, 20);

	  expect(consoleSpy.calledOnce).to.be.true;
	  expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
	});

	it('should log "The total is: 20" and be called once when called with 10 and 10', function() {
        sendPaymentRequestToApi(10, 10);

        expect(consoleSpy.calledOnce).to.be.true;
        expect(consoleSpy.calledWithExactly('The total is: 20')).to.be.true;
	});
  });

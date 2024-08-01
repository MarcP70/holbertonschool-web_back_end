const request = require('request');
const { expect } = require('chai');
const app = require('./api');

describe('Index Page', () => {
  it('should return status code 200', (done) => {
    request.get('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result', (done) => {
    request.get('http://localhost:7865', (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart Page', () => {
  it('should have the correct status code when id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should have the correct status code when id is not a number', (done) => {
    request.get('http://localhost:7865/cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments Page', () => {
  it('should return the correct result', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      const expectedResponseBody = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
      // Parse the response body as JSON
      const responseBody = JSON.parse(body);
      expect(responseBody).to.deep.equal(expectedResponseBody);
      done();
    });
  });

  it('should return status code 200', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
});

describe('Login Page', () => {
  it('should return the correct result', (done) => {
    const userName = 'Paul'; // Example user name
    request.post('http://localhost:7865/login', { json: { userName } }, (error, response, body) => {
      expect(body).to.equal(`Welcome ${userName}`);
      done();
    });
  });

  it('should return status code 200', (done) => {
    request.post('http://localhost:7865/login', { json: { userName: 'JohnDoe' } }, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
});

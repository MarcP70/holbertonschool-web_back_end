const express = require('express');
const app = express();

app.use(express.json()); // Middleware to parse JSON request bodies

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
  res.send({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

if (require.main === module) {
  const PORT = 7865;
  app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
  });
}

module.exports = app;

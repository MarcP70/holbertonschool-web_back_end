import { createClient } from "redis";

const client = createClient({
  url: 'redis://localhost:6380'
});

client
  .on('error', (err) =>
    console.log('Redis client not connected to the server:', err)
  )
  .on('connect', () =>
    console.log('Redis client connected to the server')
  );

client.subscribe("holberton school channel");

client.on("message", (channel, message) => {
  if (message === "KILL_SERVER") {
    client.unsubscribe("holberton school channel");
    client.quit();
  }
  console.log(message);
});

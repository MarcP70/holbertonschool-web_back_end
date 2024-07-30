import { createClient } from 'redis';
import { promisify } from 'util';

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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error('Error setting value:', err);
    } else {
      console.log('Reply:', reply);
    }
  });
}

// Promisify the client.get function
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error('Error getting value:', err);
  }
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Endpoint to handle geolocation data
app.post('/api/geolocation', (req, res) => {
  const { latitude, longitude } = req.body;
  
  // Print latitude and longitude to the console
  console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
  
  // Respond with a success message
  res.json({ message: 'Geolocation data received successfully!' });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
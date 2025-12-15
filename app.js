const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Route for home page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Start the server
app.listen(port, () => {
  console.log(`Express app listening at http://localhost:${port}`);
});
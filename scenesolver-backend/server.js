// scenesolver-backend/server.js

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors'); // --- IMPORT CORS ---
const dotenv = require('dotenv');
const authRoutes = require('./routes/auth');
const analysisRoutes = require('./routes/analysis');
const feedbackRoutes = require('./routes/feedback');

dotenv.config();

const app = express();

// --- SETUP CORS MIDDLEWARE ---
// This will allow requests from your React app on localhost:3000
app.use(cors({ origin: 'http://localhost:3000' }));

app.use(express.json());

app.use(express.static('public'));

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/analysis', analysisRoutes);
app.use('/api/feedback', feedbackRoutes);

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => {
  console.log('✅ MongoDB connected');
  // --- UPDATE: The port is now defined in a variable for clarity ---
  const PORT = process.env.PORT || 5000;
  app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
})
.catch(err => console.error('❌ MongoDB connection error:', err));

const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

// Create feedback schema
const feedbackSchema = new mongoose.Schema({
  rating: {
    type: Number,
    required: true,
  },
  comment: {
    type: String,
    required: true,
  },
  date: {
    type: Date,
    default: Date.now,
  },
});

// Create feedback model
const Feedback = mongoose.model('Feedback', feedbackSchema);

// POST route to save feedback
router.post('/', async (req, res) => {
  try {
    const { rating, comment } = req.body;
    const newFeedback = new Feedback({ rating, comment });
    await newFeedback.save();
    res.status(201).json({ message: 'Feedback submitted successfully' });
  } catch (error) {
    console.error('Error saving feedback:', error);
    res.status(500).json({ message: 'Error saving feedback' });
  }
});

// GET route to fetch all feedbacks (for admin page, if needed)
router.get('/', async (req, res) => {
  try {
    const feedbacks = await Feedback.find().sort({ date: -1 });
    res.json(feedbacks);
  } catch (error) {
    console.error('Error fetching feedback:', error);
    res.status(500).json({ message: 'Error fetching feedback' });
  }
});

module.exports = router;
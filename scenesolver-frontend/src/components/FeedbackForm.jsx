
import React, { useState } from 'react';
import axios from 'axios';
import './FeedbackForm.css';

const FeedbackForm = () => {
  const [rating, setRating] = useState(0);
  const [hover, setHover] = useState(0);
  const [comment, setComment] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (rating === 0 || comment.trim() === "") {
      alert("Please provide both rating and comment");
      return;
    }

    try {
      await axios.post('http://localhost:5000/api/feedback', {
        rating,
        comment,
      });

      setSubmitted(true);
    } catch (error) {
      console.error("Error submitting feedback:", error);
      alert("Failed to submit feedback. Please try again!");
    }
  };

  if (submitted) {
    return (
      <div className="feedback-container">
        <div className="feedback-box dotted-border">
          <h2>Thank you for your feedback! 🎉</h2>
        </div>
      </div>
    );
  }

  return (
    <div className="feedback-container">
      <div className="feedback-box dotted-border">
        <h2>GIVE YOUR FEEDBACK</h2>
        <div className="stars">
          {[...Array(5)].map((_, index) => {
            const starValue = index + 1;
            return (
              <span
                key={starValue}
                className={`star ${starValue <= (hover || rating) ? "active" : ""}`}
                onClick={() => setRating(starValue)}
                onMouseEnter={() => setHover(starValue)}
                onMouseLeave={() => setHover(0)}
                style={{
                  cursor: 'pointer',
                  fontSize: '3rem',
                  color: starValue <= (hover || rating) ? '#ffc107' : '#ccc',
                  transition: 'transform 0.2s, color 0.2s',
                }}
                onMouseOver={(e) => e.currentTarget.style.transform = 'scale(1.2)'}
                onMouseOut={(e) => e.currentTarget.style.transform = 'scale(1)'}
              >
                ★
              </span>
            );
          })}
        </div>
        <form onSubmit={handleSubmit}>
          <textarea
            className="feedback-textarea"
            placeholder="Write your experience here..."
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            style={{
              width: '100%',
              height: '100px',
              padding: '10px',
              marginTop: '15px',
              fontSize: '1rem',
              borderRadius: '5px',
              border: '1px solid #ccc',
              resize: 'none',
            }}
          ></textarea>
          <button type="submit" className="submit-button">
            Submit Feedback
          </button>
        </form>
      </div>
    </div>
  );
};

export default FeedbackForm;
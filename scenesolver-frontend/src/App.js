
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import LoginPage from './components/LoginPage';
import SignUpPage from './components/SignUpPage';
import HomePage from './components/HomePage';
import HowItWorks from './components/HowItWorks';
import UploadPage from './components/UploadPage';
import HistoryPage from './components/HistoryPage';
import FeedbackPage from './components/FeedbackPage';
import AdminFeedbackPage from './components/AdminFeedbackPage';
import './index.css';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(
    () => !!localStorage.getItem('token')
  );

  const handleLogin = () => setIsLoggedIn(true);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setIsLoggedIn(false);
  };

  return (
    <Router>
      <Navbar isLoggedIn={isLoggedIn} onLogout={handleLogout} />
      <main>
        <Routes>
          <Route 
            path="/" 
            element={isLoggedIn ? <Navigate to="/home" /> : <LoginPage onLogin={handleLogin} />} 
          />
          <Route path="/signup" element={<SignUpPage />} />
          
          {/* Protected Routes */}
          <Route path="/home" element={isLoggedIn ? <HomePage /> : <Navigate to="/" />} />
          <Route path="/how-it-works" element={isLoggedIn ? <HowItWorks /> : <Navigate to="/" />} />
          <Route path="/upload" element={isLoggedIn ? <UploadPage /> : <Navigate to="/" />} />
          <Route path="/history" element={isLoggedIn ? <HistoryPage /> : <Navigate to="/" />} />
          <Route path="/feedback" element={isLoggedIn ? <FeedbackPage /> : <Navigate to="/" />} />
          <Route path="/admin/feedback" element={isLoggedIn ? <AdminFeedbackPage /> : <Navigate to="/" />} />
          
          {/* Fallback route */}
          <Route path="*" element={<Navigate to={isLoggedIn ? "/home" : "/"} />} />
        </Routes>
      </main>
    </Router>
  );
};

export default App;
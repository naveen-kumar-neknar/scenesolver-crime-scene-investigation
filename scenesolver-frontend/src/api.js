import axios from 'axios';

// Create an instance of axios
const api = axios.create({
  baseURL: 'http://localhost:5000/api', // The base URL for all API requests
  headers: {
    'Content-Type': 'application/json',
  },
});

/*
  This is an interceptor. It runs BEFORE each request is sent.
  It's a powerful way to automatically add the authentication token
  to every single API call without having to do it manually in each component.
*/
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['x-auth-token'] = token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
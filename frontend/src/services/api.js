import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const analyzeTongue = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await api.post('/analyze_tongue', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: 'Failed to analyze image' };
  }
};

export const getHealthStatus = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    throw error.response?.data || { detail: 'Failed to get health status' };
  }
};

export default api;

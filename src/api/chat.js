import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const chatService = {
  async sendMessage(message) {
    try {
      const response = await axios.post(`${API_BASE_URL}/chat`, {
        message
      });
      return response.data;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  }
}; 
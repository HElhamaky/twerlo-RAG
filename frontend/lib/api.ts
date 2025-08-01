import axios from 'axios';

// API base URL - will work in both development and production
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 
  (typeof window !== 'undefined' && window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://twerlo-rag.onrender.com');

// Create axios instance
export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API endpoints
export const endpoints = {
  chat: '/chat',
  upload: '/upload',
  documents: '/documents',
  auth: '/auth',
};

// Chat API
export const chatAPI = {
  sendMessage: async (message: string, history: any[] = []) => {
    const response = await api.post(endpoints.chat, {
      message,
      history,
    });
    return response.data;
  },
};

// Document API
export const documentAPI = {
  upload: async (file: File, onProgress?: (progress: number) => void) => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await api.post(endpoints.upload, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        if (onProgress && progressEvent.total) {
          const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          onProgress(progress);
        }
      },
    });
    return response.data;
  },

  getDocuments: async () => {
    const response = await api.get(endpoints.documents);
    return response.data;
  },

  deleteDocument: async (filename: string) => {
    const response = await api.delete(`${endpoints.documents}/${filename}`);
    return response.data;
  },
};

// Auth API
export const authAPI = {
  login: async (username: string, password: string) => {
    const response = await api.post(endpoints.auth, {
      username,
      password,
    });
    return response.data;
  },
}; 
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:4000/users",
});

// automatically attach token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Show alert for any response error
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const msg =
      error.response?.data?.detail || // use 'detail' if backend sends it
      error.response?.data?.message || // fallback
      error.message || // fallback
      "Unknown error occurred";
    alert(msg);
    return Promise.reject(error);
  }
);

export default api;

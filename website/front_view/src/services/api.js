import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",
  headers:{
    'Content-Type' : 'application/json',
    'Accept' : 'application/json'
  },
  timeout: 100000000000
});

export default api;
import axios from "axios";


const api = axios.create({
  baseURL: "http://localhost:5000",
  headers:{
    'Content-Type' : 'application/json',
    'Accept' : 'application/json',
    'Authorization' : 'Bearer ' + getCookie("token")
  },
  timeout: 100000000000
});


function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

export default api;
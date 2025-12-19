import Enterprises from "./components/Enterprises.vue";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import Home from "./components/Home.vue";

export const routes = [
    { path:'/',component: Home },
    { path:'/login',component: Login },
    { path:'/register',component: Register }
]
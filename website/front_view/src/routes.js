import Enterprises from "./components/Enterprises.vue";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import Home from "./components/Home.vue";
import Profile from "./components/Profile.vue";

export const routes = [
    { path:'/',component: Home },
    { path:'/login',component: Login },
    { path:'/register',component: Register },
    { path:'/profile',component: Profile }
]
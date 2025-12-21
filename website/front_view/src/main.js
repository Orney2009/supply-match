import { createRouter,createWebHistory } from 'vue-router';
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { routes } from './routes';
import VueCookies from 'vue-cookies'
import './axios'
import VueAwesomePaginate from "vue-awesome-paginate"

import "vue-awesome-paginate/dist/style.css"

const router = createRouter ({
    history : createWebHistory(),
    routes
})

const app = createApp(App).use(VueAwesomePaginate);
app.use(router);
app.use(VueCookies);
app.mount('#app');

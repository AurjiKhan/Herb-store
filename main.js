import { createApp } from 'vue';
import App from './App.vue';
import CartComponent from "@/views/CartComponent.vue";
import LoginComponent from "@/views/LoginComponent.vue";
import { createRouter, createWebHistory } from "vue-router";

import HerbDetailComponent from "@/views/HerbDetailComponent.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: LoginComponent },
    { path: '/cart', component: CartComponent },
    { path: '/herbs/:id', component: HerbDetailComponent },
  ]
});




const app = createApp(App);
app.use(router);
app.mount('#app');

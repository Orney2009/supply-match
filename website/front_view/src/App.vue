<template>
  <Navbar/>  
  <Searchbar @search="searchEntreprises"/>  
  <Enterprises :entreprises=entreprises :categories=categories />
  <Footer/>  
</template>



<script setup>
import Enterprises from './components/Enterprises.vue';
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import Searchbar from './components/Searchbar.vue';
import { ref, onMounted } from "vue";
import api from "./services/api";
import axios from 'axios';

const entreprises = ref([]);
const categories = ref({});

const searchEntreprises = async (query) => {
  try {   

    const response = await api.get("/search", {
      
      params:{
        'query': query
      }

    });

    
    entreprises.value = response.data;    

  } catch (error) {
    console.error("Erreur API :", error);
  }
}


const fetchEntreprises = async () => {
  try {
    const response = await api.get("/");


    entreprises.value = response.data.entreprises;
    categories.value = response.data.categories;



  } catch (error) {
    console.error("Erreur API :", error);
  }
};

onMounted(fetchEntreprises);

</script>


 
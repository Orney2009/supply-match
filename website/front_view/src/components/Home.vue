<template>
  <Navbar/> 
  <Searchbar @search="searchEntreprises"/>  
  <Enterprises :entreprises=entreprises :categories=categories />
  <Footer/>  
</template>



<script setup>
import Enterprises from './Enterprises.vue';
import Footer from './Footer.vue';
import Navbar from './Navbar.vue';
import Searchbar from './Searchbar.vue';
import { ref, onMounted } from "vue";
import api from '../services/api';


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


 
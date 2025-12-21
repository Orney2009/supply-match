<template>
  <Navbar/> 
  <Searchbar @search="searchEntreprises"/>  
  <Enterprises :entreprises=paginatedEntreprises />
   
  <div class="flex justify-center mt-6">
    <vue-awesome-paginate
    :total-items = "entreprises.length"
    :items-per-page="itemsPerPage"
    :max-pages-shown="5"
    :show-ending-buttons="false"    
    :show-breakpoint-buttons="true" 
    v-model="currentPage"   
    />
  </div>
  
    <Footer/> 
</template>



<script setup>
import Enterprises from './Enterprises.vue';
import Footer from './Footer.vue';
import Navbar from './Navbar.vue';
import Searchbar from './Searchbar.vue';
import { ref, onMounted,computed } from "vue";
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
    const response = await api.get("/", {  
      params:{
        'id': $cookies.get("id")
      }  
    });
    
    entreprises.value = response.data.entreprises;    



  } catch (error) {
    console.error("Erreur API :", error);
  }
};

const currentPage = ref(1)
const itemsPerPage = 20
const paginatedEntreprises = computed(()=>{
    const start = (currentPage.value -1) * itemsPerPage;
    const end = start + itemsPerPage;
    return entreprises.value.slice(start,end)
})

onMounted(fetchEntreprises);

</script>


<style>
  .pagination-container {
    display: flex;
    margin-top: 20px;
    column-gap: 10px;
  }

  .paginate-buttons {
    height: 40px;

    width: 40px;

    border-radius: 20px;

    cursor: pointer;

    background-color: rgb(242, 242, 242);

    border: 1px solid rgb(217, 217, 217);

    color: black;
  }

  .paginate-buttons:hover {
    background-color: #d8d8d8;
  }

  .active-page {
    background-color: #3498db;

    border: 1px solid #3498db;

    color: white;
  }

  .active-page:hover {
    background-color: #2988c8;
  }
</style>

 
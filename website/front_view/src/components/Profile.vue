<template>
  <div class="max-w-xl mx-auto mt-10 p-6 bg-white rounded-2xl shadow-md">
    <h2 class="text-2xl font-bold mb-6 text-center">Profil de l'entreprise</h2>

    <form @submit.prevent="handleSubmit" class="space-y-4">

     
      <div>
        <label class="block mb-1 font-medium">Nom de l'entreprise</label>
        <input  v-model="ent_name" type="text"  class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Nom de l'entreprise" required />
      </div>

      <div>
        <label class="block mb-1 font-medium">Description</label>
        <textarea v-model="description" class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Décrivez votre entreprise" rows="4" required ></textarea>
      </div>

      
      <div>
        <label class="block mb-1 font-medium">Adresse</label>
        <input v-model="address" type="text" class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"  placeholder="Adresse" required />
      </div>

      <div>
        <label class="block mb-1 font-medium">Téléphone</label>
        <input v-model="phone" type="text" class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"  placeholder="EX: +229 0166000000" required />
      </div>

      <div>
        <label class="block mb-1 font-medium">Catégorie</label>
        <select v-model="category" class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required >
          <option value="" disabled>Sélectionnez une catégorie</option>
          <option v-for="cat in categories" :key="cat.id">
            {{ cat.name }}
          </option>
        </select>        
      </div>

      <div class="text-center mt-6">
        <button  type="submit" class="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600 transition" >
          Enregistrer
        </button>
      </div>

    </form>

  </div>
</template>


   

<script>
import api from '../services/api';
import axios from 'axios';


export default {
  name: 'Profile',
  data() {
    return {
      ent_name: '',
      description: '',
      address: '',
      category: '',
      phone:'',
      categories: [],
      token: ''      
    };
  },
  methods: {
    async fetchCategories() {
      try {        
        const response = await api.get('/categories');
        this.categories = response.data.categories;
      } catch (error) {
        console.error("Erreur lors de la récupération des catégories :", error);
      }
    },

    async fetchEntreprise() {
      try {              
        const response = await api.get(`/entreprise`);        
        this.ent_name = response.data.name.trim()
        this.description = response.data.description.trim()
        this.address = response.data.address.trim()
        this.phone = response.data.phone.trim()
        this.category = response.data.category    
      } catch (error) {
        console.error("Erreur lors de la récupération des catégories :", error);
      }
    },

    async handleSubmit() {
        const index = this.categories.findIndex(obj => obj.name == this.category);        
        const response = await api.put('/entreprise', {
          name: this.ent_name.trim(),
          description: this.description.trim(),
          address: this.address.trim(),
          category_id: this.categories[index]["category_id"],
          phone:this.phone.trim()
        });
        console.log('Entreprise enregistrée :', response.data);
        alert('Profil enregistré avec succès !');


        // this.name = '';
        // this.description = '';
        // this.address = '';
        // this.category_id = '';
        // this.phone = '';
    
    },
  },
  mounted(){
    this.fetchCategories()
    this.fetchEntreprise()
  },
  beforeCreate(){
    this.token = this.$cookies.get("token")
    if(this.token == null){
      this.$router.push("/login")
    }
  }
};


</script>

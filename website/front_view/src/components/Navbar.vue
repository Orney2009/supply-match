<template>
  <nav class="w-full bg-white px-6 py-4 flex justify-between items-center">
        <h1 class="text-xl font-bold text-gray-800">SUPPLY MATCH</h1>
        <ul class="flex gap-6 text-gray-700 font-medium">
        <li><a href="#" class="hover:text-blue-600">Accueil</a></li>
        <li><a href="#" class="hover:text-blue-600">Entreprises</a></li>
        <li><a href="#" class="hover:text-blue-600">Contact</a></li>
        </ul>
        <div v-if=cookie class="flex items-center lg:order-2">           
            <router-link to="/profile" class="mr-3  text-blue-600 hover:underline" >
              Modifier mon profil
            </router-link>
            <router-link v-on:click=logout to="/" class="text-blue-600 hover:underline cursor-btn" >
              Se déconnecter
            </router-link>
        </div>
        <div v-else>
          <router-link to="/login" class="mr-3  text-blue-600 hover:underline" >
              Se connecter
            </router-link>
            <router-link to="/register" class="text-blue-600 hover:underline" >
              S'inscrire
            </router-link>            
        </div>
  </nav>
</template>

<script setup>

  import { ref } from 'vue';  
  const cookie = ref("")
  cookie.value = $cookies.get("token")

  const logout = () =>{
    $cookies.remove("token") 
    cookie.value = ""
  }

</script>

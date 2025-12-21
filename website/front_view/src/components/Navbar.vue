<template>
  <nav class="w-full bg-white px-6 py-4 flex justify-between items-center">
    <h1 class="text-xl font-bold text-gray-800">SUPPLY MATCH</h1>
    <ul class="flex gap-6 text-gray-700 font-medium">
      <li>
        <router-link to="/" class="hover:text-blue-600">
          Accueil
        </router-link>
      </li>
      <li>
        <router-link to="/entreprises" class="hover:text-blue-600">
          Entreprises
        </router-link>
      </li>
      <li><a href="#contact" class="hover:text-blue-600">Contact</a></li>
    </ul>    
       
    <div v-if=cookie class="flex items-center lg:order-2">           
      <router-link to="/profile"
        class="flex items-center hover:bg-blue-700 hover:text-white text-blue-600 font-medium px-4 py-2 mr-3 rounded-lg transition">
        Modifier mon profil
      </router-link>
      <router-link v-on:click=logout to="/"
        class="flex items-center bg-blue-600 hover:bg-blue-700 text-white font-medium px-4 py-2 rounded-lg transition">
        Se déconnecter
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="size-6 ml-2">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
        </svg>

      </router-link>
    </div>
    <div v-else>
      <div class="flex items-center lg:order-2">
        <router-link to="/login"
          class="flex items-center hover:bg-blue-700 hover:text-white text-blue-600 font-medium px-4 py-2 mr-3 rounded-lg transition">
          Connexion
        </router-link>
        <router-link to="/register"
          class="flex items-center bg-blue-600 hover:bg-blue-700 text-white font-medium px-4 py-2 rounded-lg transition">
          Inscription
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="size-6 ml-2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
          </svg>
  
        </router-link>
      </div>                      
    </div>
  </nav>
</template>

<script setup>

  import { ref } from 'vue';  
  const cookie = ref("")
  cookie.value = $cookies.get("token")

  const logout = () =>{
    $cookies.remove("token") 
    $cookies.remove("id") 
    cookie.value = ""
  }

</script>

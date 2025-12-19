<template>
  <div class="min-h-screen grid grid-cols-1 md:grid-cols-2 bg-gray-50">

    <div class="flex items-center justify-center px-6">
      <div class="w-full max-w-md bg-white p-8 rounded-2xl shadow-sm">
        <div class="mb-8 text-center">
          <h2 class="text-2xl font-bold text-gray-800">  SUPPLY MATCH  </h2>
          <p class="text-gray-500 text-sm mt-1">
            <span class="text-blue-600 font-medium">
              Connectez-vous aux entreprises
            </span>
          </p>
        </div>
       
        <div class="mb-4">
          <label class="block text-sm text-gray-600 mb-1">
            Adresse email
          </label>
          <input type="email" placeholder="ex: johndoe@gmail.com" class="w-full border border-gray-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>

    
        <div class="mb-6">
          <label class="block text-sm text-gray-600 mb-1">
            Mot de passe
          </label>
          <input type="password" class="w-full border border-gray-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>

     
        <div class="flex items-center justify-between mb-6 text-sm">
          <router-link to="/register" class="text-blue-600 hover:underline" >
            Créer un compte
          </router-link>

          <router-link to="/forgot-password" class="text-gray-500 hover:text-blue-600" >
            Mot de passe oublié ?
          </router-link>
        </div>

        
        <button class="w-full bg-blue-600 text-white py-2.5 rounded-lg hover:bg-blue-700 transition font-medium" >
          Connexion
        </button>

      </div>
    </div>

    
    <div class="hidden md:block">
      <img
        src="../assets/connected_entreprises2.jpg"
        alt="Entreprises connectées"
        class="w-full h-full object-cover"
      />
    </div>

  </div>
</template>

<script setup>
</script>
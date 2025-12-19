<template>
  <section class="bg-gray-50 min-h-screen flex items-center justify-center">
    <div class="w-full max-w-md px-6 py-8 mx-auto">

      <router-link to="/" class="flex justify-center mb-6 text-2xl font-semibold text-blue-600" >
        SUPPLY MATCH
      </router-link>

     
      <div class="bg-white rounded-lg shadow p-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl mb-6">
          Créer votre compte
        </h1>

        <form class="space-y-4">          
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Votre email
            </label>
            <input  type="email" placeholder="johndoe@gmail.com" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg  focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" />
          </div>


          <div> 
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Mot de passe
            </label>
            <input type="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" />
          </div>

        
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900">
              Confirmez le mot de passe
            </label>
            <input  type="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" />
          </div>

         
          <button type="submit" class="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition" >
            Création de compte
          </button>

          <p class="text-sm text-gray-500 text-center">
            Avez-vous déjà un compte ?
            <router-link to="/login" class="font-medium text-blue-600 hover:underline" >
              Connexion
            </router-link>
          </p>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>
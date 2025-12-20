<template>
  <nav class="w-full bg-white px-6 py-4 flex justify-between items-center">
        <h1 class="text-xl font-bold text-gray-800">SUPPLY MATCH</h1>
        <ul class="flex gap-6 text-gray-700 font-medium">
        <li><a href="#" class="hover:text-blue-600">Accueil</a></li>
        <li><a href="#" class="hover:text-blue-600">Entreprises</a></li>
        <li><a href="#" class="hover:text-blue-600">Contact</a></li>
        </ul>
        <div class="flex items-center lg:order-2">
           <!-- <a href="#" class="text-gray-800 dark:text-white hover:bg-gray-50 focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2">Log in</a> -->
            <router-link to="/login" class="text-blue-600 hover:underline" >
              Log in
            </router-link>
        </div>
  </nav>
</template>

<script setup>
</script>

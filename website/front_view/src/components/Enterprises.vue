
<template>

    <div class="w-full px-6 flex flex-wrap justify-center sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4" >
        <div class="max-w-sm rounded overflow-hidden shadow-lg mt-5" v-for="e in props.entreprises" :key="e.id">
            <img class="w-full h-75 object-cover bg-cover" src="../assets/entreprise.jpg" alt="Sunset in the mountains">
            
            <div class="px-6 py-4 h-80">
                <div class="font-bold text-xl mb-2">{{ e.name }}</div>
                <span class="inline-flex items-center bg-brand-softer border border-brand-subtle text-fg-brand-strong text-xs font-medium px-1.5 py-0.5 rounded-sm my-2">
                  <svg class="w-3 h-3 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.122 17.645a7.185 7.185 0 0 1-2.656 2.495 7.06 7.06 0 0 1-3.52.853 6.617 6.617 0 0 1-3.306-.718 6.73 6.73 0 0 1-2.54-2.266c-2.672-4.57.287-8.846.887-9.668A4.448 4.448 0 0 0 8.07 6.31 4.49 4.49 0 0 0 7.997 4c1.284.965 6.43 3.258 5.525 10.631 1.496-1.136 2.7-3.046 2.846-6.216 1.43 1.061 3.985 5.462 1.754 9.23Z"/></svg>
                  {{ props.categories[e.category_id-1]["name"] }}
                </span>
                <p>
                    <span class="inline-flex items-center bg-brand-softer border border-brand-subtle text-fg-brand-strong text-xs font-medium px-1.5 py-0.5 rounded-sm my-2">
                        <svg class="w-3 h-3 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.122 17.645a7.185 7.185 0 0 1-2.656 2.495 7.06 7.06 0 0 1-3.52.853 6.617 6.617 0 0 1-3.306-.718 6.73 6.73 0 0 1-2.54-2.266c-2.672-4.57.287-8.846.887-9.668A4.448 4.448 0 0 0 8.07 6.31 4.49 4.49 0 0 0 7.997 4c1.284.965 6.43 3.258 5.525 10.631 1.496-1.136 2.7-3.046 2.846-6.216 1.43 1.061 3.985 5.462 1.754 9.23Z"/></svg>
                        {{ e.address }}
                    </span>
                </p>
                <p class="text-gray-700 text-base text-justify line-clamp-6">
                    {{ e.description != 'NaN'? e.description : 'Aucune information' }} 
                </p>
            </div>
            <div class="flex justify-center pb-2 ">
                <span class="inline-block bg-blue-500 -bottom-40 rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2 ">Voir plus</span>
            </div>
        </div>

    </div>
</template>


<script setup>

const props = defineProps({
  toDisplay: Object,
  entreprises : Array,
  categories : Object
})



</script>
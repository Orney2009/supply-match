<template>
  <div class="w-full shadow bg-white px-6 py-4 flex items-center gap-3">
    <input type="text" v-model="query" placeholder="Rechercher ..." class="flex-1 p-2 border rounded-lg" />

    <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="submitSearch" >
      Rechercher
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const query = ref("");
const emit = defineEmits(["search"]);

const submitSearch = () => {
  emit("search", query.value);
};
</script>
<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const entreprises = ref([]);

const fetchEntreprises = async () => {
  try {
    const response = await api.get("/");
    entreprises.value = response.data;
  } catch (error) {
    console.error("Erreur API :", error);
  }
};

onMounted(fetchEntreprises);
</script>

<template>
  <div>
    <h2>Liste des entreprises</h2>

    <ul>
      <li v-for="e in entreprises" :key="e.id">
        <strong>{{ e.name }}</strong><br />
        {{ e.category_id }} - {{ e.address }}<br />
        📞 {{ e.phone }}
      </li>
    </ul>
  </div>
</template>
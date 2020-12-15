<template>
  <div class="container">
    <div id="app">
      <h1>Lista de Campanhas</h1>
      <hr />
      <ul>
        <li v-for="campanha in campanhas" :key="campanha.campanha_id">
          {{ campanha.titulo_campanha }}
        </li>
      </ul>
    </div>
  </div>  
</template>

<script>
import axios from "axios";
export default {
  name: "CampanhaList",
  data() {
    return {
      newCampanha: "",
      campanhas: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getCampanha();
  },
  methods: {
    getCampanha() {
      axios.get("api/campanhas").then((res) => {
        // console.log(res.data);
        this.campanhas = res.data;
      });
    },
  },
};
</script>

<style>
</style>
<template>
  <div class="container"> 
    <div id="app">
      <h1>Lista de Demandas</h1>
      <hr />
      <ul>
        <li v-for="demanda in demandas" :key="demanda.demanda_id">
          {{ demanda.titulo_demanda }}
        </li>
      </ul>
    </div>
  </div>  
</template>

<script>
import axios from "axios";
export default {
  name: "DemandaList",
  data() {
    return {
      newDemanda: "",
      demandas: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getDemanda();
  },
  methods: {
    getDemanda() {
      axios.get("http://localhost:8000/api/demanda").then((res) => {
        // console.log(res.data);
        this.demandas = res.data;
      });
    },
  },
};
</script>

<style>
</style>
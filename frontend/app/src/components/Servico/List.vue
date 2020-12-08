<template>
  <div class="container">
    <div id="app">
      <h1>Lista de Serviços</h1>
      <hr />
      <ul>
        <li v-for="servico in servicos" :key="servico.servico_id">
          {{ servico.titulo_servico }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ServicoList",
  data() {
    return {
      newServico: "",
      servicos: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getServico();
  },
  methods: {
    getServico() {
      axios.get("http://localhost:8000/api/servico").then((res) => {
        // console.log(res.data);
        this.servicos = res.data;
      });
    },
  },
};
</script>

<style>
</style>
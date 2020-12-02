<template>
  <div id="app">
    <h1>Lista de Voluntariados</h1>
    <hr />
    <ul>
      <li v-for="voluntariado in voluntariados" :key="voluntariado.voluntariado_id">
        {{ voluntariado.titulo_voluntariado }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "VoluntariadoList",
  data() {
    return {
      newVoluntariado: "",
      voluntariados: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getVoluntariado();
  },
  methods: {
    getVoluntariado() {
      axios.get("http://localhost:8000/api/voluntariado").then((res) => {
        // console.log(res.data);
        this.voluntariados = res.data;
      });
    },
  },
};
</script>

<style>
</style>
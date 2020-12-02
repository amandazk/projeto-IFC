<template>
  <div id="app">
    <h1>Lista de Ofertas</h1>
    <hr />
    <ul>
      <li v-for="oferta in ofertas" :key="oferta.oferta_id">
        {{ oferta.titulo_oferta }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "OfertaList",
  data() {
    return {
      newOferta: "",
      ofertas: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getOferta();
  },
  methods: {
    getOferta() {
      axios.get("http://localhost:8000/api/oferta").then((res) => {
        // console.log(res.data);
        this.ofertas = res.data;
      });
    },
  },
};
</script>

<style>
</style>
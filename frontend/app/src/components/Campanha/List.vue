<template>
  <div id="app">
    <h1>Lista</h1>
    <button @click="getCampanha">Buscar dados</button>
    <hr />
    <ul>
      <li v-for="campanha in campanhas" :key="campanha.campanha_id">
        {{ campanha.titulo_campanha }}
      </li>
    </ul>
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
  methods: {
    getCampanha() {
      axios.get("http://localhost:8000/api/campanhas").then((res) => {
        // console.log(res.data)
        this.campanhas = res.data;
      });
    },
  },
};
</script>

<style>
</style>
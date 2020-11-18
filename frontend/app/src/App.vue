<template>
  <dir id="app">
    <h1>Lista</h1>
    <button @click="getPessoas">Buscar dados</button>
    <hr />
    <input v-model="newPessoa" type="text" />
    <ul>
      <li v-for="pessoa in pessoas" :key="pessoa.pessoa.id">
        {{ pessoa.nome }}
      </li>
    </ul>
  </dir>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      newPessoa: "",
      pessoas: [],
    };
  },
  methods: {
  getPessoas(){
    axios.get('http://localhost:8000/api/pessoas').then((res) => {
      console.log(res.data)
    })
  }
  }
};

</script>

<style>
</style>template
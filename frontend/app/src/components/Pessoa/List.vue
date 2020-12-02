<template>
  <div id="app">
    <h1>Lista de Pessoas</h1>
    <hr />
    <ul>
      <li v-for="pessoa in pessoas" :key="pessoa.pessoa_id">
        {{ pessoa.nome_pessoa }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PessoaList",
  data() {
    return {
      newPessoa: "",
      pessoas: [],
    };
  },
  mounted() {
    // na hora que a página for montada, quero exibir o resultado do banco
    this.getPessoa();
  },
  methods: {
    getPessoa() {
      axios.get("http://localhost:8000/api/pessoas").then((res) => {
        // console.log(res.data);
        this.pessoas = res.data;
      });
    },
  },
};
</script>

<style>
</style>
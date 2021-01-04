<template>
  <div class="container">
    <div id="app">
      <h1>Campanhas Solidárias</h1>
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Campanha</th>
            <th scope="col">Data Início</th>
            <th scope="col">Data Fim</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="campanha in campanhas" :key="campanha.campanha_id">
            <td>{{ campanha.titulo_campanha }}</td>
            <td>{{ campanha.dt_inicio_campanha }}</td>
            <td>{{ campanha.dt_fim_campanha }}</td>
          </tr>
        </tbody>
      </table>
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
.table {
  margin-top: 40px;
}
</style>
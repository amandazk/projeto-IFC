<template>
  <div>
    <v-app id="">
      <NavBar ref="drawer"></NavBar>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>Descrição do projeto</h2>
          <p>
            A proposta deste projeto é a disponibilização do Portal 
            da Solidariedade, um ambiente web com a função de dar visibilidade 
            a estas pessoas.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="./descricao"
              role="button"
              >Saiba mais &raquo;</a
            >
          </p>
        </div>
        <div class="col-md-4">
          <h2>Como se cadastrar</h2>
          <p>
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="/informacao-projeto"
              role="button"
              >Saiba mais &raquo;</a
            >
          </p>
        </div>
        <div class="col-md-4">
          <h2>Cuidados na Pandemia</h2>
          <p>
            É importante nos previrmos durante a pandemia que acontece, por isso
            criamos essa área para informar quais cuidados devemos ter.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="/cuidados-covid"
              role="button"
              >Saiba mais &raquo;</a
            >
          </p>
        </div>
      </div>
    </div>

    <div class="t1">
      <h2> DESCRIÇÃO DO PROJETO </h2>
    </div>
    <div class="alt">
      <a> O Brasil é a sétima nação mais desigual do mundo atualmente e com <br>
        a questão da COVID-19 e o isolamento social, a desigualdade cresce <br>
        cada vez mais. A proposta deste projeto é a disponibilização do Portal <br>
        da Solidariedade, um ambiente web com a função de dar visibilidade <br>
        a estas pessoas.
        <br>
        <br>

        O projeto pretende oferecer espaço para que esta população possa ser <br>
        enxergada, possa disponibilizar suas qualificações, seus saberes, <br>
        apresentar seus produtos e serviços e, desta forma, conseguir ampliar <br>
        as suas possibilidades de serem incluídos nos processos de proteção <br>
        e também de recuperação dos efeitos da pandemia que, seguramente, <br>
        ainda vão se refletir por vários meses. Também as ações de solidariedade <br>
        que aos poucos vão acontecendo nas cidades poderão ser hospedadas <br>
        neste portal. Este conjunto de esforços, todos concentrados em um local, <br>
        permitindo a ampliação do suporte para os excluídos deste
        nosso país.
      </a>
    </div>

    <v-app id="">
      <Footer ref="drawer"></Footer>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<script>
//import router from "../router/index.js";
export default {
  name: "Index",
  data() {
    
}}

</script>

<style>
.navbar-default {
  margin : 0 !important; 
}

.container{
  margin-top: 70px;
}

.alt{
  margin-top: 50px;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 19px;
}

.t1{
  margin-top: 25px;
  text-align: center;
}

</style>
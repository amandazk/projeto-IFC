<template>
  <div>
    <v-app id="">
      <NavBar ref="drawer"></NavBar>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>

    <!-- <div><a> aaaaaa </a></div>
    <div><a> aaaaaa </a></div>
    <div><a> aaaaaa </a></div>
    <div><a> aaaaaa </a></div> -->

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>Descrição do projeto</h2>
          <p>
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="./descricao-projeto"
              role="button"
              >View details &raquo;</a
            >
          </p>
        </div>
        <div class="col-md-4">
          <h2>Como funciona</h2>
          <p>
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="#"
              role="button"
              >View details &raquo;</a
            >
          </p>
        </div>
        <div class="col-md-4">
          <h2>Outra informação</h2>
          <p>
            Donec sed odio dui. Cras justo odio, dapibus ac facilisis in,
            egestas eget quam. Vestibulum id ligula porta felis euismod semper.
            Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
            nibh, ut fermentum massa justo sit amet risus.
          </p>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="#"
              role="button"
              >View details &raquo;</a
            >
          </p>
        </div>
      </div>
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
</style>
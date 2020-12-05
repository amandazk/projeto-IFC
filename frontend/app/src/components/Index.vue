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
        <div class="card bg-light mb-3 col-md-4">
           <div class="card-body">
            <h2 class="card-title">Light card title</h2>
            <p class="card-text">
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
            </p>
           </div>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="./descricao"
              role="button"
              >Saiba mais &raquo;</a
            >
          </p>
        </div>
        <div class="card bg-light mb-3 col-md-4">
          <div class="card-body">
            <h2 class="card-title">Light card title</h2>
            <p class="card-text">
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
          </p>
          </div>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="#"
              role="button"
              >Saiba mais &raquo;</a
            >
          </p>
        </div>
        <div class="card bg-light mb-3 col-md-4">
          <div class="card-body">
            <h2 class="card-title">Light card title</h2>
            <p class="card-text">
            Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
            tellus ac cursus commodo, tortor mauris condimentum nibh, ut
            fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.
          </p>
          </div>
          <p>
            <a
              class="btn btn-secondary p-2 mb-2 bg-success text-white"
              href="#"
              role="button"
              >Saiba mais &raquo;</a
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
  data() {},
};
</script>

<style>
.navbar-default {
  margin: 0 !important;
}

.container {
  margin-top: 70px;
}
</style>
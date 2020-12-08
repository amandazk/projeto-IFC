<template>
  <div class="container">
    <v-app id="">
      <NavBar ref="drawer"></NavBar>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>


    <div>
        <a> teste </a>
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

export default {
  name: "Cadastro",
  data() {
    
}}

</script>
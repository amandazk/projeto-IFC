<template>
   <v-app id="">
    <NavBar ref="drawer"></NavBar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>

    <h1> a </h1>
    <h1> a </h1>


    <h1> a </h1>
    <h1> a </h1><h1> a </h1>
    <h1> a </h1><h1> a </h1><h1> a </h1>



   <v-app id="">
    <Footer ref="drawer"></Footer>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

import NavBar from "./components/NavBar.vue"
import Footer from "./components/Footer.vue"

export default {
  name: 'DescProj',
  components: {
    NavBar: NavBar,
    Footer: Footer
    }
  }

</script>

<template>
  <div>
    <!-- <v-app id=""> -->
      <nav-bar ref="drawer" />
      <section id="content">
        <router-view></router-view>
      </section>
      <footer-bar ref="drawer" />
    <!-- </v-app> -->
  </div>
</template>
 
<script>
import NavBar from "./components/NavBar";
import FooterBar from "./components/Footer";

export default {
  name: "App",
  components: {
    NavBar,
    FooterBar,
  },
};
</script>
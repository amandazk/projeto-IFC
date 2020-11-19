<template>
  <v-app id="portal">
    <nav-bar-component />
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import NavBarComponent from "./components/NavBarComponent.vue";
export default {
  components: { NavBarComponent },
};
</script>

<style>
</style>template
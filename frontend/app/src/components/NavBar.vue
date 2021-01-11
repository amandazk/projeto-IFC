<template>
  <nav
    class="navbar navbar-expand-md navbar-dark"
    style="background-color: #9bb694"
  >
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <img
        src="../assets/pequeno.png"
        width="160"
        height="40"
        class="d-inline-block align-top"
        alt=""
      />
      <ul class="navbar-nav mr-auto mt-2 ml-4 mt-lg-0">
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="/"
            >Home</a
          >
        </li>
        <!-- <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="#">Notícias</a>
        </li> -->
        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/campanhas"
            >Campanhas</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/servicos"
            >Serviços</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/voluntariados"
            >Voluntariado</a
          >
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <a class="btn btn-outline-dark my-2 my-sm-0"
          v-if="isLoggedIn"
          v-on:click="logout"
          href="/login"
        >
          Sair
        </a>
        <a class="btn btn-outline-dark my-2 my-sm-0"
          v-else
          v-on:click="login"
          href="/login"
        >
          Entrar
        </a>
      </form>
    </div>
  </nav>
</template>
 
<script>
export default {
  name: "NavBar",
  computed: {
    isLoggedIn() {
      return window.localStorage.getItem("psIfc");
    },
  },
  methods: {
    logout() {
      window.localStorage.removeItem("psIfc");
      this.$router.go();
    },
  },
};
</script>

<style>
.navbar-nav > li {
  padding-left: 7px;
  padding-right: 7px;
}
</style>
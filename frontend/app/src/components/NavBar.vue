<template>
  <nav
    class="navbar navbar-expand-md navbar-dark"
    style="background-color: #9BB694;"
  >
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <img
        src="../assets/logo_p.png"
        width="160"
        height="40"
        class="d-inline-block align-top"
        alt=""
      />
      <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="#">Notícias</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="/campanhas">Campanhas</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="#">Serviços</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="#">Iniciativas</a>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <button class="btn btn-outline-dark my-2 my-sm-0" href="#">
          Entrar
        </button>
      </form>
    </div>
  </nav>
</template>
 
<script>
export default {
  name: "NavBar",
};
</script>

<style>
.navbar-nav > li {
  padding-left: 7px;
  padding-right: 7px;
}
</style>
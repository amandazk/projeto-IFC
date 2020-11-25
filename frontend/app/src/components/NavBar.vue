<template>

<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-success">

  <div class="collapse navbar-collapse" id="navbarsExampleDefault">
    <ul class="navbar-nav mr-auto">
      <a class="navbar-brand" href="#">
    <img src="../assets/pequno.png" width="160" height="40" class="d-inline-block align-top" alt="">
      </a>
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Notícias</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Campanhas</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Serviços</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Iniciativas</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Cadastro</a>
      </li>
      <li class="form-inline my-2 my-lg-0">
        <a class="btn btn-outline-success my-2 my-sm-0" href="#">Entrar</a>
      </li>
    </ul>
  </div>
</nav>
  
</template>

<script>
export default {
    name: "NavBar"
}
</script>
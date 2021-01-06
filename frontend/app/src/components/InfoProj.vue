<template>
  <div class="container">
    <v-app id="">
      <NavBar ref="drawer"></NavBar>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>

    <div class="how-section1">
      <div class="row">
        <div class="col-md-6 how-img">
          <img src="../assets/1.png" class="rounded-circle img-fluid" alt="" />
        </div>
        <div class="col-md-6">
          <h4>Como fazer o cadastro?</h4>
          <p class="text-muted">
            Primeiro é necessário fazer o login no site. Se você ainda não é
            cadastrado, entre na página de login, no menu "Entrar" e selecione a
            opção de registrar-se. Após isso, você poderá fazer o login e entrar
            na página de cadastros de campanhas, serviços ou voluntariado.
          </p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <p class="text-muted">
            Então é necessário escolher qual tipo de cadastro você deseja fazer.
            Existem as seguintes opções: <br />
            <br />
            • <b>Campanhas</b> : Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Ut sit amet purus eu leo tincidunt placerat non
            quis turpis. <br />
            • <b>Serviços</b> : Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Ut sit amet purus eu leo tincidunt placerat non
            quis turpis. <br />
            • <b>Voluntariado</b> : Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Ut sit amet purus eu leo tincidunt placerat non
            quis turpis.
          </p>
        </div>
        <div class="col-md-6 how-img">
          <img src="../assets/2.png" class="rounded-circle img-fluid" alt="" />
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 how-img">
          <img src="../assets/3.png" class="rounded-circle img-fluid" alt="" />
        </div>
        <div class="col-md-6">
          <p class="text-muted">
            Por fim, as suas informações serão revisadas por um administrados. 
            Se o cadastro estiver correto, será publicado no nosso site, 
            disponibilizando as informações para outros usuários.
            Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Ut sit amet purus eu leo tincidunt placerat non
            quis turpis.
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
export default {
  name: "InfoProj",
  data() {},
};
</script>

<style>
.how-section1 {
  margin-top: -15%;
  padding: 10%;
}
.how-section1 h4 {
  color: rgba(71, 82, 94, 100);
  font-weight: bold;
  font-size: 30px;
}
.how-section1 .subheading {
  color: #3931af;
  font-size: 20px;
}
.how-section1 .row {
  margin-top: 10%;
}
.how-img {
  text-align: center;
}
.how-img img {
  width: 70%;
}
.h2 {
  text-align: center;
}
</style>
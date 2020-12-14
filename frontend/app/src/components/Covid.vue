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
          <img
            src="../assets/covid-19.png"
            class="rounded-circle img-fluid"
            alt=""
          />
        </div>
        <div class="col-md-6">
          <h4>O que é Coronavírus?</h4>
          <p class="text-muted">
            Coronavírus é uma família de vírus que causam infecções
            respiratórias. Alguns coronavírus podem causar doenças graves com
            impacto importante em termos de saúde pública, como a Síndrome
            Respiratória Aguda Grave (SARS), identificada em 2002, e a Síndrome
            Respiratória do Oriente Médio (MERS), identificada em 2012. O novo
            agente do coronavírus (SARS-CoV-2) foi descoberto no final de 2019
            após casos registrados na China e provoca a doença chamada de
            Covid-19. O número de casos registrados mobilizou organismos
            internacionais e a comunidade científica na busca por respostas
            sobre prevenção, transmissão e tratamento desse novo tipo de
            coronavírus.
          </p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <h4>Prevenção</h4>
          <p class="text-muted">
            Para afastar o risco de doenças, principalmente em tempos de
            pandemia da Covid-19, vale a pena incorporar alguns outros cuidados
            ao seu dia a dia. <br />
            • Lave sempre as mãos. Use sabão e água ou álcool em gel; <br />
            • Cubra a boca ao tossir ou espirrar; <br />
            • Mantenha o distânciamento social; <br />
            • Use máscara quando não for possível manter o distanciamento
            físico. <br />
            • Evite tocar nos olhos, nariz e boca; <br />
            • Fique em casa se não se sentir bem.
          </p>
        </div>
        <div class="col-md-6 how-img">
          <img
            src="../assets/gel.png"
            class="rounded-circle img-fluid"
            alt=""
          />
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 how-img">
          <img
            src="../assets/mascara.png"
            class="rounded-circle img-fluid"
            alt=""
          />
        </div>
        <div class="col-md-6">
          <h4>Formas de Contágio</h4>
          <p class="text-muted">
            A transmissão costuma ocorrer pelo ar ou por contato pessoal com
            secreções contaminadas, como: <br />
            • Gotículas de saliva; <br />
            • Espirro; <br />
            • Tosse; <br />
            • Catarro; <br />
            • Contato pessoal próximo, como toque ou aperto de mão; <br />
            • Contato com objetos ou superfícies contaminadas, seguido de
            contato com a boca, nariz ou olhos.
          </p>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="jumbotron bg-white text-dark">
        <h6><b>Fontes</b></h6>
        <ul>
          <li>
            <a href="http://www.saude.pa.gov.br/transmissao/"
              >Secretaria de Saúde Público do Estado do Pará</a
            >
          </li>
          <li>
            <a href="https://www.saude.sc.gov.br/coronavirus/doenca.html"
              >Secretaria de Estado da Saúde de SC</a
            >
          </li>
          <li>
            <a
              href="https://saude.abril.com.br/bem-estar/higiene-pessoal-em-tempos-de-covid-19/"
              >Saúde Abril</a
            >
          </li>
        </ul>
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
  name: "Covid",
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
.jumbotron {
  background-color: #9bb694 !important;
  /* background-size: 70%; */
  padding-top: 30px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
  padding-right: 20px !important;
  /* height: 50%; */
  /* width: 60%; */
  /* text-align: center; */


}
</style>
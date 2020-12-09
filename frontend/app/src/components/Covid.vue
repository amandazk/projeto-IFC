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
                            <img src="https://image.ibb.co/dDW27U/Work_Section2_freelance_img1.png" class="rounded-circle img-fluid" alt=""/>
                        </div>
                        <div class="col-md-6">
                            <h4>O que é Coronavírus?</h4>
                        <p class="text-muted">Coronavírus é uma família de vírus que causam infecções respiratórias. Alguns coronavírus podem 
                        causar doenças graves com impacto importante em termos de saúde pública, como a Síndrome Respiratória Aguda Grave (SARS),
                         identificada em 2002, e a Síndrome Respiratória do Oriente Médio (MERS), identificada em 2012. O novo agente do
                          coronavírus (SARS-CoV-2) foi descoberto no final de 2019 após casos registrados na China e provoca a doença chamada
                           de Covid-19. O número de casos registrados mobilizou organismos internacionais e a comunidade científica na busca
                            por respostas sobre prevenção, transmissão e tratamento desse novo tipo de coronavírus.</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <h4>Transmissão</h4>
                                        <p class="text-muted">As investigações sobre a transmissão do coronavírus ainda estão em andamento,
                                         mas a disseminação da doença se dá por contato próximo de pessoa por pessoa e pode ocorrer de forma continuada.
                                        Alguns vírus são altamente contagiosos (como sarampo), enquanto outros são menos. Ainda não está claro 
                                        com que facilidade o coronavírus se espalha de pessoa para pessoa.</p>
                        </div>
                        <div class="col-md-6 how-img">
                            <img src="https://image.ibb.co/cHgKnU/Work_Section2_freelance_img2.png" class="rounded-circle img-fluid" alt=""/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6 how-img">
                             <img src="https://image.ibb.co/ctSLu9/Work_Section2_freelance_img3.png" class="rounded-circle img-fluid" alt=""/>
                        </div>
                        <div class="col-md-6">
                            <h4>Formas de Contágio</h4>
                                        <p class="text-muted">A transmissão costuma ocorrer pelo ar ou por contato pessoal com secreções
                                         contaminadas, como: <br>
                                          • Gotículas de saliva; <br>
                                          • Espirro; <br>
                                          • Tosse; <br>
                                          • Catarro; <br>
                                          • Contato pessoal próximo, como toque ou aperto de mão; <br>
                                          • Contato com objetos ou superfícies contaminadas, seguido de contato com a boca, nariz ou olhos.</p>
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
  name: "Covid",
  data() {
    
}}

</script>

<style>

.how-section1{
    margin-top:-15%;
    padding: 10%;
}
.how-section1 h4{
    color: #ffa500;
    font-weight: bold;
    font-size: 30px;
}
.how-section1 .subheading{
    color: #3931af;
    font-size: 20px;
}
.how-section1 .row
{
    margin-top: 10%;
}
.how-img 
{
    text-align: center;
}
.how-img img{
    width: 40%;
}

</style>
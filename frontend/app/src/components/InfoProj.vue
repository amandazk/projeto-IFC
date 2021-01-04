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
          <h4>Como fazer o cadastro?</h4>
          <p class="text-muted">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse fermentum sit 
            amet odio sed facilisis. Aliquam ipsum leo, porttitor eget feugiat vitae, molestie 
            in lorem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur 
            ridiculus mus. Vestibulum lacus diam, tristique et facilisis ac, euismod eget odio. 
            Vivamus ultrices fermentum urna, quis elementum tortor gravida a. Ut placerat ligula 
            ut erat consectetur interdum. Phasellus tristique vitae felis et vestibulum. Nullam 
            semper, ante ut vulputate laoreet, diam sapien rhoncus libero, sed dapibus ante sem 
            non mauris. Fusce pharetra, nisi nec vestibulum ultricies, tortor neque condimentum.
          </p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <h4>Exemplo</h4>
          <p class="text-muted">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse fermentum sit 
            amet odio sed facilisis. Aliquam ipsum leo, porttitor eget feugiat vitae, molestie 
            in lorem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur 
            ridiculus mus. Vestibulum lacus diam, tristique et facilisis ac, euismod eget odio. 
            Vivamus ultrices fermentum urna, quis elementum tortor gravida a. Ut placerat ligula 
            ut erat consectetur interdum. Phasellus tristique vitae felis et vestibulum. Nullam 
            semper, ante ut vulputate laoreet, diam sapien rhoncus libero, sed dapibus ante sem 
            non mauris. Fusce pharetra, nisi nec vestibulum ultricies, tortor neque condimentum.
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
          <h4>Exemplo</h4>
          <p class="text-muted">
           Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse fermentum sit 
            amet odio sed facilisis. Aliquam ipsum leo, porttitor eget feugiat vitae, molestie 
            in lorem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur 
            ridiculus mus. Vestibulum lacus diam, tristique et facilisis ac, euismod eget odio. 
            Vivamus ultrices fermentum urna, quis elementum tortor gravida a. Ut placerat ligula 
            ut erat consectetur interdum. Phasellus tristique vitae felis et vestibulum. Nullam 
            semper, ante ut vulputate laoreet, diam sapien rhoncus libero, sed dapibus ante sem 
            non mauris. Fusce pharetra, nisi nec vestibulum ultricies, tortor neque condimentum.
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
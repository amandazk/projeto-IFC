<template>
  <div class="container">
    <div class="row d-flex justify-content-center">
      <div class="col-lg-4 col-sm-10 mb-4 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal" id="title">Card text</h4>
          </div>
          <div class="card-body">
            <ul class="list-unstyled mt-3 mb-4">
              <li>
                <p id="text-card">
                  Donec id elit non mi porta gravida at eget metus. Fusce
                  dapibus, tellus ac cursus commodo, tortor mauris condimentum
                  nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
                  malesuada magna mollis euismod. Donec sed odio dui
                </p>
                <p>
                  <a
                    class="btn btn-secondary p-2 mb-2"
                    href="#"
                    role="button"
                    >Saiba mais &raquo;</a
                  >
                </p>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-sm-10 mb-4 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal" id="title">Como se cadastrar</h4>
          </div>
          <div class="card-body">
            <ul class="list-unstyled mt-3 mb-4">
              <li>
                <p id="text-card">
                  Para efetuar o cadastro em nosso site é simples, basta clicar no botão ''Saiba mais''
                  e você vai entender qual cadastro deve realizar e quais suas finalidades.
                </p>
                <p>
                  <a
                    class="btn btn-secondary p-2 mb-2"
                    href="#"
                    role="button"
                    >Saiba mais &raquo;</a
                  >
                </p>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-sm-10 mb-4 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal" id="title">Cuidados na pandemia</h4>
          </div>
          <div class="card-body">
            <ul class="list-unstyled mt-3 mb-4">
              <li>
                <p id="text-card">
                  Durante essa época difícil que estamos passando é importante estarmos sempre 
                  prevenidos. Para isso, criamos essa área para você saber como se cuidar.
                </p>
                <p>
                  <a
                    class="btn btn-secondary p-2 mb-2"
                    href="/cuidados-covid"
                    role="button"
                    >Saiba mais &raquo;</a
                  >
                </p>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="row d-flex justify-content-center">
      <div class="col-lg-12 col-sm-12 mb-4 text-center">
        <h1 class="t1">Portal da Solidariedade</h1>
        <p class="texto">
          O Brasil é a sétima nação mais desigual do mundo atualmente e com
          <br />
          a questão da COVID-19 e o isolamento social, a desigualdade cresce
          <br />
          cada vez mais. A proposta deste projeto é a disponibilização do Portal
          <br />
          da Solidariedade, um ambiente web com a função de dar visibilidade
          <br />
          a estas pessoas.
          <br />
          <br />
          O projeto pretende oferecer espaço para que esta população em <br />
          vulnerabilidade social possa ser enxergada, possa disponibilizar
          <br />
          suas qualificações, seus saberes, apresentar seus produtos e serviços
          e,<br />
          desta forma, conseguir ampliar as suas possibilidades de serem
          incluídos nos<br />
          processos de proteção e também de recuperação dos efeitos da pandemia
          que,<br />
          seguramente, ainda vão se refletir por vários meses. Também as ações
          de<br />
          solidariedade que aos poucos vão acontecendo nas cidades poderão
          ser<br />
          hospedadas neste portal. Este conjunto de esforços, todos concentrados
          em<br />
          um local, permitindo a ampliação do suporte para os excluídos deste
          nosso país.<br />
        </p>
      </div>
    </div>
  </div>
</template>

<script>
//import router from "../router/index.js";
export default {
  name: "Index",
  data() {},
};
</script>

<style>
/* .navbar-default {
  margin: 0 !important;
} */

.container {
  margin-top: 70px;
}

.texto {
  margin-top: 15px;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 19px;
}

.t1 {
  margin-top: 25px;
  text-align: center;
}

/* .btn-secondary {
  text-align: center;
} */

.card {
  margin-right: 5px;
}
</style>
<template>
  <div class="container">
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <h1>Cadastro</h1>
        <!-- Login Form -->
        <form>
          <p>
            <label for="nome">Nome</label>
            <input
              type="text"
              id="nome"
              v-model="pessoa.nome_pessoa"
              class="fadeIn second"
              name="login"
            />
          </p>

          <p>
            <label for="cpf">CPF</label>
            <input
              type="text"
              id="cpf"
              v-model="pessoa.cpf_pessoa"
              class="fadeIn third"
              name="login"
            />
          </p>

          <p>
            <label for="email">Email</label>
            <input
              type="email"
              id="email"
              v-model="pessoa.email_pessoa"
              class="fadeIn third"
              name="login"
            />
          </p>

          <p>
            <label for="nasc">Data de Nascimento</label>
            <input
              type="date"
              id="nasc"
              v-model="pessoa.nasc_pessoa"
              class="fadeIn third"
              name="login"
            />
          </p>

          <p>
            <label for="fone">Fone</label>
            <input
              type="tel"
              id="fone"
              v-model="fone.nr_fone"
              class="fadeIn third"
              name="login"
            />
          </p>

          <input
            type="submit"
            class="fadeIn fourth"
            style="font-weight: bold"
            value="Cadastrar"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CreatePessoas",
  data: function () {
    return {
      dialog: false,
      // nome: [],
      // cpf: [],
      // email: [],
      // fone: [],
      pessoa: {},
      fone: {},
    };
  },
  created() {
    this.getPessoa();
  },
  methods: {
    getPessoa() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/pessoas/",
        })
        .then((response) => {
          this.pessoa = response.data;
          console.log(response);
        });
    },
    add() {
      axios
        .post("http://localhost:8000/api/pessoas/add/", this.pessoa, {
          headers: {
            Authorization: `Token ${this.$session.get("token")}`,
          },
        })
        .then((response) => {
          this.dialog = false;
          this.$emit("updatePessoa");
          this.log.console(response);
        });
    },
  },
};
</script>

<style>
.container {
  margin-top: 150px;
}

label {
  margin: 5px;
}

h1 {
  padding: 10px;
}

body {
  font-family: "Poppins", sans-serif;
  height: 100vh;
  /* overflow: hidden;  */
}

a {
  color: #56555e;
  display: inline-block;
  text-decoration: none;
  font-weight: 400;
}

h2 {
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  display: inline-block;
  margin: 40px 8px 10px 8px;
  color: #cccccc;
}

.wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #fff;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  /* -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3); */
  text-align: center;
}

#formFooter {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}

h2.inactive {
  color: #cccccc;
}

h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #9bb694;
}

input[type="button"],
input[type="submit"],
input[type="reset"] {
  background-color: #56555e;
  border: none;
  color: white;
  padding: 15px 80px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  text-transform: uppercase;
  font-size: 13px;
  /* -webkit-box-shadow: 0 10px 30px 0 #9bb694; */
  /* box-shadow: 0 10px 30px 0 #9bb694; */
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  margin: 5px 20px 40px 20px;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
  background-color: #868686;
}

input[type="button"]:active,
input[type="submit"]:active,
input[type="reset"]:active {
  -moz-transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -o-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

input[type="text"],
input[type="date"],
input[type="email"],
input[type="tel"] {
  background-color: #f6f6f6;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #f6f6f6;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

input[type="text"]:focus,
input[type="date"]:focus,
input[type="email"]:focus,
input[type="tel"]:focus {
  background-color: #fff;
  border-bottom: 2px solid #9bb694;
}

input[type="text"]:placeholder,
input[type="date"]:placeholder,
input[type="email"]:placeholder,
input[type="tel"]:placeholder {
  color: #cccccc;
}

*:focus {
  outline: none;
}
</style>
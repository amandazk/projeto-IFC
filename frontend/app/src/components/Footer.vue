<template>

    <div class="">
    <!----------- Footer ------------>
    <footer class="footer-bs">
        <div class="row">
          <div class="col-md-3 footer-brand animated fadeInLeft">
              <h2>Logo</h2>
                <p>Suspendisse hendrerit tellus laoreet luctus pharetra. Aliquam porttitor vitae orci nec ultricies. Curabitur vehicula, libero eget faucibus faucibus, purus erat eleifend enim, porta pellentesque ex mi ut sem.</p>
                <p>© 2020-2020, Todos os direitos reservados.</p>
            </div>
          <div class="col-md-4 footer-nav animated fadeInUp">
              <h4>Menu</h4>
              <div class="col-md-6">
                    <ul class="list">
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Notícias</a></li>
                        <li><a href="#">Campanhas</a></li>
                        <li><a href="#">Iniciativas</a></li>
                        <li><a href="#">Serviços</a></li>
                        <li><a href="#">Sobre nós</a></li>
                    </ul>
                </div>
            </div>
          <div class="col-md-2 footer-social animated fadeInDown">
              <h4>Redes sociais do IFC</h4>
              <ul>
                  <li><a href="https://www.facebook.com/ifc.oficial.araquari">Facebook</a></li>
                  <li><a href="#">Twitter</a></li>
                  <li><a href="https://www.instagram.com/ifc.oficial.araquari/">Instagram</a></li>
                  <li><a href="https://araquari.ifc.edu.br/">Site</a></li>
                </ul>
            </div>
        </div>
    </footer>
</div>

</template>

<script>
export default {
    name: "Footer"
}
</script>

<style>
.footer-bs {
  background-color: rgba(181, 205, 172, 100);
	padding: 60px 40px;
	color: rgba(71,82,94,100);
	margin-bottom: 20px;
	border-bottom-right-radius: 6px;
	border-top-left-radius: 0px;
	border-bottom-left-radius: 6px;
}
.footer-bs .footer-brand, .footer-bs .footer-nav, .footer-bs .footer-social, .footer-bs .footer-ns { padding:10px 25px; }
.footer-bs .footer-nav, .footer-bs .footer-social, .footer-bs .footer-ns { border-color: transparent; }
.footer-bs .footer-brand h2 { margin:0px 0px 10px; }
.footer-bs .footer-brand p { font-size:12px; color:rgba(71,82,94,100); }

.footer-bs .footer-nav ul.pages { list-style:none; padding:0px; }
.footer-bs .footer-nav ul.pages li { padding:5px 0px;}
.footer-bs .footer-nav ul.pages a { color:rgba(71,82,94,100); font-weight:bold; text-transform:uppercase; }
.footer-bs .footer-nav ul.pages a:hover { color:rgba(71,82,94,100); text-decoration:none; }
.footer-bs .footer-nav h4 {
	font-size: 11px;
	text-transform: uppercase;
	letter-spacing: 3px;
	margin-bottom:10px;
}

.footer-bs .footer-nav ul.list { list-style:none; padding:0px; }
.footer-bs .footer-nav ul.list li { padding:5px 0px;}
.footer-bs .footer-nav ul.list a { color:rgba(71,82,94,100); }
.footer-bs .footer-nav ul.list a:hover { color:rgba(71,82,94,100); text-decoration:none; }

.footer-bs .footer-social ul { list-style:none; padding:0px; }
.footer-bs .footer-social h4 {
	font-size: 11px;
	text-transform: uppercase;
	letter-spacing: 3px;
}
.footer-bs .footer-social li { padding:5px 4px;}
.footer-bs .footer-social a { color:rgba(71,82,94,100);}
.footer-bs .footer-social a:hover { color:rgba(71,82,94,100); text-decoration:none; }

.footer-bs .footer-ns h4 {
	font-size: 11px;
	text-transform: uppercase;
	letter-spacing: 3px;
	margin-bottom:10px;
}
.footer-bs .footer-ns p { font-size:12px; color:rgba(71,82,94,100); }

@media (min-width: 768px) {
	.footer-bs .footer-nav, .footer-bs .footer-social, .footer-bs .footer-ns { border-left:solid 1px rgba(255,255,255,0.10); }
}

</style>

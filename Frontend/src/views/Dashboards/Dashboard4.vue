<!-- eslint-disable prettier/prettier -->
<template>
  <b-container fluid>
    <b-row>
      <b-col sm="12">
        <b-row>
          <b-col lg="12">
            <h1 style="text-align: center; font-size: 30px">
              Comite de Transplantes
            </h1>
            <br />
            <h5 class="text-center">Transformando vidas, un donante a la vez.</h5>
            <br />
            <div class="iq-card-body p-0 rounded"
              :style="`background: url(${require('../../assets/images/page-img/comiteTransplantes/comiteBanner.jpg')}) no-repeat scroll center center; background-size: contain;  min-height: 446px;`">
            </div>
            <br />
          </b-col>

          <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
            <div style="display: flex; justify-content: space-between">
              <b-col md="4" lg="3">
                <iq-card>
                  <template v-slot:body>
                    <div class="iq-card-body p-0 rounded"
                      :style="`background: url(${require('../../assets/images/page-img/comiteTransplantes/letra.png')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`">
                    </div>
                    <h4 class="mb-2 mt-2" style="text-align: center">
                      Solicitud para Donanciones
                    </h4>
                    <div class="text-center">
                      <router-link :to="{ name: 'formWizard.simpleWizard' }">
                        <b-button variant="primary">Solicitar</b-button>
                      </router-link>
                    </div>
                  </template>
                </iq-card>
              </b-col>

              <b-col md="6" lg="3">
                <iq-card>
                  <template v-slot:body>
                    <div class="iq-card-body p-0 rounded"
                      :style="`background: url(${require('../../assets/images/page-img/comiteTransplantes/tabla-de-base-de-datos.png')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`">
                    </div>
                    <h4 class="mb-2 mt-2" style="text-align: center">
                      Solicitudes Generadas
                    </h4>
                    <div class="text-center">
                      <router-link :to="{ name: 'table.basic' }">
                        <b-button variant="primary">ver</b-button>
                      </router-link>
                    </div>
                  </template>
                </iq-card>
              </b-col>

              <b-col md="6" lg="3">
                <iq-card>
                  <template v-slot:body>
                    <div class="iq-card-body p-0 rounded"
                      :style="`background: url(${require('../../assets/images/page-img/comiteTransplantes/grafico.png')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`">
                    </div>
                    <h4 class="mb-2 mt-2" style="text-align: center">
                      Dashboard Comite de Transplantes
                    </h4>
                    <div class="text-center">
                      <router-link :to="{ name: 'dashboard.home-1' }">
                        <b-button variant="primary">Ver</b-button>
                      </router-link>
                    </div>
                  </template>
                </iq-card>
              </b-col>
            </div>
          </div>
        </b-row>
      </b-col>
    </b-row>

    <!-- --------------------------------------------------------------------------------------------------------------------------->
    <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
      <div style="display: flex; justify-content: space-between">
        <b-row>
          <b-col lg="12">
            <iq-card>
              <template v-slot:headerTitle>
                <h4 class="card-title">Comite de Transplantes</h4>
              </template>
              <template v-slot:body>
                <div style="text-align: justify">
                  <p>
                    La donación de órganos es un acto altruista que salva vidas. Cada año, miles de personas en todo el
                    mundo esperan desesperadamente un trasplante para poder seguir viviendo. Donar órganos es una
                    oportunidad única para brindar esperanza y renovar la vida de aquellos que lo necesitan. Tu decisión
                    de convertirte en donante puede marcar la diferencia entre la vida y la muerte para alguien en
                    necesidad.
                  </p>
                  <p>
                    La donación de trasplantes tiene un impacto significativo en la vida de los receptores y sus seres
                    queridos. Para los receptores, un trasplante puede significar la diferencia entre la vida y la
                    muerte, permitiéndoles recuperar su salud y calidad de vida. Además, la donación de órganos también
                    tiene un impacto emocional profundo en las familias donantes, al saber que el legado de su ser
                    querido continúa a través de la vida de otros. Esta generosidad y solidaridad en momentos de pérdida
                    son invaluables y crean un vínculo humano indeleble.
                  </p>
                </div>
              </template>
            </iq-card>
          </b-col>

          <b-col lg="6">
            <iq-card body-class="hospital-mgt" class="iq-card-block iq-card-height1">
              <template v-slot:headerTitle>
                <h4 class="card-title">Contacto</h4>
              </template>

              <template v-slot:body>
                <div>
                  <div>
                    <p>Dirección: calle nombre hospital general #352</p>
                    <p>Xicotepec de Juárez, Puebla C.P 73080</p>
                    <hr />
                    <p>Comunicate con Nosotros</p>
                    <li>
                      <p><a href="tel:+5253558858876">(52)33 55 885 8876</a></p>
                      <p><a href="tel:+5233558858878">(52)33 55 885 8878</a></p>
                      <p>
                        <a href="tel:+5233558858870">Fax: (52)33 55 885 8870</a>
                      </p>
                    </li>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>

          <b-col lg="6">
            <iq-card body-class="hospital-mgt" class="iq-card-block iq-card-height1">
              <template v-slot:headerTitle>
                <h4 class="card-title">Enlaces</h4>
              </template>

              <template v-slot:body>
                <div>
                  <div>
                    <p>Correo Electronico</p>
                    <p>
                      <a href="mailto:comitetransplantes@hospitalgeneral.com">comitetransplantes@hospitalgeneral.com</a>
                    </p>
                    <hr />
                    <iq-card>
                      <template v-slot:headerTitle>
                        <h4 class="card-title">Redes Sociales</h4>
                      </template>
                      <div style="text-align: center">
                        <link rel="stylesheet"
                          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
                        <!-- Facebook -->
                        <i class="fab fa-facebook-f fa-2x" style="color: #3b5998; margin-right: 25px"></i>

                        <!-- Twitter -->
                        <i class="fab fa-twitter fa-2x" style="color: #55acee; margin-right: 25px"></i>

                        <!-- Instagram -->
                        <i class="fab fa-instagram fa-2x" style="color: #ac2bac; margin-right: 25px"></i>

                        <!-- Linkedin -->
                        <i class="fab fa-linkedin-in fa-2x" style="color: #0082ca; margin-right: 25px"></i>

                        <!-- Youtube -->
                        <i class="fab fa-youtube fa-2x" style="color: #ed302f; margin-right: 25px"></i>

                        <!-- Whatsapp -->
                        <i class="fab fa-whatsapp fa-2x" style="color: #25d366; margin-right: 25px"></i>
                      </div>
                    </iq-card>
                  </div>
                </div>
              </template>
            </iq-card>
          </b-col>
        </b-row>
      </div>
    </div>

    <!-- --------------------------------------------------------------------------------------------------------------------------->
  </b-container>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import IqCard from "../../components/xray/cards/iq-card";
import { xray } from "../../config/pluginInit";
//import CountUp from 'vue-countup-v3'
const body = document.getElementsByTagName("body");

export default {
  name: "ComiteTransplantes",
  components: { IqCard },
  data() {
    return {
      config: {
        dateFormat: "Y-m-d",
        inline: true,
      },
    };
  },
  mounted() {
    xray.index();
    body[0].classList.add("sidebar-main-menu");
  },
  unmounted() {
    body[0].classList.remove("sidebar-main-menu");
  },
};
</script>

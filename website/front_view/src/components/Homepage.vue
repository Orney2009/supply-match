<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />

    <section class="text-black py-20 bg-gray-50">
      <div class="container mx-auto px-4 md:px-0 grid grid-cols-1 md:grid-cols-2 items-center gap-12">
        <div class="text-center md:text-left">
          <h1 class="text-4xl md:text-5xl font-bold mb-4">
            Découvrez notre plateforme
          </h1>

          <p class="text-lg md:text-xl mb-6 text-justify">
            Grâce à notre plateforme, trouvez les meilleures entreprises au Bénin et créez votre profil pour être
            visible.
            <br />
            Que vous soyez entrepreneur, investisseur ou particulier, notre plateforme est votre alliée pour réussir.
          </p>

          <router-link to="/register"
            class="inline-block bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-300 transition">
            Créer votre profil
          </router-link>
        </div>

        <div class="flex justify-center md:justify-end">
          <div class="containers">
            <div class="hero-circle">
              <img class="inner-img" src="../assets/image1.jpg" alt="" />

              <div class="hero-rotate">
                <div class="planet">
                  <img src="../assets/image1.jpg" />
                </div>
                <div class="planet">
                  <img src="../assets/image2.jpg"/>
                </div>
                <div class="planet">
                  <img src="../assets/image3.jpg" />
                </div>
                <div class="planet">
                  <img src="../assets/image4.jpg" />
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <section class="py-20 bg-white">
      <div class="container mx-auto px-4 md:px-0">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12"> Nos Services </h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-gray-50 p-6 rounded-xl shadow hover:shadow-lg transition text-center">
            <img src="../assets/rechercher.png" alt="Recherche facile" class="w-16 h-16 mx-auto mb-4" />
            <h3 class="text-xl font-semibold mb-2">Recherche facile</h3>
            <p class="text-gray-600">
              Trouver rapidement les entreprises béninoises par nom, secteur ou ville grâce à notre moteur de recherche
              optimisé.
            </p>
          </div>

          <div class="bg-gray-50 p-6 rounded-xl shadow hover:shadow-lg transition text-center">
            <img src="../assets/utilisateur.png" alt="Création de profil" class="w-16 h-16 mx-auto mb-4" />
            <h3 class="text-xl font-semibold mb-2">Création de profil</h3>
            <p class="text-gray-600">
              Permettre aux entreprises de se présenter, partager leurs services et rester visibles auprès des
              partenaires et clients.
            </p>
          </div>

          <div class="bg-gray-50 p-6 rounded-xl shadow hover:shadow-lg transition text-center">
            <img src="../assets/collaboration.png" alt="Collaboration facile" class="w-16 h-16 mx-auto mb-4" />
            <h3 class="text-xl font-semibold mb-2">Collaboration & Opportunités</h3>
            <p class="text-gray-600">
              Faciliter les échanges, partenariats et transactions grâce aux outils intégrés de communication et
              e-services.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 bg-gray-50" id="contact">
      <div class="max-w-6xl max-lg:max-w-3xl mx-auto bg-white p-4">
        <div
          class="grid lg:grid-cols-2 gap-16 items-center relative overflow-hidden p-8 [box-shadow:0_2px_10px_-3px_rgba(6,81,237,0.3)] before:absolute before:right-0 before:w-[300px] before:bg-blue-600 before:h-full max-lg:before:hidden">
          <div>
            <h2 class="text-slate-900 text-3xl font-bold">Contactez-nous</h2>
            <form>
              <div class="space-y-4 mt-8">
                <input type="text" placeholder="Nom complet"
                  class="px-2 py-3 bg-white w-full text-slate-900 text-sm border-b border-slate-300 focus:border-blue-600 outline-none" />


                <input type="email" placeholder="Email"
                  class="px-2 py-3 bg-white w-full text-slate-900 text-sm border-b border-slate-300 focus:border-blue-600 outline-none" />

                <textarea placeholder="Votre message"
                  class="px-2 pt-3 bg-white w-full text-slate-900 text-sm border-b border-slate-300 focus:border-blue-600 outline-none"></textarea>
              </div>

              <button type="button"
                class="mt-8 flex items-center justify-center text-sm font-medium w-full px-4 py-2.5 bg-blue-600 hover:bg-blue-700 text-white cursor-pointer">

                Envoyer
              </button>
            </form>


          </div>

          <div class="z-10 relative  ">

            <img src="../assets/contact.jpg" alt="">
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import Footer from './Footer.vue';
import Navbar from './Navbar.vue';

export default {
  name: 'Homepage',
  components: {
    Navbar,
    Footer
  }
}

</script>

<style scoped>
.containers {
  display: grid;

  place-items: center;

  --circleDiameter: 500px;
  --planets: calc(var(--circleDiameter) / 5)
}

.hero-circle {
  position: relative;
  width: var(--circleDiameter);
  height: var(--circleDiameter)
}

.inner-img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  overflow: hidden;
  border-radius: 10px;
  width: 150px;
  height: 120px; 
}

.hero-rotate {
  position: relative;
  top: -7px;
  left: -7px;
  width: 100%;
  height: 100%;
  border: 7px solid blue;
  border-radius: 100%;
  animation: rotate 30s linear infinite;
}

.planet {
  position: absolute;
  width: var(--planets);
  aspect-ratio: 1;
  border-radius: 100%;
  animation: maintain 30s linear infinite;
}


.planet:nth-child(1) {
  top: calc(-1 * var(--planets) / 2);
  left: calc(var(--circleDiameter)/ 2 - var(--planets) / 2 - 5px)
}

.planet:nth-child(2) {
  top: calc(var(--circleDiameter)/ 2 - var(--planets) / 2 - 5px);
  right: calc(-1 * var(--planets) / 2);
}

.planet:nth-child(3) {
  top: calc(var(--circleDiameter)/ 2 - var(--planets) / 2 - 5px);
  left: calc(-1 * var(--planets) / 2);
}

.planet:nth-child(4) {
  left: calc(var(--circleDiameter)/ 2 - var(--planets) / 2 - 5px);
  bottom: calc(-1 * var(--planets) / 2);
}

.planet>img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border: 5px solid blue;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  animation: scale 1s linear infinite alternate;
}

@keyframes rotate {
  0% {
    transform: rotate(0)
  }

  100% {
    transform: rotate(360deg);
  }
}

@keyframes maintain {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(-360deg);
  }
}

@keyframes scale {
  0% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}
</style>

<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import EducacionComponente from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponentes from './components/ProyectosComponentes.vue';
import FooterComponente from './components/FooterComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
</script>

<template>
  <!--html-->
<header>
  <!--barra de navegación-->
  <NavBar />
  <DatosPersonales/>
</header>
<main>
  <section id="educacion" class="titulo"><h2 class="principal">Educación</h2>
    <EducacionComponente/>
  </section>
 
  <section id="experiencia" class="titulo"><h2>Experiencia</h2>
  <ExperienciaComponente/>
  </section>
  <section id="proyectos" class="titulo"><h2>Proyectos</h2>
    <ProyectosComponentes/>
  </section>
  <section id="habilidades" class="titulo"><h2></h2></section>
  <HabilidadesComponente/>
</main>
<footer>
  <FooterComponente/>
</footer>
</template>

<style scoped>
.titulo{
  color:#141414;
}
</style>

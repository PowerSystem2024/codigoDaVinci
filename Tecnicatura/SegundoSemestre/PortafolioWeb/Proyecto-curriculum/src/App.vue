<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import EducacionComponente from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponentes from './components/ProyectosComponentes.vue';
</script>

<template>
  <!--html-->
<header>
  <!--barra de navegación-->
  <NavBar />
  <DatosPersonales/>
</header>
<main>
  <section id="educacion"><h2>Educación</h2>
    <EducacionComponente/>
  </section>
 
  <section id="experiencia"><h2>Experiencia</h2>
  <ExperienciaComponente/>
  </section>
  <section id="proyectos"><h2>Proyectos</h2>
    <ProyectosComponentes/>
  </section>
  <section id="habilidades"><h2>Habilidades</h2></section>
  <section id="intereses"><h2>Intereses</h2></section>
</main>
</template>

<style scoped>


</style>

<script setup>
import java from '/src/components/icons/java-logo.svg';
import javascript from '/src/components/icons/js-ico.svg';
import python from '/src/components/icons/python-ico.svg';
import github from '/src/components/icons/github-ico.svg';
import node from '/src/components/icons/node-ico.svg';
import gitlab from '/src/components/icons/gitlab-ico.svg';
import jira from '/src/components/icons/jira-ico.svg';
import jenkins from '/src/components/icons/jenkins-ico.svg';
import spring from '/src/components/icons/spring-ico.svg';
import hibernate from '/src/components/icons/hibernate-ico.svg';
import junit from '/src/components/icons/junit-ico.svg';
import git from '/src/components/icons/git-ico.svg';
import argo from '/src/components/icons/Argo.svg';
import mysql from '/src/components/icons/MySQL.svg';
import sqlDeveloper from '/src/components/icons/sql-developer.svg';
import oracle from '/src/components/icons/Oracle.svg';
import docker from '/src/components/icons/Docker.svg';
import maven from '/src/components/icons/maven-apache.svg';




import { ref } from 'vue';

// Listas de iconos de habilidades
const lenguajes = ref([
  { id: 1, src: java, alt: 'Java' },
  { id: 2, src: javascript, alt: 'Javascript' },
  { id: 3, src: python, alt: 'Python' },
  { id: 4, src: oracle , alt: 'Oracle'},
  { od: 5, src: mysql , alt: 'MySQL'},
  { id: 6, src: sqlDeveloper, alt: 'SQLdeveloper'}
]);

const frameworks = ref([
  { id: 1, src: spring, alt: 'Spring' },
  { id: 2, src: hibernate, alt: 'Hibernate' },
  { id: 3, src: junit, alt: 'JUnit' },
  { id: 4, src: docker, alt: 'Docker' },
  { id: 5, src: node, alt: 'Nodejs' },
  { id: 6, src: maven, alt: 'Apache maven' },

]);

const varias = ref([
  { id: 1, src: git, alt: 'Git' },
  { id: 2, src: github, alt: 'GitHub' },
  { id: 3, src: gitlab, alt: 'GitLab' },
  { id: 4, src: jira, alt: 'Jira' },
  { id: 5, src: jenkins, alt: 'Jenkins' },
  { id: 6, src: argo , alt: 'Argo'},
]);
</script>

<template>
  <div class="habilidades">
    <h1>Tecnologías utilizadas</h1>
    
    <h2 class="programacion">Programación y otros</h2>
    <div class="grid-container">
      <div v-for="lenguaje in lenguajes" :key="lenguaje.id" class="grid-item">
        <img :src="lenguaje.src" :alt="lenguaje.alt" class="icon"/>
      </div>
    </div>

    <h2 class="frameworks"> Frameworks y otros </h2>
    <div class="grid-container">
      <div v-for="framework in frameworks" :key="framework.id" class="grid-item">
        <img :src="framework.src" :alt="framework.alt" class="icon"/>
      </div>
    </div>

    <h2 class="herramientas">Herramientas </h2>
    <div class="grid-container">
      <div v-for="item in varias" :key="item.id" class="grid-item">
        <img :src="item.src" :alt="item.alt" class="icon"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Contenedor principal */
.habilidades {
  text-align: center;
  padding: 20px;
  color: #141414;
}

.programacion{
  color: #141414;
}

.frameworks{
  color: #141414;
}

.herramientas{
color: #141414;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); /* Adaptable al tamaño de la pantalla */
  gap: 20px;
  margin-bottom: 40px;
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  border-radius: 10px;
  background-color: #f3f3f3;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.grid-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.icon {
  width: 60px;
  height: 60px;
  transition: transform 0.3s ease;
}

.icon:hover {
  transform: scale(1.1); /* Efecto al pasar el mouse sobre los iconos */
}

h2 {
  position: relative;
  font-size: 1.5rem;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #D6EAEB;
}

h2::before,
h2::after {
  content: '';
  position: absolute;
  width: 30%;
  height: 4px;
  background-color: #D6EAEB;
  top: 100%;
  left: 0;
  transform: translateY(10px);
}

h2::after {
  left: auto;
  right: 0;
}

/* Estilos responsive */
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: repeat(auto-fill, minmax(80px, 1fr)); /* Ajustar el tamaño en pantallas pequeñas */
  }

  .icon {
    width: 50px;
    height: 50px;
  }

  .grid-item {
    padding: 10px;
  }
}
</style>
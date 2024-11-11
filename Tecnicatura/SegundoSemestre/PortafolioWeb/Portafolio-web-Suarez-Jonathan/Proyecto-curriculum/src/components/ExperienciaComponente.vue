<script setup>
import {ref} from 'vue';
const titulo = 'Desarrollo de Software - Backend ';
const fecha = "Actualmente trabajando en relación de dependencia para software Factory ";
const experiencias = ref([
    {id: 1, src:'/src/assets/microservices-icon.svg', parrafo:'Migración de funcionalidades de aplicación monolítica a arquitectura de Microservicios'},
    {id: 2, src:'/src/assets/bank-icon.svg', parrafo:'Participación en desarollos para sectores bancas empresas '},
    {id: 3, src:'/src/assets/manteiner-icon.svg', parrafo:'Mantenimiento de aplicaciones monolíticas en paralelo con la migración'},

]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img  class="imagen-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card{
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: #F3F4F6;  /* Gris muy suave */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Sombra sutil alrededor */    border-radius: 15px;
}

.titulo{
    font-size: 1.5rem;
    color: #141414;
}

.fecha{
    font-size: 1.3rem;
    color: #464646;
    margin-bottom: 1rem;
}

.listado{
    display: flex;
    flex-direction: column;

}

.item{
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
    color:#000000;
}
</style>
<script setup>
import {ref} from 'vue';
const titulo = 'Varios campos del conocimiento y ahora Programación';
const fecha = "Desde junio de 1469 - Taller de Verrochio";
const experiencias = ref([
    {id: 1, src:'/src/assets/escultura-icon.svg', parrafo:'Años aprendiendo técnicas, perfeccionándolas. Desarrollando nuevas teorías, creatividad , mucha creatividad.'},
    {id: 2, src:'/src/assets/microservices-icon.svg', parrafo:' Adentrandome en el mundo que llaman microservicios. Construcción de servicios para artesanos y artistas en general. '},
    {id: 3, src:'/src/assets/manteiner-icon.svg', parrafo:'Mantenimiento de aplicaciones legacy y en migración. Cuidando el taller para que no se venga abajo mientras se construye el nuevo. '},

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
    background-color: rgb(28,41,52);
    border-radius: 15px;
}

.titulo{
    font-size: 1.5rem;
    color: coral;
}

.fecha{
    font-size: 1rem;
    color: burlywood;
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
}
</style>
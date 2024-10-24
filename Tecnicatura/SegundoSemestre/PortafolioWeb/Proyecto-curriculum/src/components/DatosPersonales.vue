<script setup>
const title = 'Leonardo Da Vinci';
const descripcion = 'Multifacético  y ahora incursionando en la Tecnicatura Universitaria en programación de la UTN';
const residencia = '-Villa Toscana de Vinci';
const presentacion = 'Hola , bienvenidos a mi mundo.';

const redesSociales = [
    {id: 1, name:'Linkedin', src:'/src/assets/linkedin-icon.svg' , url: 'https://www.linkedin.com/in/Jonathan'},
    {id: 2, name:'Instagram', src:'/src/assets/instagram-icon.svg' , url: ''},
    {id: 3, name:'GitHub', src:'/src/assets/github-icon.svg' , url: ''},
    {id: 4, name:'Curriculum', src:'/src/assets/curriculum-icon.svg' , url: ''},
];

const telefono = '1452';

</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{title}}</h1>
            <h2>{{descripcion}}</h2>
            <p>{{presentacion}}</p>
            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="15rem" :alt="red.name" ></a>
                </li>
            </ul>
            <h3>{{telefono}}</h3>
            <h4>{{ residencia }}</h4>
        </div>

    </section>

</template>

<style scoped>
h1{
    font-size: 2.5rem;
}

p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.card{
background-color: rgb(28,41,52);
border-radius: 10px;
padding: 10px;
margin:10px;
text-align: center;
}

.container-lista{
 display: flex;
 justify-content: center;
 list-style: none;
 padding: 0;
 margin: 0;
 text-align: center;
}

.icon-redsocial{
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
    background-color: rgb(28, 41, 52);
    box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3{
    font-size: 1.2rem;
    font-weight: 600;
}
</style>

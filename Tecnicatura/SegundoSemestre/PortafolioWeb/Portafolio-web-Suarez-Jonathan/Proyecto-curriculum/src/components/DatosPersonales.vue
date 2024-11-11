<script setup>
const title = 'Jonathan Suarez';
const descripcion = 'Desarrollador Backend ';
const residencia = 'San Rafael - Mendoza ';
const presentacion = '';

const redesSociales = [
    {id: 1, name:'Linkedin', src:'/src/assets/linkedin-icon.svg' , url: 'https://www.linkedin.com/in/jonathan35622/'},
    {id: 2, name:'GitHub', src:'/src/assets/github-icon.svg' , url: 'https://github.com/jonathan35622'},
    {id: 3, name:'Curriculum', src:'/src/assets/curriculum-icon.svg' , url: ''},
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
/* Colores de la paleta */
:root {
  --gutsiest-sand-yellow: #FDE166;
  --revitalized-pinkish: #D46A7E;
  --paper-petrol: #015F6B;
}

/* Estilo para el título */
h1 {
    font-size: 2.5rem;
    color: #464646;
    animation: moverTitulo 10s ease-in-out infinite ;
}

/* Estilo para la descripción */
h2 {
    font-size: 1.5rem;
    color: #464646;;
}

/* Estilo para el párrafo */
p {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #000000; /* Usando el color gutsiest sand yellow */
}

/* Estilo para la tarjeta */
.card {
    background-color: var(--paper-petrol); /* Usando el color paper petrol como fondo */
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
    color: white; /* Color blanco para el texto */
}

/* Estilo para la lista de redes sociales */
.container-lista {
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

/* Estilo para los iconos de redes sociales */
.icon-redsocial {
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
    width: 40px;  /* Ajusta el tamaño de la imagen según sea necesario */
    height: 50px; /* Mantén la misma altura para que sea un círculo */
    object-fit: cover; /* Hace que la imagen cubra el área sin distorsionarse */
}

/* Hover sobre iconos de redes sociales */
.icon-redsocial:hover {
    background-color: var(--paper-petrol); /* Usando el color paper petrol en el hover */
   
}

/* Estilo para el número de teléfono */
h3 {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--revitalized-pinkish); /* Usando el color revitalized pinkish */
}

/* Estilo para la residencia */
h4 {
    font-size: 1.1rem;
    color: var(--gutsiest-sand-yellow); /* Usando el color gutsiest sand yellow */
}

@keyframes moverTitulo {
    0% {
        transform: translateX(-100%); /* Empieza fuera de la pantalla, a la izquierda */
        opacity: 0;
    }
    50% {
        transform: translateX(0); /* Se mueve al centro */
        opacity: 1;
    }
    100% {
        transform: translateX(100%); /* Se mueve fuera de la pantalla, a la derecha */
        opacity: 0;
    }
}
</style>
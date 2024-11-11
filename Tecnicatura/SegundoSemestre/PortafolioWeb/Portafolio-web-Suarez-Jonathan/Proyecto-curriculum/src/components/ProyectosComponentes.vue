<script setup>
import logoCiudad from '@/assets/banco-logo.svg';
import logoMicroservicios from '@/assets/microservice.png';
import logoMantenimiento from '@/assets/manteiner-ico.svg';
import logoAppComunidad from '@/assets/comunidad-ico.svg';

</script>

<template>
    <div class="galeria">
        <div class="proyecto">
            <img :src="logoCiudad" alt="Proyecto 1">
            <div class="proyecto-info">
                <h3>Bancas empresas</h3>
                <p>Participación como desarrollador backend en diferentes proyectos y para diferentes bancos </p>
                <h4 class="proyecto-privado">Repositorios privados</h4>
            </div>
        </div>
        <div class="proyecto">
            <img :src="logoMicroservicios" alt="Proyecto 1">
            <div class="proyecto-info">
                <h3>Desarrollo de API REST para Bancas Empresas</h3>
                <p>Exposición de endpoints para comunicación entre microservicios</p>
                <h4 class="proyecto-privado">Repositorios privados</h4>
            </div>
        </div>
        <div class="proyecto">
            <img :src="logoAppComunidad" alt="Proyecto 1">
            <div class="proyecto-info">
                <h3>Aplicación para ofrecer hogar a personas en situación de calle </h3>
                <p>participación desarrollo backend cliente español</p>
                <h4 class="proyecto-privado">Repositorios privados</h4>
              
            </div>
        </div>

        <div class="proyecto">
            <img :src="logoMantenimiento" alt="Proyecto 1">
            <div class="proyecto-info">
                <h3>Mantenimiento de aplicaciones</h3>
                <p>Mantenimientos de microservicios y aplicaciones monolíticas</p>
                <h4 class="proyecto-privado">Repositorios privados</h4>
            </div>
        </div>
    </div>


</template>

<style scoped>
.galeria {
    width: 100%;
    height: 100%;
    display: grid;
    /**display: flex;*/
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    flex-wrap: wrap;
    /*distribuye las tarjetas que tenga dentreo del contenedor galeria */
    background-color: #F3F4F6;
    /* Gris muy suave */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    /* Sombra sutil alrededor */

    gap: 20px;
    /*espacio entre tarjeta y tarjeta */
    padding: 20px;
    /*agrega un padding de 20px alrededor de la galeria */
    justify-content: center;
    /*las tarjetas quedaran centradas dentro de galeria */
    background-size: 400% 400%;
    /*ajusta el tamaño del fodo para que cubra el área completa */
    animation: gradient 15s ease infinite;
}

/*Define una animación llamada 'gradient' para cambiar la posiciónm del fondo */
@keyframes gradient {

    /*al inicio , el fondo está poosicionado en el 0% horizontal y 50% vertical */
    0% {
        background-position: 100% 50%;
    }

    /*a la mitad de la animación , el fondo se desplaza al 100% horizontal */
    50% {
        background-position: 100% 50%;
    }

    /* al final , el fondo vuelve a la posición inicial*/
    100% {
        background-position: 0% 50%;
    }
}


/*la clase 'proyecto' es el contenedor individual de cada proyecto */
.proyecto {
    display: flex;
    /*utiliza flexbox para organizar el contenido del proyecto en una columna */
    flex-direction: column;
    /*establece la dirección de los elementos en columna */
    border: 2px solid #ddd;
    /*aplica un borde de 2px solido y color gris claro (#ddd) alrededor del proyecto */
    border-radius: 8px;
    /*redondea las esquinas del contenedor */
    overflow: hidden;
    /*oculta cualquier contenido que se desborde del contenedor */
    background-color: #f9f9f9;
    max-width: 222px;
    /*define el ancho máximo del proyecto en 222px */
    flex: 1 1 300px;
    /* hace que el contenedor se ajuste flexiblemente ocupando al menos 300 px de ancho */
}

/*estilo para las imagenes dentro del contenedor 'proyecto' */
.proyecto img {
    /*hace que la imagen ocupe el 100% del ancho del contenedor */
    width: 100%;
    /*Mantiene la relación de aspecto de la imagen */
    height: auto;
    /*asegura que la imagen se muestre como un bloque, sin espacio en línea alrededor */
    display: block;
}

/*La clase 'proyecto-info' contiene la información del proyecto*/
.proyecto-info {
    /*Agrega un padding de 15px alrededor de la información */
    padding: 15px;
    /*Centra el texto dentro del contenedor */
    text-align: center;
}

/*Estilo para los títulos de los proyectos */
.proyecto-info h3 {
    /*Establece un margen superior e inferior de 10px */
    margin: 10px 0;
    /*Define el tamaño de la fuente a 1.3em (relativo al tamaño de fuente del contenedor) */
    font-size: 1.3rem;
    /*aplica un color gris oscuro (#333) al texto */
    color: #333;
}

/*Estilo para los párrafos de los proyectos */
.proyecto-info p {
    /*Establece un margen superior e inferior de 10px */
    margin: 10 px 0;
    /*Define el tamaño de la fuente a 1em (igual al tamaño de fuente base) */
    font-size: 1em;
    /*Aplica un color gris (#666) al texto*/
    color: #666;
}

/*La clase 'proyecto-links' organiza los enlaces y botones del proyecto */
.proyecto-links {
    /*utiliza flexbox para organizar los enlaces en una columna */
    display: flex;
    /*Establece la dirección de los elementos en columna */
    flex-direction: column;
    /*Establece un espacio de 10px entre los elementos */
    gap: 10px;
    /*agrega un margen superior de 10px */
    margin-top: 10px;
}

/*Estilo para el botón 'Ver más' dentro de la clase 'proyecto-links'*/
.proyecto-links .btn-ver-mas {
    /*Aplica un color de fondo azul */
    background-color: #007BFF;
    /*Aplica un color de texto blanco */
    color: #fff;
    /*Agrega un padding de 10px en vertical y 15px en horizontal */
    padding: 10px 15px;
    /*Redondea las esquinas del botón */
    border-radius: 5px;
    /*Elimina el subrayado del texto */
    text-decoration: none;
    /*Aplica una transición suave al cambiar el color de fondo */
    transition: background-color 0.3s;
}

/*Estilo para cuando el botón 'Ver más' es hover */
.proyecto-links .btn-ver-mas:hover {
    background-color: #0056b3;
}

/*Estilo para el enlace a Github dentro de la clase 'proyecto-links' */
.proyecto-links .github-link {
    /*aplica un co lor gris oscuro (#333) al texto */
    color: #333;
    /*Elimina el subrayado del texto */
    text-decoration: none;
    /*Establece el tamaño de fuente a 0.9em ( un poco más pequeño que el tamaño base) */
    font-size: 0.9em;
}

/*Estilo para cuando el enlace de Github es hover */
.proyecto-links .github-link:hover {
    /*añade un subrayado al texto */
    text-decoration: underline;
}

.proyecto-privado {
    display: inline-block; /* Hace que el h4 se comporte como un bloque en línea */
    padding: 10px 20px; /* Agrega espacio alrededor del texto para darle aspecto de botón */
    margin-top: 15px; /* Este espacio será el que añada separación entre el último <p> y el <h4> */
    background-color: #007BFF; /* Color de fondo del botón (puedes cambiarlo a tu gusto) */
    color: white; /* Color del texto */
    text-align: center; /* Centra el texto dentro del área del botón */
    border-radius: 5px; /* Bordes redondeados */
    cursor: pointer; /* Cambia el cursor a una mano cuando se pasa por encima */
    font-weight: bold; /* Resalta el texto */
    text-transform: uppercase; /* Opcional, transforma el texto a mayúsculas */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra ligera para un efecto de botón */
    transition: background-color 0.3s, transform 0.2s; /* Animaciones para interacción */
}

.proyecto-privado:hover {
    background-color: #0056b3; /* Cambia el color de fondo cuando se pasa el mouse */
    transform: translateY(-2px); /* Efecto de desplazamiento hacia arriba */
}

.proyecto-privado:active {
    transform: translateY(2px); /* Efecto al presionar, simula un clic */
}

</style>

<script setup>
</script>

<template>
    <div class="galeria">
        <div class="proyecto">
            <img src="/src/assets/img-mona.jpeg" alt="Proyecto 1">
            <div class="proyecto-info">
                <h3>Pintura Mona Modern</h3>
                <p>Realicé una reversión de una de mis piezas clásicas. Fue toda una aventura</p>
                <div class="proyecto-links">
                    <a href="https://www.youtube.com/watch?v=yRK_uCMwZPY" class="btn-ver-mas" target="_blank" rel="nooper norefrrer">Ver Proyecto</a>
                    <a href="" class="github-link" target="_blank"
                    rel="noopener noreferrer">Ver código Github</a>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.galeria{
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;/*distribuye las tarjetas que tenga dentreo del contenedor galeria */
    gap: 20px; /*espacio entre tarjeta y tarjeta */
    padding: 20px;/*agrega un padding de 20px alrededor de la galeria */
    justify-content: center; /*las tarjetas quedaran centradas dentro de galeria */
    background: linear-gradient(-45deg, #021526, #03346e, #6eacda, #E2E2B6);
    background-size: 400% 400%;/*ajusta el tamaño del fodo para que cubra el área completa */
    animation: gradient 15s ease infinite;
}

/*Define una animación llamada 'gradient' para cambiar la posiciónm del fondo */
@keyframes gradient{
    /*al inicio , el fondo está poosicionado en el 0% horizontal y 50% vertical */
    0%{
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
    display: flex;/*utiliza flexbox para organizar el contenido del proyecto en una columna */ 
    flex-direction: column; /*establece la dirección de los elementos en columna */ 
    border: 2px solid #ddd;/*aplica un borde de 2px solido y color gris claro (#ddd) alrededor del proyecto */      
    border-radius: 8px;/*redondea las esquinas del contenedor */
    overflow: hidden; /*oculta cualquier contenido que se desborde del contenedor */
    background-color: #f9f9f9;
    max-width: 222px;/*define el ancho máximo del proyecto en 222px */
    flex: 1 1 300px;/* hace que el contenedor se ajuste flexiblemente ocupando al menos 300 px de ancho */
    }

    /*estilo para las imagenes dentro del contenedor 'proyecto' */
.proyecto img{
    /*hace que la imagen ocupe el 100% del ancho del contenedor */
    width: 100%;
    /*Mantiene la relación de aspecto de la imagen */
    height: auto;
    /*asegura que la imagen se muestre como un bloque, sin espacio en línea alrededor */
    display: block;
    }

    /*La clase 'proyecto-info' contiene la información del proyecto*/
    .proyecto-info{
        /*Agrega un padding de 15px alrededor de la información */
        padding: 15px;
        /*Centra el texto dentro del contenedor */
        text-align: center;
    }

    /*Estilo para los títulos de los proyectos */
    .proyecto-info h3{
    /*Establece un margen superior e inferior de 10px */
     margin: 10px 0;
     /*Define el tamaño de la fuente a 1.3em (relativo al tamaño de fuente del contenedor) */
     font-size: 1.3rem;
     /*aplica un color gris oscuro (#333) al texto */
     color: #333;
    }

    /*Estilo para los párrafos de los proyectos */
    .proyecto-info p{
        /*Establece un margen superior e inferior de 10px */
        margin: 10 px 0;
        /*Define el tamaño de la fuente a 1em (igual al tamaño de fuente base) */
        font-size: 1em;
        /*Aplica un color gris (#666) al texto*/
        color: #666;
    }

    /*La clase 'proyecto-links' organiza los enlaces y botones del proyecto */
    .proyecto-links{
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
    .proyecto-links .btn-ver-mas{
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
    .proyecto-links .btn-ver-mas:hover{
        background-color: #0056b3;
    }

    /*Estilo para el enlace a Github dentro de la clase 'proyecto-links' */
    .proyecto-links .github-link{
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
</style>

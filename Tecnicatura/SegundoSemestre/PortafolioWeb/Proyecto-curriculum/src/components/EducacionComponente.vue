<script setup>

import {ref } from 'vue';
const fechaColor = ref([]);
fechaColor.value = [
    {color:'#41516c'},
    {color:'#FBCA3E'},
    {color:'#E24A68'},
    {color:'#185F8C'},
    {color:'#4CADAD'},
];
const educacion = ref([]);
educacion.value = [
    {fecha:'2024', title:'Tecnicatura universitaria en programación', descripcion:'Cursando actualmente', enlace:'https://www.frsr.utn.edu.ar/'},
    {fecha:'2000', title:'Me adentré en conocimientos de programación ', descripcion:'tenía que actualizarme un poco', enlace:'https://www.youtube.com/watch?v=T8wyFbpmu8g'},
    {fecha:'1472', title:'Pintor / artista, experimentador', descripcion:'De esta época deriva uno de mis primeros trabajos conocidos, el Paisaje del valle del Arno o Paisaje de Santa Maria della neve', enlace:'https://es.m.wikipedia.org/wiki/Archivo:Study_of_a_Tuscan_Landscape.jpg'},
    {fecha:'1482', title:'Varios estudios sobre algoritmos', descripcion:'Escuela de  Paolo dal Pozzo Toscanelli y Leonardo Chernionese', enlace:'https://es.wikipedia.org/wiki/Leonardo_da_Vinci'},
];

</script>


<template>
 <ul>
    <li v-for="(item,index) in educacion" :key="index" :style="{'--fecha-color': fechaColor[index].color}">
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.title }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
        <!--aquí vemos con el uso de b-vind (:) que bindeamos el atributo href del html con el item.enlace-->
        <a class="enlace" :href="item.enlace" target="_blank">Saber más</a>
    </li>
 </ul>
</template>

<style scoped>
/*Estilos generales */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");
/*Reseteo de estilos básicos para todos los elementos y pseudo-elementos */
*,
*::before,
*::after{
    margin: 0; /*Elimina el margen predeterminado*/
    padding: 0; /*Elimina el padding predeterminado */
    box-sizing: border-box; /*Incluye el padding y el borde en el tamaño total del elemento */
}

/*Estilo para el cuerpo de la página */
body{
  --color: rgba(30,30,30); /*variable para el color de texto*/  
  --bgColor: rgba(245, 245, 245); /*variable para el color de fondo */  
  min-height: 100vh;/*Asegura que el cuerpo ocupe al menos el 100% de la altura de la ventana*/
  display: grid;/*utiliza el modelo de caja de cuadricula*/
  align-content: center;/*centra verticalmente el contenido dentro de la cuadricula */  
  gap:2rem; /* Espaciado entre los elementos de la cuadrícula*/
  padding: 2rem; /*Espaciado interno alrededor del cuerpo */  
  font-family: "Poppins", "sans-serif";
  color: var(--color); /*Aplica el color de texto definido en la variable*/
  background: var(--bgColor);/*aplica el color de fondo definido en la variable*/  
}

/*Estilos para la lista*/
ul{
    margin-top: 2rem;
    --col-gap: 2rem; /*Espacio entre las columnas de la cuadrícula*/
    --row-gap: 2rem; /*Espacio entre las  filas de la cuadrícula*/
    --line-w: 0.25rem; /*Ancho de la línea que conecta los  elementos de la lista */
    display: grid;/*usa un layout de cuadrícula */
    grid-template-columns: var(--line-w) 1fr; /*Define las columnas de la cuadrícula: la primera es la línea y la segunda es el contenido*/
    grid-auto-columns: max-content;/*Las columnas se ajustan automáticamente al contenido */
    column-gap: var(--col-gap);/*Espacio entre columnas */
    list-style: none;/*Elimina las viñetas predeterminadas de la lista*/
    width: min(60rem, 90%);
    margin-inline: auto; /*Centra la lista horizontalmente */
}

/*Estilo para la línea vertical que conecta los elementos de la lista */
ul::before{
    content: "";/*Elemento vacío para crear la línea */
    grid-column: 1; /*coloca la línea en la primera columna de la cuadrícula */
    grid-row: 1 / span 20; /*La línea se extiende sobre varias filas */
    background: rgb(225, 225, 225); /*color de la línea */
    border-radius: calc(var(--line-w) / 2);/*bordes redondeados para la línea*/
}

/*Estilo para los elementos de la lista que no son el último*/
ul li:not(:last-child){
    margin-bottom: var(--row-gap);/*espacio entre los elementos de la lista*/

}

/*Estilo para cada item de la lista */
ul li{
    grid-column: 2; /*coloca el contenido en la segunda columna de la cuadrícula */
    --inlineP: 1.5rem; /*Espacio interno horizontal dentro de cada item */
    margin-inline: var(--inlineP);/*Margen horizontal para los ítems */
    grid-row: span 2;/*cada item ocupa dos filas en la cuadrícula */
    display: grid; /*usa un layout de cuadrícula dentro de cada item */
    grid-template-rows: min-content min-content min-content;/*Define tres filas de altura mínima */
}

/*Estilo para la fecha dentro de cada item */
ul li .fecha{
    --dateH: 3rem; /*altura de la sección de la fecha */
    height: var(--dateH);
    margin-inline: calc(var(--inlineP) * -1);/*ajusta el margen horizontal para que la fecha sobresalga */
    text-align: center;/*centra el texto dentro de la fecha */
    background-color: var(--fecha-color);/*color de fondo, usando una variable personalizada */
    color: white; /*color del texto en la fecha */
    font-size: 1.25rem;/*tamaño del texto */
    font-weight: 700;/*hace el texto en negrita */
    display: grid;/*usa un layout de cuadrícula */
    place-content: center;/*centra el contenido de la fecha */
    position: relative;/*posiciona la fecha relativa a su contenedor */
    border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);/*Bordes redondeados para la fecha */
}

/*Estilo para la parte inferior de la fecha, que parece un triángulo */
ul li .fecha::before {
    content: ""; /*Elemento vacío para crear el triángulo */
    width: var(--inlineP); /*ancho igual al espacio interno definido */
    aspect-ratio: 1; /*Mantiene una relación de aspecto 1:1 para crear un cuadrado */
    background: var(--fecha-color);/*usa el color de fondo de la fecha */
    background-image: linear-gradient(rgba(0,0,0,0.2) 100% , transparent); /*aplica un degradado sutil para dar un efecto de sombra */
    position: absolute;/*posiciona el triángulo respecto al contenedor de la fecha */
    top: 100%; /*coloca el triángulo justo debajo de la fecha */
    clip-path: polygon(0 0, 100% 0, 0 100%);/*recorta el cuadrado para convertirlo en un triángulo */
    right: 0; /*alinea el triángulo a la derecha de la fecha */
}

/*Estilo para el círculo que conecta la fecha con la línea */
ul li .fecha::after{
    content: "";/*Elemento vacío para crear el círculo */
    position: absolute; /*posiciona el círculo respecto al contenedor de la fecha */
    width: 1rem;/*ancho del círculo */
    aspect-ratio: 1;/*Mantiene una relación de aspecto 1:1 para crear un círculo */
    background: var(--bgColor);/*color de fondo , utilizando la variable definida */
    border: 0.3rem solid var(--fecha-color);/*borde del círculo, con el color de la fecha */
    border-radius: 50%; /*centra verticalmente el círculo dentro del contenedor de la fecha */
    top:50%;
    transform: translate(50%, -50%);/*Ajusta la posición del círculo para alinearlo correctamente */
    right: calc(100% + var(--col-gap) + var(--line-w) / 2); /*coloca el círculo a la izquiuerda de la línea */
}

/*Estilos para el título y la descripción dentro de cada item */
ul li .title,
ul li .descripcion {
    background: var(--bgColor);/*fondos del título y la descripción, usando variable definida */
    position: relative;/* posiciona los elementos relativos a su contenedor */
    padding-inline: 1.5rem;/* espaciado interno horizontal */
}

ul li .title{
    overflow: hidden;/* oculta cualquier contenido que se desborde */
    padding-block-start: 1.5rem;/*espaciado interno superior */
    padding-block-end: 1rem;/* espaciado interno inferior */
    font-weight: 500;/*hace el texto del título un poco más grueso */
}

ul.li.descripcion{
    padding-block-end: 1.5rem;/*espaciado interno inferior */
    font-weight: 300;/*hace el texto de la descripción más delgado */
}

ul li .title::before,
ul li .descripcion::before {
    content: ""; /*Elemento vacío para crear la sombra */
    position: absolute; /*posiciona la sombra respecto al contenedor del título o descripción */
    width: 90%;/*ancho de la sombra */
    height: 0.5rem;/* altura de la sombra */
    background: rgba(0, 0,0, 0.5);/* color de fondo oscuro para simular una sombra */
    left: 50%; /*centra la sombra horizontalmente */
    border-radius: 50%; /* bordes redondeados para la sombra */
    filter: blur(4px);/* aplica un desenfoque para hacer la sombra más suave */
    transform: translate(-50%, 50%); /*Ajusta la posición para centrar la sombra */
}

ul li .title::before{
    bottom: calc(100% + 0.125rem);/*coloca la sombra debajo del título */
}

ul li .descripcion::before{
    z-index: -1;/*Coloca la sombra detrás del contenido */
    bottom: 0.25rem;/*coloca la sombra justo6 */
}

/**Media query para pantallas anchas (40rem o más) */
@media (min-width: 40rem){
    ul{
        grid-template-columns: 1fr var(--line-w) 1fr; /*Ajusta la cuadrícula para tener tres columnas */
    }
    ul::before{
        grid-column: 2;/**Mueve la línea vertical a la segunda columna de la cuadrícula */
    }
    ul li:nth-child(odd){
        grid-column: 1; /**coloca los ítems impares en la primera columna */
    }
    ul li:nth-child(even){
        grid-column: 3;/**Coloca los ítems pares en la tercera columna */
    }

    /**Ajuste para que el segundo item abarque dos filas */
    ul li:nth-child(2){
        grid-row: 2/4;/**El segundo item ocupará desde la segunda hasta la cuarta fila */
    }
    /**Ajustes específicos para los items impares */
    ul li:nth-child(odd) .fecha::before{
        clip-path: polygon(0 0, 100% 0, 100% 100%);/**Invierte el triángulo en los items impares */
        left: 0;/**Alinea el triángulo a la izquierda */
    }

    ul li:nth-child(odd) .fecha::after {
        transform: translate(-50%, -50%);/**Ajusta la posición del círculo en los items impares */
        left: calc(100% + var(--col-gap) + var(--line-w) / 2);/**coloca el círculo a la derecha de la línea */
    }

    ul li:nth-child(odd) .fecha {
        border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0;/**Ajusta los bordes redondeados para los ítems impares */
    }

}

/**Estilo para los créditos */
.credits{
    margin-top: 1rem; /**Espaciado superior para los créditos */
    text-align: right; /**alinea el texto de los créditos a la derecha */
}

.credits a{
    color: var(--color); /**Aplica el color de texto definido en la variable */
}


</style>
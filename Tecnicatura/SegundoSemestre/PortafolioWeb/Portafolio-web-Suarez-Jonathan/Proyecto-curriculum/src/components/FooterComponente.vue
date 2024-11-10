<template>
  <footer class="footer">
    <h1 class="contact">Contactame</h1>
    <ul class="menu">
      <li><a class="menu__link" href="#"></a></li>
      <li><a class="menu__link" href="#educacion">Educación</a></li>
      <li><a class="menu__link" href="#proyectos">Proyectos</a></li>
      <li><a class="menu__link" href="#experiencia">Experiencia</a></li>
      <li><a class="float-wa" href="https://wa.me/5492604306093?text=Hola" target="_blank">
        <img src="../components/icons/icons-whatsapp.svg" alt="WhatsApp" class="whatsapp-icon">
      </a></li>
    </ul>
    <p>&copy;2024 Suarez Jonathan | All Rights Reserved</p>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponente'
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800;900&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  color: var(--color);
  background: white;
  justify-content: flex-end;
  align-items: flex-end;
  min-height: 100vh;
}

.footer {
  position: relative;
  width: 100%;
  background-color: #F3F4F6;  /* Gris muy suave */
  padding: 20px 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border-top: 5px solid #015F6B; /* Agregado Paper Petrol como color para el borde */
}

.social-icon, .menu {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px 0;
  flex-wrap: wrap;
}

.social-icon__item, .menu__item {
  list-style: none;
}

.social-icon__link {
  font-size: 2rem;
  color: #333; /* Color más suave */
  margin: 0 10px;
  display: inline-block;
  transition: 0.3s;
}

.social-icon__link:hover {
  transform: translateY(-5px);
  color: #015F6B; /* Paper Petrol como color para hover */
}

.menu__link {
  font-size: 1.2rem;
  color: #333; /* Color más suave */
  margin: 0 10px;
  display: inline-block;
  transition: 0.3s;
  text-decoration: none;
  opacity: 0.85;
  font-weight: 300;
}

.menu__link:hover {
  opacity: 1;
  color: #D46A7E; /* Revitalized Pinkish como color de hover */
}

.footer p {
  color: #555; /* Color más suave para el texto */
  margin: 15px 0 10px 0;
  font-size: 1rem;
  font-weight: 300;
}

.contact {
  color: #141414; /* Gutsiest Sand Yellow como color principal */
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.float-wa {
  position: fixed;
  width: 50px;
  height: 50px;
  bottom: 30px;
  right: 30px;
  color: #FFF;
  border-radius: 50px;
  text-align: center;
  font-size: 30px;
  z-index: 100;
}

.whatsapp-icon {
  width: 100%;
  height: 100%;
}
</style>

// Cambiar entre pestañas
function cambiarPestana(tipo) {
    const pestanas = document.querySelectorAll('.pestana');
    const formularios = document.querySelectorAll('.formulario');

    pestanas.forEach(p => p.classList.remove('activa'));
    formularios.forEach(f => f.classList.remove('activo'));

    if (tipo === 'login') {
        pestanas[0].classList.add('activa');
        document.getElementById('formularioLogin').classList.add('activo');
    } else {
        pestanas[1].classList.add('activa');
        document.getElementById('formularioRegistro').classList.add('activo');
    }
}

// Alternar visibilidad de contraseña
function alternarPassword(idCampo, icono) {
    const campo = document.getElementById(idCampo);
    const esPassword = campo.type === 'password';

    campo.type = esPassword ? 'text' : 'password';

    // Cambiar imagen según estado
    icono.src = esPassword ? 'img/icon-menu/ojo-abierto.png' : 'static/img/icon-menu/ojo-esconder.png';
}




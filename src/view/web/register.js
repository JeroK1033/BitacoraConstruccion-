async function registrarse() {
    const correo = document.getElementById("correo").value.trim();
    const contrasena = document.getElementById("contrasena").value;

    if (!correo || !contrasena) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    const response = await fetch('/registrar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({correo, contrasena})
    });

    const resultado = await response.json();
    if (resultado.exito) {
        alert("Registro exitoso.");
        window.location.href = "index.html";
    } else {
        alert("El correo ya se encuentra registrado.");
    }
}

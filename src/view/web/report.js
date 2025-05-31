function generarPDF() {
    const fechaInicio = document.getElementById("fechaInicio").value;
    const fechaFin = document.getElementById("fechaFin").value;
    const rango = document.getElementById("rangoFechas");

    if (!fechaInicio || !fechaFin) {
        alert("Por favor, ingrese ambas fechas para generar el reporte.");
        return;
    }

    // Actualiza el contenido del reporte
    rango.textContent = `Desde: ${fechaInicio} - Hasta: ${fechaFin}`;

    // Aquí podrías reemplazar el contenido por actividades filtradas si tienes datos reales
    // Simulación de datos:
    const lista = document.getElementById("listaActividadesPDF");
    lista.innerHTML = ""; // Limpia la lista
    lista.innerHTML += `<li>Actividad ejemplo filtrada entre las fechas seleccionadas</li>`;

    const contenido = document.getElementById("contenidoReporte");
    contenido.style.display = "block";

    html2pdf().from(contenido).save("reporte_actividades.pdf");

    // Opcional: ocultar contenido nuevamente
    setTimeout(() => {
        contenido.style.display = "none";
    }, 1000);
}

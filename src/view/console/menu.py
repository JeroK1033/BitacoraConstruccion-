from src.controller.app_controlador import AppControlador
import os

class Menu:
    """
        Clase que representa el menú de la bitácora
    """

    def __init__(self, controlador: AppControlador):
        self.__controlador: AppControlador = controlador

    def limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def encabezado(self, titulo):
        print("=" * 60)
        print(f"{titulo.center(60)}")
        print("=" * 60)

    def menu_principal(self):
        while True:
            self.limpiar_consola()
            self.encabezado("\U0001F4D2 BITÁCORA DE CONSTRUCCIÓN \U0001F477‍♂️")
            print("1. \U0001F3D7️  Iniciar sesión")
            print("2. \U0001F9F1  Registrarse")
            print("3. ❌  Salir")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-3): ").strip()

            if opcion == "1":
                self.menu_login()
            elif opcion == "2":
                self.menu_registro()
            elif opcion == "3":
                print("\n\U0001F44B Gracias por utilizar la Bitácora de Construcción.")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")

    def menu_login(self):
        while True:
            self.limpiar_consola()
            self.encabezado("\U0001F510 INICIAR SESIÓN")
            print("1. ✔️  Acceder")
            print("2. \U0001F519  Volver")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-2): ").strip()

            if opcion == "1":
                email = input("📧 Correo electrónico: ").strip()
                contraseña = input("🔒 Contraseña: ").strip()
                if self.__controlador.iniciar_sesion(email, contraseña):
                    print("\n✅ Inicio de sesión exitoso.")
                    input("Presione Enter para continuar...")
                    self.menu_actividad()
                else:
                    print("❌ Credenciales incorrectas.")
                    input("Presione Enter para intentar nuevamente...")
            elif opcion == "2":
                break
            else:
                print("⚠️ Opción no válida.")
                input("Presione Enter para continuar...")

    def menu_registro(self):
        while True:
            self.limpiar_consola()
            self.encabezado("📝 REGISTRAR NUEVO USUARIO")
            print("1. ➕  Registrar")
            print("2. 🔙  Volver")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-2): ").strip()

            if opcion == "1":
                nombre = input("👤 Nombre completo: ").strip()
                email = input("📧 Correo electrónico nuevo: ").strip()
                contraseña = input("🔒 Nueva contraseña: ").strip()
                if self.__controlador.registrar_usuario(nombre, email, contraseña):
                    print("✅ Usuario registrado exitosamente.")
                    input("Presione Enter para continuar...")
                    break
                else:
                    print("❌ El correo ya está registrado.")
                    input("Presione Enter para intentar nuevamente...")
            elif opcion == "2":
                break
            else:
                print("⚠️ Opción no válida.")
                input("Presione Enter para continuar...")

    def menu_actividad(self):
        while True:
            self.limpiar_consola()
            self.encabezado("📋 MENÚ DE ACTIVIDADES")
            print("1. 📝 Registrar nueva actividad")
            print("2. 🔍 Consultar actividades")
            print("3. 📄 Generar reporte PDF")
            print("4. 🔐 Actualizar contraseña")
            print("5. 🚪 Cerrar sesión")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-5): ").strip()

            if opcion == "1":
                self.registrar_actividad()
            elif opcion == "2":
                self.consultar_actividades()
            elif opcion == "3":
                self.generar_reporte()
            elif opcion == "4":
                self.actualizar_contraseña()
            elif opcion == "5":
                break
            else:
                print("⚠️ Opción no válida.")
                input("Presione Enter para continuar...")

    def registrar_actividad(self):
        self.limpiar_consola()
        self.encabezado("📝 REGISTRAR ACTIVIDAD")
        descripcion = input("Descripción: ").strip()
        clima = input("Condiciones climáticas: ").strip()
        if self.__controlador.registrar_actividad(descripcion, clima):
            print("✅ Actividad registrada con éxito.")
        else:
            print("❌ Error al registrar actividad.")
        input("Presione Enter para continuar...")

    def consultar_actividades(self):
        self.limpiar_consola()
        self.encabezado("🔍 CONSULTAR ACTIVIDADES")
        actividades = self.__controlador.consultar_actividades()
        if not actividades:
            print("❌ No hay actividades registradas.")
        else:
            for act in actividades:
                print(f"- {act}")
        input("Presione Enter para continuar...")

    def generar_reporte(self):
        self.limpiar_consola()
        self.encabezado("📄 GENERAR REPORTE PDF")
        if self.__controlador.generar_reporte_pdf():
            print("✅ Reporte generado correctamente.")
        else:
            print("❌ Error al generar el reporte.")
        input("Presione Enter para continuar...")

    def actualizar_contraseña(self):
        self.limpiar_consola()
        self.encabezado("🔐 ACTUALIZAR CONTRASEÑA")
        email = input("📧 Correo electrónico: ").strip()
        nueva = input("🔑 Nueva contraseña: ").strip()
        if self.__controlador.actualizar_contraseña(email, nueva):
            print("✅ Contraseña actualizada con éxito.")
        else:
            print("❌ Error al actualizar la contraseña.")
        input("Presione Enter para continuar...")

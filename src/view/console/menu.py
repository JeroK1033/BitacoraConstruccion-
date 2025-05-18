from src.controller.app_controlador import AppControlador
import os

class Menu:
    """
        Clase que representa el menu de la bitacora
    
    """
    
    def __init__(self, controlador: AppControlador):
        self.__controlador: AppControlador = controlador
    

    @staticmethod
    def limpiar_consola():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def encabezado(titulo):
        print("=" * 60)
        print(f"{titulo.center(60)}")
        print("=" * 60)

    @staticmethod
    def menu_principal():
        while True:
            Menu.limpiar_consola()
            Menu.encabezado("📒 BITÁCORA DE CONSTRUCCIÓN 👷‍♂️")
            print("1. 🏗️  Iniciar sesión")
            print("2. 🧱  Registrarse")
            print("3. ❌  Salir")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-3): ").strip()

            if opcion == "1":
                Menu.menu_login()
            elif opcion == "2":
                Menu.menu_registro()
            elif opcion == "3":
                print("\n👋 Gracias por utilizar la Bitácora de Construcción.")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                
    @staticmethod
    def menu_login(self):
        while True:
            Menu.limpiar_consola()
            Menu.encabezado("🔐 INICIAR SESIÓN")
            print("1. ✔️  Acceder")
            print("2. 🔙  Volver")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-2): ").strip()

            if opcion == "1":
                email = input("📧 Correo electrónico: ").strip()
                contraseña = input("🔒 Contraseña: ").strip()
                print(f"\n🔍 Verificando credenciales para {email}...")
                self.controlador.iniciar_sesion(email, contraseña)
                input("✅ Acceso simulado. Presione Enter para continuar...")
            elif opcion == "2":
                break
            else:
                print("⚠️ Opción no válida.")
                input("Presione Enter para continuar...")
    @staticmethod
    def menu_registro():
        while True:
            Menu.limpiar_consola()
            Menu.encabezado("📝 REGISTRAR NUEVO USUARIO")
            print("1. ➕  Registrar")
            print("2. 🔙  Volver")
            print("-" * 60)

            opcion = input("Seleccione una opción (1-2): ").strip()

            if opcion == "1":
                nombre = input("👤 Nombre completo: ").strip()
                email = input("📧 Correo electrónico nuevo: ").strip()
                contraseña = input("🔒 Nueva contraseña: ").strip()
                print(f"\n🛠️ Registrando supervisor: {email}")
                # Aquí se llamaría a la lógica de registro real
                input("✅ Registro simulado. Presione Enter para continuar...")
            elif opcion == "2":
                break
            else:
                print("⚠️ Opción no válida.")
                input("Presione Enter para continuar...")

from src.view.gui.gui import BitacoraApp
from src.controller.app_controlador import AppControlador

if __name__ == "__main__":
    app_controlador: AppControlador = AppControlador()
    BitacoraApp(controlador=app_controlador).run()
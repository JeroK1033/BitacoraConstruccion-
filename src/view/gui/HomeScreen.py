from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/HomeScreen.kv")

class HomeScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
    
    def actividad(self):
        """
        Cambia a la pantalla de registro de actividad.
        """
        self.manager.current = "ActivityScreen"
    
    def consulta(self):
        """
        Cambia a la pantalla de consulta de actividades.
        """
        self.manager.current = "ListScreen"
    
    def reporte(self):
        """
        Cambia a la pantalla de reporte de actividades.
        """
        self.manager.current = "ReportScreen"
    
    def update(self):
        """
        Cambia a la pantalla de actualización de actividades.
        """
        self.manager.current = "UpdatePScreen"
    
    def CerrarSesion(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador
from datetime import datetime

Builder.load_file("src/view/gui/kv/ActivityScreen.kv")

class ActivityScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
    
    def nueva_actividad(self):
        if self.controlador.registrar_actividad(self.ids.fecha_hora_input.text, self.ids.supervisor_input.text, self.ids.descripcion_input.text, self.ids.anexo_input.text, self.ids.anexo_input.text):
            self.manager.current = "HomeScreen"
        else:
            self.ids.error_label.text = "Error al registrar la actividad. Por favor, inténtalo de nuevo."
        
    
    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "HomeScreen"
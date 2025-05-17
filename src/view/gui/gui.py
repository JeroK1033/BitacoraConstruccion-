from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.controller.app_controlador import AppControlador
from src.view.gui.MainScreen import MainScreen
from src.view.gui.LoginScreen import LoginScreen
from src.view.gui.RegisterScreen import RegisterScreen
from src.view.gui.ActivityScreen import ActivityScreen
from src.view.gui.HomeScreen import HomeScreen
from src.view.gui.ListScreen import ListScreen
from src.view.gui.ReportScreen import ReportScreen
from src.view.gui.UpdatePScreen import UpdatePScreen

class BitacoraApp(App):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
        
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="MainScreen", controlador=self.controlador))
        screen_manager.add_widget(LoginScreen(name="LoginScreen", controlador=self.controlador))
        screen_manager.add_widget(RegisterScreen(name="RegisterScreen", controlador=self.controlador))
        screen_manager.add_widget(ActivityScreen(name="ActivityScreen", controlador=self.controlador))
        screen_manager.add_widget(HomeScreen(name="HomeScreen", controlador=self.controlador))
        screen_manager.add_widget(ListScreen(name="ListScreen", controlador=self.controlador))
        screen_manager.add_widget(ReportScreen(name="ReportScreen", controlador=self.controlador))
        screen_manager.add_widget(UpdatePScreen(name="UpdatePScreen", controlador=self.controlador))
        return screen_manager
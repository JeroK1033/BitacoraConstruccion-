import pytest
from src.model.bitacora import Bitacora
from src.model.errorres_usuario import ErrorEmailNo, ErrorEmailYa, ErrorContraseñaCorta

class DiccionarioMock:
    def registrar_supervisor(self, nombre, email, contraseña):
        return True

    def verificar_supervisor(self, email, contraseña):
        return True

bitacora = Bitacora(DiccionarioMock())


def test_registro_exitoso():
    assert bitacora.registrar_supervisor("Juan Perez", "juan.perez@example.com", "JuanP@123")

def test_registro_con_email_valido():
    assert bitacora.registrar_supervisor("Maria Lopez", "maria.lopez@example.com", "Maria2024#") 

def test_registro_con_nombre_apellido_validos():
    assert bitacora.registrar_supervisor("Carlos Rivera", "carlos.r@example.com", "Carlos2024#")

def test_registro_contraseña_larga():
    assert bitacora.registrar_supervisor("Luis Gómez", "luis.gomez@example.com", "32CaracteresLargos1234#@")

def test_registro_caracteres_especiales_nombre():
    assert bitacora.registrar_supervisor("Ana-María López", "ana.lopez@example.com", "AnaFuerte2024!")

def test_registro_sin_email():
    with pytest.raises(ErrorEmailNo):
        bitacora.registrar_supervisor("Carlos Rivera", None, "Carlos2024")is True

def test_registro_contraseña_corta():
    with pytest.raises(ErrorContraseñaCorta):
        bitacora.registrar_supervisor("Luis Gómez", "luis.gomez@example.com", "123") is True

def test_registro_email_ya_registrado():
    bitacora.registrar_supervisor("Juan Perez", "juan.perez@example.com", "JuanP@123")
    with pytest.raises(ErrorEmailYa):
        bitacora.registrar_supervisor("Juan Perez", "juan.perez@example.com", "JuanP@123")





def test_inicio_sesion_exitoso():
    assert bitacora.verificar_credenciales("juan.perez@example.com", "JuanP@123")

def test_inicio_sesion_recordar_activado():
    assert bitacora.verificar_credenciales("MARIA.LOPEZ@EXAMPLE.COM", "Maria2024#")

def test_inicio_sesion_varios_intentos():
    assert bitacora.verificar_credenciales("carlos.r@gmail.com", "Carlos2024#")


def test_inicio_sesion_contraseña_larga():
    assert bitacora.verificar_credenciales("luis.gomez@gmail.com", "32CaracteresLargos1234#@")
    

def test_inicio_sesion_solo_letras_minusculas():
    assert bitacora.verificar_credenciales("maria.lopez@gmail.com", "mariaclave")
    

def test_inicio_sesion_solo_numeros():
    assert bitacora.verificar_credenciales("carlos.r@gmail.com", "12345678")
    
'''

def test_inicio_sesion_contraseña_incorrecta():
    usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "Incorrecta123")
    with pytest.raises(ErrorContraseñaIncorrecta):
        usuario.iniciar_sesion()

def test_inicio_sesion_email_no_registrado():
    usuario = Supervisor("Usuario Nuevo", "usuario.nuevo@gmail.com", "NuevaClave@456")
    with pytest.raises(ErrorEmailNo):
        usuario.iniciar_sesion()

def test_inicio_sesion_formato_email_invalido():
    usuario = Supervisor("Usuario Incorrecto", "incorrecto.com", "Prueba2024#")
    with pytest.raises(ErrorEmailNo):
        usuario.iniciar_sesion()
'''
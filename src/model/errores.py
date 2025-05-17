class ErrorCamposVacios(Exception):
    """
    Excepción personalizada que se lanza cuando el usuario todavia tiene campos vacios en los formularios que puedan haber en la bitacora.
    
    """
    
    def __init__(self):
        """
        Inicializa la excepción con un mensaje indicando que hay campos que no estan completos.
        
        """
        super().__init__(f"Rellene todos los campos")       
import re
import pandas as pd 
import json
from datetime import datetime


def validate_phone(num: str ) -> bool:
    """
    Esta función  se agura de que el  número de teléfono (movil) cumpla con las siguientes condiciones:
    1. Debe tener 10 dígitos.
    2. Debe comenzar con el dígito '3'
    3.  Debe seguir el patrón 3MM-XXX-XXXX. Donde 
    el prefijo 3MM debe pertenecer a un operador móvil válido en Colombia.
    Fuente : https://en.wikipedia.org/wiki/Telephone_numbers_in_Colombia 
    Args:
        num (int): Número de teléfono a validar.
    Returns:
        bool: True si el número es válido, False en caso contrario.
    """
    # Diccionario de operadores móviles en Colombia con sus respectivos prefijos.
    operadores = {
        'Tigo': [300, 301, 302, 304, 305, 324],
        'Flash Móvil': [304],
        'ETB': [304, 305],
        'Móvil Éxito': [305],
        'Claro': [310, 311, 312, 313, 314, 320, 321, 322, 323],
        'Movistar': [315, 316, 317, 318],
        'Virgin Mobile': [319],
        'Suma Móvil': [333],
        'Avantel': [350, 351],
        'WOM': [302, 323]
    }
        
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(num):
        return False
    
    num_str = str(num).strip()

    #Validamos las condiciones 1 y 2. 
    if len(num_str) != 10 or not num_str.startswith('3') or not num_str.isdigit():
        return False
   
    # Validamos la condición 3.
    
    #Extraemos el prefijo
    prefijo = int(num_str[:3])

    # Comprueba si el prefijo pertenece a algún operador
    for prefijos in operadores.values():
        if prefijo in prefijos:
            return True
    #Si elprefijo no pertenece a ningún operador, retornamos False.
    
    return False

def validate_ID(doc : str) -> bool: 
    """
    Esta función valida que el número de documento cumpla con las siguientes condiciones:
    1. Debe contener 10 digitos
    2. Empieza con 1. (rango de  mil millones 1000000000 )
    Args: 
        doc (int): Número de documento a validar.
    Returns:
        bool: True si el número es válido, False en caso contrario.
        
     Fuente : https://www.registraduria.gov.co/Ahora-la-cedula-es-de-10-digitos.html
    """
    
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(doc) :   
        return False
    
    doc_str = str(doc).strip()

    # Validamos las condiciones 1 y 2.
    return doc_str.isdigit() and  len(doc_str) == 10 and  doc_str.startswith('1')

def Validate_Document_type(tipo:str, fecha_nacimiento: str) -> bool :
    """ 
    Valida que el tipo de documento sea consistente con la edad de la persona.
    Requisitos:
    - Si la persona es mayor de 18 años, el tipo de documento debe ser 'CC' (Cédula de Ciudadanía).
    - Si la persona es menor o igual a 18 años, el tipo de documento debe ser 'TI' (Tarjeta de Identidad).
    - El tipo de documento debe ser 'CC' o 'TI'.
    -Fecha y tipo de documento no pueden ser nulos o vacíos.   
    Args:
        tipo (str): Tipo de documento ('CC' o 'TI').
        fecha_nacimiento (str or datetime): Fecha de nacimiento de la persona.  
    Returns:
        bool: True si el tipo de documento es consistente con la edad, False en caso contrario
    """
    #Primero, verificamos que la fecha de nacimiento y el tipo de documento no estén vacío o sean nulo.
    if pd.isna(tipo) or pd.isna(fecha_nacimiento):
        return False
    
    # Convertimos a mayúsculas y eliminamos espacios en blanco
    tipo = str(tipo).strip().upper()
    if tipo not in ['CC', 'TI']:
        return False
    
    try:
        # Convertir la fecha de nacimiento a objeto datetime
        fecha = pd.to_datetime(str(fecha_nacimiento).strip(), errors='raise')
        if pd.isna(fecha):
            return False

        hoy = pd.Timestamp(datetime.now())
        if fecha > hoy:
            return False
        # Calcular la edad
        edad = (hoy - fecha).days // 365
        # Validar el tipo de documento según la edad
        if edad >= 18 and tipo == 'CC':
            return True
        if edad < 18 and tipo == 'TI':
            return True
        return False
    except Exception:
        return False

def validate_Email(email: str) -> bool:
    """
    Esta función valida que el correo electrónico cumpla con el formato estándar.
    Args:
        email (str): Correo electrónico a validar.
    Returns:
        bool: True si el correo es válido, False en caso contrario. 
    """
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(email):
        return False
    
    #patron de busqueda de la leccion 7 : regular expressions
    patron = (r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
              r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
              r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    
    
    return re.match(patron,  str(email)) is not None

def validate_Gender(gender: str) -> bool:
    """
    Válida si el genero es uno de los valores aceptados.
    - Male 
    - Female
    - X   
    
    Args:
        gender(str):  género a validar.
    Returns:
        bool: True si el género es válido, False en caso contrario.
    """
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(gender):
        return False
    # Convertimos a mayúsculas y eliminamos espacios en blanco
    gender_ = str(gender).strip().upper()
    
    return gender_ in [ 'M', 'F','X']

def validate_marital_status(marital_status: str) -> bool:
    """
    Comprueba si el valor del estado civil es uno de los siguientes:
    -soltero (single)
    -casado (married)
    -divorciado (divorced)
    -viudo (widowed)
    -separado(separated)
    Args:
        marital_status (str): Estado civil a validar.
    Returns:
        bool: True si el estado civil es válido, False en caso contrario.
    """
    
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(marital_status):
        return False
    
    # Convertimos a minúsculas y eliminamos espacios en blanco
    status = str(marital_status).strip().lower()
    options = ['soltero', 'casado', 'divorciado', 'viudo', 'separado']
    return  status in options

def validate_Birthday(fecha : str)-> bool:
    """
    Valida si la fecha de nacimiento es válida.
    
    Requisitos:
    - No puede ser nula o vacía.
    - Debe ser una fecha válida.
    - No puede ser una fecha futura.
    
    Args:
        fecha (str or datetime): Fecha de nacimiento a validar.
    
    Returns:
        bool: True si la fecha es válida, False en caso contrario.
    """
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(fecha):
        return False
    
    try:
        # 2. Convertir a objeto datetime con varios formatos 
        fecha_dt = pd.to_datetime(str(fecha).strip(), errors='raise').date()
        
        # 3. Comparar con la fecha actual
        hoy = datetime.today().date()
        if fecha_dt > hoy:
            return False
        
        return True
    except Exception:
        # Si no se puede convertir en fecha válida
        return False

def validate_Names(names : str) -> bool :
    """
    valida que el nombre o apellido cumpla con las siguientes condiciones:
    - No puede ser vacío o nulo.
    - Solo letras (incluye acentos, ñ, ü).
    - Longitud mínima: 3, máxima: 12 caracteres.
    Args:
        names (str): Nombre o apellido a validar.
    Returns:
        bool: True si el nombre o apellido es válido, False en caso contrario.
    """
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(names):
        return False
    
    #Solo letras (incluye acentos, ñ, ü).
    #Longitud mínima: 3, máxima: 12 caracteres.
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]{3,12}$"
    
    return re.fullmatch(patron, str(names).strip()) is not None


# Cargar archivo de referencia de departamentos y ciudades desde colombia.json
with open('colombia.json', encoding='utf-8') as f:
    colombia_data = json.load(f)
departamento_ciudad_dict = {}
for item in colombia_data:
    dept = item['departamento'].strip().lower()
    ciudades = set(city.strip().lower() for city in item['ciudades'])
    departamento_ciudad_dict[dept] = ciudades

def validate_Location(departamento :str, ciudad:str) -> bool:
    """
    Valida si la ciudad pertenece al departamento en Colombia.
    Args:
        departamento (str): Nombre del departamento.
        ciudad (str): Nombre de la ciudad.  
    Returns:
        bool: True si la ciudad pertenece al departamento, False en caso contrario.
    """
    
    #Primero, verificamos que el campo no esté vacío o sea nulo.
    if pd.isna(departamento) or pd.isna(ciudad):
        return False
    dept = str(departamento).strip().lower()
    city = str(ciudad).strip().lower()
    if dept in departamento_ciudad_dict:
        return city in departamento_ciudad_dict[dept]
    return False


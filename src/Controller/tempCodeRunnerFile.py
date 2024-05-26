import sys
import os

# Obtén la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Agrega la ruta del directorio Model al sys.path
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Model.MonthlyPaymentLogic import *
import src.Model.MonthlyPaymentLogic as mp

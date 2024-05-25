import sys
import os

# Obtén la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Agrega la ruta del directorio Model al sys.path
model_dir = os.path.join(current_dir, "..", "Model")
sys.path.append(model_dir)
from ..Model.MonthlyPaymentLogic import *
import Model.MonthlyPaymentLogic as mp
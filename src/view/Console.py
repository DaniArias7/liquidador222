import sys


# Agregar el directorio 'src' al path para permitir importaciones relativas
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")

from src.Model.MonthlyPaymentLogic import *
import src.Model.MonthlyPaymentLogic as mp

print(f"""
El propósito del programa es calcular el salario mensual de un empleado 
considerando diferentes variables como el salario básico, días laborados, 
días de licencia, y días de incapacidad, entre otros.

Para llevar a cabo este cálculo, se utilizan varias constantes:
- El salario mínimo legal en Colombia es de ${mp.MINIMUM_WAGE}.
- La Unidad de Valor Tributario (UVT) tiene un valor de ${mp.UVT}.
- Coeficientes para calcular el pago de horas extras en diferentes situaciones:
  - Horas extras diurnas: {mp.EXTRA_HOUR_DAYSHIFT}
  - Horas extras nocturnas: {mp.EXTRA_HOUR_NIGHTSHIFT}
  - Horas extras diurnas en días festivos: {mp.EXTRA_HOUR_DAYSHIFT_HOLIDAYS}
  - Horas extras nocturnas en días festivos: {mp.EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS}
- El número de días y horas en un mes se establece en {mp.MONTH_DAYS} días y {mp.MONTH_HOURS} horas.
- Porcentajes utilizados para calcular contribuciones de seguro de salud, aportes a pensiones, fondos de retiro y licencias por enfermedad:
  - Porcentaje de seguro de salud y aportes a pensiones: {mp.PERCENTAGE_HEALTH_INSURANCE * 100}%
    - Porcentaje de fondo de retiro: {mp.PERCENTAGE_RETIREMENT_FUND * 100}%
- Una lista que define los porcentajes de retención salarial en función del salario en UVT.
""")

def user_data_input():
    """
    Requests the user to input various parameters related to an employee's settlement.
    
    Parameters:
        None

    Returns:
        SettlementParameters: An object encapsulating the settlement parameters inputted by the user.
    """
    basic_salary = float(input("Ingrese el salario básico del empleado: "))
    workdays = int(input("Ingrese el número de días laborados en el mes: "))
    sick_leave = int(input("Ingrese el número de días de licencia por enfermedad: "))
    transportation_aid = float(input("Ingrese el valor del auxilio de transporte: "))
    dayshift_extra_hours = int(input("Ingrese el número de horas extras diurnas: "))
    nightshift_extra_hours = int(input("Ingrese el número de horas extras nocturnas: "))
    dayshift_extra_hours_holidays = int(input("Ingrese el número de horas extras diurnas en días festivos: "))
    nightshift_extra_hours_holidays = int(input("Ingrese el número de horas extras nocturnas en días festivos: "))
    leave_days = int(input("Ingrese el número de días de licencia (vacaciones u otros): "))
    percentage_health_insurance = float(input("Ingrese el porcentaje de seguro de salud: ")) / 100
    percentage_retirement_insurance = float(input("Ingrese el porcentaje de aporte a pensiones: ")) / 100
    percentage_retirement_fund = float(input("Ingrese el porcentaje de fondo de retiro: ")) / 100
    
    return mp.SettlementParameters(basic_salary, workdays, sick_leave, transportation_aid, dayshift_extra_hours,
                                   nightshift_extra_hours, dayshift_extra_hours_holidays,
                                   nightshift_extra_hours_holidays,
                                   leave_days, percentage_health_insurance,
                                   percentage_retirement_insurance, percentage_retirement_fund)

def calculate_settlement():
    """
    Calculates the settlement value based on the user input data.

    Returns:
        float: The calculated settlement value.
    """
    datos_ingresados_por_usuario = user_data_input()
    print("El valor que se le deberá pagar al trabajador es:", mp.calculate_settlement(datos_ingresados_por_usuario))

def program_start():
    """
    Initiates the program to calculate the settlement and prompts the user if they want to calculate another worker's salary.

    Returns:
        None
    """
    calculate_settlement()
    while True:
        valor = input("¿Quiere calcular el salario de otro trabajador? (escriba 'si' o 'no'): ").lower()
        if valor == "si":
            calculate_settlement()
        elif valor == "no":
            print("Gracias por utilizar nuestro servicio.")
            break
        else:
            print("Entrada inválida. Por favor, escriba 'si' o 'no'.")

try :
    print("¡Hola! Comencemos a calcular el salario de los trabajadores.")
    program_start()

except Exception as the_exception:
    print(f"Ha ocurrido un error; no se puede continuar; el error que hay es el siguiente: {the_exception}")


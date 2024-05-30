from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from src.Model.TablesEmployer import Employerinput, Employeroutput as Temployer,Employeroutput
import src.Model.TablesEmployer as Temployer
import src.Model.MonthlyPaymentLogic as mp
from src.Model.MonthlyPaymentLogic import calculate_settlement, InvalidRetirementFundPercentageError, SettlementParameters
import pandas as pd

app = Flask(__name__)
blueprint = Blueprint("vista_usuarios", __name__, template_folder="templates")


@blueprint.route("/")
def home():
    return render_template("inicio.html")

@blueprint.route("/new-user")
def nuevo():
    return render_template("crear_usuario.html")

@blueprint.route("/crear_usuario")
def crear_usuario():
    nuevo_empleado = Employerinput(
        name=request.args["nombre"], 
        id=request.args["cedula"], 
        basic_salary=float(request.args["salario"]), 
        monthly_worked_days=int(request.args["Días_Trabajados"]), 
        days_leave=int(request.args["Días_Libres"]), 
        transportation_allowance=float(request.args["Auxilio_Trasporte"]),
        daytime_overtime_hours=float(request.args["Horas_diurnas_extra"]), 
        nighttime_overtime_hours=float(request.args["Horas_nocturnas_extra"]), 
        daytime_holiday_overtime_hours=float(request.args["Horas_diurnas_extra_festivo"]),
        nighttime_holiday_overtime_hours=float(request.args["Horas_nocturnas_extra_festivo"]), 
        sick_leave_days=int(request.args["Días_enfermedad"]), 
        health_contribution_percentage=float(request.args["Porcentaje_seguro_salud"]),
        pension_contribution_percentage=float(request.args["Porcentaje_retiro"]), 
        solidarity_pension_fund_contribution_percentage=float(request.args["percentage_retirement_fund"])
    )

    WorkersIncomeData.Insert(nuevo_empleado)
    return render_template("resultado.html", user=nuevo_empleado, mensaje="Usuario insertado exitosamente!")

@blueprint.route("/buscar-usuario")
def buscar_usuario():
    return render_template("buscar_usuario.html")

@blueprint.route("/buscar_usuario_result", methods=["GET"])
def buscar_usuario_result():
    nombre = request.args["nombre"]
    cedula = request.args["cedula"]
    trabajador = WorkersIncomeData.QueryWorker(nombre, cedula)
    if trabajador:
        return render_template("resultado.html", user=trabajador, mensaje="Trabajador encontrado:")
    else:
        return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")

@blueprint.route("/actualizar-usuario")
def modificar_usuario():
    return render_template("actualizar_usuario.html")

@blueprint.route("/actualizar_usuario_result", methods=["POST"])
def actualizar_usuario_result():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]
    columna = request.form["columna"]
    valor = request.form["valor"]

    try:
        if columna in ["basic_salary", "transportation_allowance", "daytime_overtime_hours", "nighttime_overtime_hours",
                       "daytime_holiday_overtime_hours", "nighttime_holiday_overtime_hours", "health_contribution_percentage",
                       "pension_contribution_percentage", "solidarity_pension_fund_contribution_percentage"]:
            valor = float(valor)
        else:
            valor = int(valor)
        
        worker = WorkersIncomeData.QueryWorker(nombre, cedula)
        if worker:
            WorkersIncomeData.Update(nombre, cedula, KEYUPDATE=columna, VALUEUPDATE=valor)
            mensaje = "Información del trabajador actualizada exitosamente!"
        else:
            mensaje = "No se encontró ningún trabajador con el nombre y la cédula proporcionados."
        return render_template("resultado.html", mensaje=mensaje)
    except Temployer.not_exist as e:
        mensaje = f"Error al actualizar: {str(e)}"
        return render_template("resultado.html", mensaje=mensaje)
    except Exception as e:
        mensaje = f"Error inesperado: {str(e)}"
        return render_template("resultado.html", mensaje=mensaje)

@blueprint.route("/eliminar-usuario")
def eliminar_usuario():
    return render_template("eliminar_usuario.html")

@blueprint.route("/eliminar_usuario_result", methods=["POST"])
def eliminar_usuario_result():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]

    trabajador = WorkersIncomeData.QueryWorker(nombre, cedula)
    if trabajador:
        WorkersIncomeData.DeleteWorker(nombre, cedula)
        return render_template("resultado.html", mensaje="Trabajador eliminado exitosamente!")
    else:
        return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")
    
@blueprint.route("/calcular-liquidacion", methods=["GET"])
def calcular_liquidacion():
    return render_template("calcular_liquidacion.html")

@blueprint.route("/mostrar_resultado_liquidacion", methods=["POST"])
def mostrar_resultado_liquidacion():
    nombre = request.form["nombre"]
    cedula = request.form["cedula"]
    
    try:
        trabajador = WorkersIncomeData.QueryWorker(nombre, cedula)
        if trabajador:
            # Lógica de cálculo de liquidación basada en los datos del trabajador
            settlement_params = SettlementParameters(
                basic_salary=trabajador.basic_salary,
                workdays=trabajador.monthly_worked_days,
                sick_leave=trabajador.sick_leave_days,
                transportation_aid=trabajador.transportation_allowance,
                dayshift_extra_hours=trabajador.daytime_overtime_hours,
                nightshift_extra_hours=trabajador.nighttime_overtime_hours,
                dayshift_extra_hours_holidays=trabajador.daytime_holiday_overtime_hours,
                nightshift_extra_hours_holidays=trabajador.nighttime_holiday_overtime_hours,
                leave_days=trabajador.days_leave,
                percentage_health_insurance=trabajador.health_contribution_percentage / 100,
                percentage_retirement_insurance=trabajador.pension_contribution_percentage / 100,
                percentage_retirement_fund=trabajador.solidarity_pension_fund_contribution_percentage / 100
            )
            liquidacion = calculate_settlement(settlement_params)
            
            return render_template(
                "resultado_liquidacion.html",
                nombre=trabajador.name,
                cedula=trabajador.id,
                salario_basico=trabajador.basic_salary,
                dias_trabajados=trabajador.monthly_worked_days,
                dias_licencia_enfermedad=trabajador.sick_leave_days,
                subsidio_transporte=trabajador.transportation_allowance,
                horas_extra_diurnas=trabajador.daytime_overtime_hours,
                horas_extra_nocturnas=trabajador.nighttime_overtime_hours,
                horas_extra_diurnas_festivos=trabajador.daytime_holiday_overtime_hours,
                horas_extra_nocturnas_festivos=trabajador.nighttime_holiday_overtime_hours,
                dias_licencia=trabajador.days_leave,
                porcentaje_seguro_salud=trabajador.health_contribution_percentage,
                porcentaje_aporte_pensiones=trabajador.pension_contribution_percentage,
                porcentaje_aporte_fondo_retiro=trabajador.solidarity_pension_fund_contribution_percentage,
                total_a_pagar=liquidacion
            )
        else:
            return render_template("resultado.html", mensaje="No se encontró ningún trabajador con el nombre y la cédula proporcionados.")
    except Temployer.not_found as e:
        return render_template("resultado.html", mensaje=str(e))
    except Exception as e:
        return render_template("resultado.html", mensaje=str(e))
    

@blueprint.route('/description')
def description():
    return render_template('description.html', 
                           MINIMUM_WAGE=mp.MINIMUM_WAGE,
                           UVT=mp.UVT,
                           EXTRA_HOUR_DAYSHIFT=mp.EXTRA_HOUR_DAYSHIFT,
                           EXTRA_HOUR_NIGHTSHIFT=mp.EXTRA_HOUR_NIGHTSHIFT,
                           EXTRA_HOUR_DAYSHIFT_HOLIDAYS=mp.EXTRA_HOUR_DAYSHIFT_HOLIDAYS,
                           EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS=mp.EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS,
                           MONTH_DAYS=mp.MONTH_DAYS,
                           MONTH_HOURS=mp.MONTH_HOURS,
                           PERCENTAGE_HEALTH_INSURANCE=mp.PERCENTAGE_HEALTH_INSURANCE * 100,
                           PERCENTAGE_RETIREMENT_FUND=mp.PERCENTAGE_RETIREMENT_FUND * 100)


app.register_blueprint(blueprint, url_prefix="/")


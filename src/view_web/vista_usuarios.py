from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

blueprint = Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement
from Model.TablesEmployer import Employerinput
import Model.TablesEmployer as Temployer
app = Flask(__name__)
app.secret_key = "supersecretkey"
# Definir la clase NuevoEmpleado
class NuevoEmpleado:
    def __init__(self, name, basic_salary, workdays, sick_leave, transportation_aid, dayshift_extra_hours, nightshift_extra_hours, dayshift_extra_hours_holidays, nightshift_extra_hours_holidays, leave_days, percentage_health_insurance, percentage_retirement_insurance, percentage_retirement_fund, id=None):
        self.id = id
        self.name = name
        self.basic_salary = basic_salary
        self.workdays = workdays
        self.sick_leave = sick_leave
        self.transportation_aid = transportation_aid
        self.dayshift_extra_hours = dayshift_extra_hours
        self.nightshift_extra_hours = nightshift_extra_hours
        self.dayshift_extra_hours_holidays = dayshift_extra_hours_holidays
        self.nightshift_extra_hours_holidays = nightshift_extra_hours_holidays
        self.leave_days = leave_days
        self.percentage_health_insurance = percentage_health_insurance
        self.percentage_retirement_insurance = percentage_retirement_insurance
        self.percentage_retirement_fund = percentage_retirement_fund

# Definir las rutas y las funciones asociadas
@blueprint.route("/")
def home():
    return render_template('inicio.html')

@blueprint.route('/crear-usuario')
def crear_usuario():

    # Obtener los datos del formulario
    nombre = request.args['nombre']
    cedula = request.args['cedula']
    salario = request.args['salario']
    Días_Trabajados = request.args['Días_Trabajados']
    Días_enfermedad = request.args['Días_enfermedad']
    Auxilio_Trasporte = request.args['Auxilio_Trasporte']
    Horas_diurnas_extra = request.args['Horas_diurnas_extra']
    Horas_nocturnas_extra = request.args['Horas_nocturnas_extra']
    Horas_diurnas_extra_festivo = request.args['Horas_diurnas_extra_festivo']
    Horas_nocturnas_extra_festivo = request.args['Horas_nocturnas_extra_festivo']
    Días_Libres = request.args['Días_Libres']
    Porcentaje_seguro_salud = request.args['Porcentaje_seguro_salud']
    Porcentaje_fondo_retiro = request.args['Porcentaje_retiro']
    Porcentaje_fondo_solidario = request.args['percentage_retirement_fund']

    # Crear una instancia de NuevoEmpleado con los datos del formulario
    nuevo_empleado = Employerinput(nombre=nombre, cedula=cedula, salario=salario, Días_Trabajados=Días_Trabajados, Días_enfermedad=Días_enfermedad, Auxilio_Trasporte=Auxilio_Trasporte,
                Horas_diurnas_extra=Horas_diurnas_extra, Horas_nocturnas_extra=Horas_nocturnas_extra, Horas_diurnas_extra_festivo=Horas_diurnas_extra_festivo,
                Horas_nocturnas_extra_festivo=Horas_nocturnas_extra_festivo, Días_Libres=Días_Libres, Porcentaje_seguro_salud=Porcentaje_seguro_salud,
                Porcentaje_fondo_retiro=Porcentaje_fondo_retiro, Porcentaje_fondo_solidario=Porcentaje_fondo_solidario)

    # Insertar el nuevo empleado en la base de datos
    WorkersIncomeData.Insert(nuevo_empleado)

        # Redirigir al usuario a la página de resultado después de insertar los datos
    return redirect(url_for('vista_usuarios.resultado'))


@blueprint.route('/resultado')
def resultado():
    # Aquí puedes incluir el código para mostrar los resultados después de procesar los datos
    return render_template('resultado.html')

@blueprint.route("/buscar_usuario")
def buscar_usuario():
    # Aquí podrías manejar la lógica para buscar un usuario
    return render_template('buscar_usuario.html')

@blueprint.route("/actualizar_usuario")
def modificar_usuario():
    # Aquí podrías manejar la lógica para modificar un usuario
    return render_template('actualizar_usuario.html')

@blueprint.route("/eliminar_usuario")
def eliminar_usuario():
    # Aquí podrías manejar la lógica para eliminar un usuario
    return render_template('eliminar_usuario.html')

# Registrar el blueprint en la aplicación Flask
app.register_blueprint(blueprint)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
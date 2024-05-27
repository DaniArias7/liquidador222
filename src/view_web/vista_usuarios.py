from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

blueprint = Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from src.Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement
import src.Model.TablesEmployer as Temployer
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

@blueprint.route('/crear-usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form.get('name')
        basic_salary = request.form.get('basic_salary')
        workdays = request.form.get('workdays')
        sick_leave = request.form.get('sick_leave')
        transportation_aid = request.form.get('transportation_aid')
        dayshift_extra_hours = request.form.get('dayshift_extra_hours')
        nightshift_extra_hours = request.form.get('nightshift_extra_hours')
        dayshift_extra_hours_holidays = request.form.get('dayshift_extra_hours_holidays')
        nightshift_extra_hours_holidays = request.form.get('nightshift_extra_hours_holidays')
        leave_days = request.form.get('leave_days')
        percentage_health_insurance = request.form.get('percentage_health_insurance')
        percentage_retirement_insurance = request.form.get('percentage_retirement_insurance')
        percentage_retirement_fund = request.form.get('percentage_retirement_fund')

        # Crear una instancia de NuevoEmpleado con los datos del formulario
        nuevo_empleado = NuevoEmpleado(name=name, basic_salary=basic_salary, workdays=workdays, sick_leave=sick_leave, transportation_aid=transportation_aid, dayshift_extra_hours=dayshift_extra_hours, nightshift_extra_hours=nightshift_extra_hours, dayshift_extra_hours_holidays=dayshift_extra_hours_holidays, nightshift_extra_hours_holidays=nightshift_extra_hours_holidays, leave_days=leave_days, percentage_health_insurance=percentage_health_insurance, percentage_retirement_insurance=percentage_retirement_insurance, percentage_retirement_fund=percentage_retirement_fund)

        # Insertar el nuevo empleado en la base de datos
        WorkersIncomeData.Insert(nuevo_empleado)

        # Redirigir al usuario a la página de resultado después de insertar los datos
        return redirect(url_for('vista_usuarios.resultado'))

    # Si el método es GET o si se procesaron los datos del formulario, renderizar el formulario
    return render_template('crear_usuario.html')

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
import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from src.Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement
import src.Model.TablesEmployer as Temployer
from flask import Blueprint, request, redirect, url_for, render_template
from src.Controller.Controladortablas import WorkersIncomeData

blueprint = Blueprint('vista_usuarios', __name__)

@blueprint.route('/')
def index():
    return render_template('inicio.html')

@blueprint.route('/crear-usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        name = request.form['name']
        basic_salary = float(request.form['basic_salary'])
        workdays = int(request.form['workdays'])
        sick_leave = int(request.form['sick_leave'])
        transportation_aid = float(request.form['transportation_aid'])
        dayshift_extra_hours = int(request.form['dayshift_extra_hours'])
        nightshift_extra_hours = int(request.form['nightshift_extra_hours'])
        dayshift_extra_hours_holidays = int(request.form['dayshift_extra_hours_holidays'])
        nightshift_extra_hours_holidays = int(request.form['nightshift_extra_hours_holidays'])
        leave_days = int(request.form['leave_days'])
        percentage_health_insurance = float(request.form['percentage_health_insurance'])
        percentage_retirement_insurance = float(request.form['percentage_retirement_insurance'])
        percentage_retirement_fund = float(request.form['percentage_retirement_fund'])

        new_employer = Temployer.Employerinput(
            name=name,
            id="dummy_id",  # Agrega lógica para ID si es necesario
            basic_salary=basic_salary,
            monthly_worked_days=workdays,
            days_leave=leave_days,
            transportation_allowance=transportation_aid,
            daytime_overtime_hours=dayshift_extra_hours,
            nighttime_overtime_hours=nightshift_extra_hours,
            daytime_holiday_overtime_hours=dayshift_extra_hours_holidays,
            nighttime_holiday_overtime_hours=nightshift_extra_hours_holidays,
            sick_leave_days=sick_leave,
            health_contribution_percentage=percentage_health_insurance,
            pension_contribution_percentage=percentage_retirement_insurance,
            solidarity_pension_fund_contribution_percentage=percentage_retirement_fund
        )

        WorkersIncomeData.Insert(new_employer)
        return redirect(url_for('vista_usuarios.resultado'))

    return render_template('crear_usuario.html')

@blueprint.route('/resultado')
def resultado():
    return render_template('resultado.html')

@blueprint.route('/buscar-usuario', methods=['GET', 'POST'])
def buscar_usuario():
    if request.method == 'POST':
        nombre = request.form['buscar_nombre']
        usuario = WorkersIncomeData.buscar_usuario_por_nombre(nombre)
        if usuario:
            return render_template('resultado_busqueda.html', usuario=usuario)
        else:
            flash("Usuario no encontrado", "error")
            return redirect(url_for('vista_usuarios.buscar_usuario'))

    return render_template('buscar_usuario.html')

@blueprint.route('/actualizar-informacion', methods=['GET', 'POST'])
def actualizar_informacion():
    if request.method == 'POST':
        modificar_nombre = request.form['modificar_nombre']
        nuevo_nombre = request.form['nuevo_nombre']
        usuario = WorkersIncomeData.buscar_usuario_por_nombre(modificar_nombre)
        if usuario:
            usuario.name = nuevo_nombre
            WorkersIncomeData.actualizar_usuario(usuario)
            flash("Usuario actualizado exitosamente", "success")
            return redirect(url_for('vista_usuarios.resultado_actualizacion'))
        else:
            flash("Usuario no encontrado", "error")
            return redirect(url_for('vista_usuarios.actualizar_informacion'))

    return render_template('actualizar_usuario.html')

@blueprint.route('/eliminar-usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'POST':
        eliminar_nombre = request.form['eliminar_nombre']
        eliminar_apellido = request.form['eliminar_apellido']
        exito = WorkersIncomeData.eliminar_usuario_por_nombre_apellido(eliminar_nombre, eliminar_apellido)
        if exito:
            flash("Usuario eliminado exitosamente", "success")
            return redirect(url_for('vista_usuarios.resultado_eliminacion'))
        else:
            flash("Usuario no encontrado", "error")
            return redirect(url_for('vista_usuarios.eliminar_usuario'))

    return render_template('eliminar_usuario.html')

@blueprint.route('/resultado_busqueda')
def resultado_busqueda():
    nombre = request.args.get('nombre')
    usuario = WorkersIncomeData.buscar_usuario_por_nombre(nombre)
    return render_template('resultado_busqueda.html', usuario=usuario)

@blueprint.route('/resultado_actualizacion')
def resultado_actualizacion():
    return render_template('resultado_actualizacion.html')

@blueprint.route('/resultado_eliminacion')
def resultado_eliminacion():
    return render_template('resultado_eliminacion.html')

from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import sys
import uuid
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from src.Controller.Controladortablas import WorkersIncomeData, WorkersoutputsData
from src.Model.MonthlyPaymentLogic import SettlementParameters, calculate_settlement
import src.Model.TablesEmployer as Temployer
from flask import Blueprint, request, redirect, url_for, render_template, flash

blueprint = Blueprint('vista_usuarios', __name__)

@blueprint.route('/')
def index():
    return render_template('inicio.html')

@blueprint.route('/crear-usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        basic_salary = float(request.form['basic_salary'])
        monthly_worked_days = int(request.form['monthly_worked_days'])
        days_leave = int(request.form['days_leave'])
        transportation_allowance = float(request.form['transportation_allowance'])
        daytime_overtime_hours = int(request.form['daytime_overtime_hours'])
        nighttime_overtime_hours = int(request.form['nighttime_overtime_hours'])
        daytime_holiday_overtime_hours = int(request.form['daytime_holiday_overtime_hours'])
        nighttime_holiday_overtime_hours = int(request.form['nighttime_holiday_overtime_hours'])
        sick_leave_days = int(request.form['sick_leave_days'])
        health_contribution_percentage = float(request.form['health_contribution_percentage'])
        pension_contribution_percentage = float(request.form['pension_contribution_percentage'])
        solidarity_pension_fund_contribution_percentage = float(request.form['solidarity_pension_fund_contribution_percentage'])

        # Crear una instancia de Employerinput
        employer = Temployer.Employerinput(
            name=name,
            id=id,
            basic_salary=basic_salary,
            monthly_worked_days=monthly_worked_days,
            days_leave=days_leave,
            transportation_allowance=transportation_allowance,
            daytime_overtime_hours=daytime_overtime_hours,
            nighttime_overtime_hours=nighttime_overtime_hours,
            daytime_holiday_overtime_hours=daytime_holiday_overtime_hours,
            nighttime_holiday_overtime_hours=nighttime_holiday_overtime_hours,
            sick_leave_days=sick_leave_days,
            health_contribution_percentage=health_contribution_percentage,
            pension_contribution_percentage=pension_contribution_percentage,
            solidarity_pension_fund_contribution_percentage=solidarity_pension_fund_contribution_percentage
        )

        try:
            # Verificar si el usuario ya existe en la base de datos
            Temployer.Employerinput.primary_key(name, id, WorkersIncomeData)
            # Insertar el usuario en la base de datos
            WorkersIncomeData.Insert(employer)
            flash('Usuario creado correctamente.', 'success')
            return redirect(url_for('vista_usuarios.index'))
        except Temployer.faileprimarykey as e:
            flash(str(e), 'danger')
        except Exception as e:
            flash(str(e), 'danger')

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
            try:
                WorkersIncomeData.actualizar_usuario(usuario)
                flash("Usuario actualizado exitosamente", "success")
            except Exception as e:
                flash(f"Error al actualizar usuario: {str(e)}", "error")
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

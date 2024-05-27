import sys
sys.path.append("C:/Users/ACER/liquidador_nomina")
sys.path.append("./src")
from flask import Flask, request, redirect, url_for, render_template_string
from src.Controller.Controladortablas import WorkersIncomeData
import src.Model.TablesEmployer as Temployer

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template_string('''
        <h1>Registrar Nuevo Empleado</h1>
        <form action="/create_user" method="post">
            Nombre: <input type="text" name="name"><br>
            ID: <input type="text" name="id"><br>
            Salario Básico: <input type="number" step="0.01" name="basic_salary"><br>
            Días Trabajados Mensuales: <input type="number" name="monthly_worked_days"><br>
            Días de Licencia: <input type="number" name="days_leave"><br>
            Subsidio de Transporte: <input type="number" step="0.01" name="transportation_allowance"><br>
            Horas Extras Diurnas: <input type="number" name="daytime_overtime_hours"><br>
            Horas Extras Nocturnas: <input type="number" name="nighttime_overtime_hours"><br>
            Horas Extras Festivas Diurnas: <input type="number" name="daytime_holiday_overtime_hours"><br>
            Horas Extras Festivas Nocturnas: <input type="number" name="nighttime_holiday_overtime_hours"><br>
            Días de Incapacidad: <input type="number" name="sick_leave_days"><br>
            Porcentaje de Contribución a la Salud: <input type="number" step="0.01" name="health_contribution_percentage"><br>
            Porcentaje de Contribución a la Pensión: <input type="number" step="0.01" name="pension_contribution_percentage"><br>
            Porcentaje de Contribución al Fondo de Solidaridad Pensional: <input type="number" step="0.01" name="solidarity_pension_fund_contribution_percentage"><br>
            <input type="submit" value="Registrar">
        </form>
    ''')

@app.route('/create_user', methods=['POST'])
def create_user():
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

    new_employer = Temployer.Employerinput(
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

    WorkersIncomeData.Insert(new_employer)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

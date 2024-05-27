import sys
import os
from MonthlyPaymentLogic import *


# Obtenemos la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtenemos la ruta del directorio principal del proyecto
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
# Agregamos el directorio principal del proyecto al sys.path
sys.path.append(project_dir)

# Ahora podemos importar los módulos del proyecto
from MonthlyPaymentLogic import *
import MonthlyPaymentLogic as mp
#from Controller.Controladortablas import WorkersIncomeData

class faileprimarykey(Exception):
    pass

class not_exist(Exception):
    pass

class not_found(Exception):
    pass

class updatenotfount(Exception):
    pass

class Employerinput:
    """
    Class to represent input data for an employer.

    Parameters:
    -----------
    name : str
        Name of the employer.
    id : int
        Unique identifier for the employer.
    basic_salary : float
        Basic salary of the employer.
    monthly_worked_days : int
        Number of days the employer worked in a month.
    days_leave : int
        Number of days the employer took leave.
    transportation_allowance : float
        Allowance for transportation expenses.
    daytime_overtime_hours : float
        Number of overtime hours worked during the daytime.
    nighttime_overtime_hours : float
        Number of overtime hours worked during the nighttime.
    daytime_holiday_overtime_hours : float
        Number of overtime hours worked during daytime holidays.
    nighttime_holiday_overtime_hours : float
        Number of overtime hours worked during nighttime holidays.
    sick_leave_days : int
        Number of sick leave days taken by the employer.
    health_contribution_percentage : float
        Percentage of health insurance contribution.
    pension_contribution_percentage : float
        Percentage of pension contribution.
    solidarity_pension_fund_contribution_percentage : float
        Percentage of contribution to the solidarity pension fund.
    """
    def __init__(self,name, id, basic_salary, monthly_worked_days, days_leave, transportation_allowance,
                 daytime_overtime_hours, nighttime_overtime_hours, daytime_holiday_overtime_hours,
                 nighttime_holiday_overtime_hours, sick_leave_days, health_contribution_percentage,
                 pension_contribution_percentage, solidarity_pension_fund_contribution_percentage):
        
        self.name = name
        self.id = id
        self.basic_salary = basic_salary
        self.monthly_worked_days = monthly_worked_days
        self.days_leave = days_leave
        self.transportation_allowance = transportation_allowance
        self.daytime_overtime_hours = daytime_overtime_hours
        self.nighttime_overtime_hours = nighttime_overtime_hours
        self.daytime_holiday_overtime_hours = daytime_holiday_overtime_hours
        self.nighttime_holiday_overtime_hours = nighttime_holiday_overtime_hours
        self.sick_leave_days = sick_leave_days
        self.health_contribution_percentage = health_contribution_percentage
        self.pension_contribution_percentage = pension_contribution_percentage
        self.solidarity_pension_fund_contribution_percentage = solidarity_pension_fund_contribution_percentage
    
    def Isequal(self, dbneon):
        """
        Check if two Employerinput instances are equal in all attributes.

        Parameters:
        -----------
        dbneon : Employerinput
            Another instance of Employerinput to compare with.

        Raises:
        -------
        AssertionError:
            If any attribute of the two instances is not equal.
        """
        assert (self.name == dbneon.name)
        assert (self.id == dbneon.id)
        assert (self.basic_salary == dbneon.basic_salary)
        assert (self.monthly_worked_days == dbneon.monthly_worked_days)
        assert (self.days_leave == dbneon.days_leave)
        assert (self.transportation_allowance == dbneon.transportation_allowance)
        assert (self.daytime_overtime_hours == dbneon.daytime_overtime_hours)
        assert (self.nighttime_overtime_hours == dbneon.nighttime_overtime_hours)
        assert (self.daytime_holiday_overtime_hours == dbneon.daytime_holiday_overtime_hours)
        assert (self.nighttime_holiday_overtime_hours == dbneon.nighttime_holiday_overtime_hours)
        assert (self.sick_leave_days == dbneon.sick_leave_days)
        assert (self.health_contribution_percentage == dbneon.health_contribution_percentage)
        assert (self.pension_contribution_percentage == dbneon.pension_contribution_percentage)
        assert (self.solidarity_pension_fund_contribution_percentage == dbneon.solidarity_pension_fund_contribution_percentage)
    
    def primary_key(name, id, module):
        """
        Check if the given name and id combination already exists in the database.

        Parameters:
        -----------
        name : str
            Name of the employer.
        id : int
            Unique identifier for the employer.
        module : Module
            Module containing the QueryWorker function to query the database.

        Raises:
        -------
        faileprimarykey:
            If the given name and id combination already exists in the database.
        """      
        value = module.QueryWorker(name, id)
        if value is not None:
            raise faileprimarykey("Ya ingresaste este usuario: {} - {}".format(name, id))
        
    @staticmethod
    def notexist(employer):
        """
        Check if any attribute of the employer object is None.

        Parameters:
        -----------
        employer : Employerinput
            An instance of the Employerinput class.

        Raises:
        -------
        not_exist:
            If any attribute of the employer object is None.
        """
        # Verificar si algún atributo es None
        if any(value is None for value in employer.__dict__.values()):
            raise not_exist("Falta un valor al crear la clase Employerinput")
    
    def valor_presente(atributo):
        """
        Check if the given attribute is present in the list of expected attributes.

        Parameters:
        -----------
        atributo : str
            The name of the attribute to check.

        Raises:
        -------
        updatenotfount:
            If the given attribute is not found in the list of expected attributes.
        """
        lista_atributos=parametros_constructor = [
                                            "name", "id", "basic_salary", "monthly_worked_days", "days_leave", "transportation_allowance",
                                            "daytime_overtime_hours", "nighttime_overtime_hours", "daytime_holiday_overtime_hours",
                                            "nighttime_holiday_overtime_hours", "sick_leave_days", "health_contribution_percentage",
                                            "pension_contribution_percentage", "solidarity_pension_fund_contribution_percentage"]
        if atributo  not in lista_atributos:
            raise updatenotfount("no se encuentra el valor para realizar el update")
    




class Employeroutput():
    """
    Class to represent output data for an employer.

    Parameters:
    -----------
    name : str
        Name of the employer.
    id : int
        Unique identifier for the employer.
    basic_salary : float
        Basic salary of the employer.
    workdays : int
        Number of days the employer worked.
    sick_leave : int
        Number of days the employer took sick leave.
    transportation_aid : float
        Financial aid for transportation expenses.
    dayshift_extra_hours : float
        Number of extra hours worked during the day shift.
    nightshift_extra_hours : float
        Number of extra hours worked during the night shift.
    dayshift_extra_hours_holidays : float
        Number of extra hours worked during day shift holidays.
    nightshift_extra_hours_holidays : float
        Number of extra hours worked during night shift holidays.
    leave_days : int
        Number of leave days taken by the employer.
    percentage_health_insurance : float
        Percentage of health insurance contribution.
    percentage_retirement_insurance : float
        Percentage of retirement insurance contribution.
    percentage_retirement_fund : float
        Percentage of contribution to retirement fund.
    devengado : float
        Amount earned by the employer.
    deducido : float
        Amount deducted from the employer's earnings.
    amounttopay : float
        Total amount to be paid to the employer.
    """

    def __init__(self, name,id,basic_salary, workdays, sick_leave, transportation_aid, dayshift_extra_hours, nightshift_extra_hours,
                 dayshift_extra_hours_holidays, nightshift_extra_hours_holidays, leave_days, percentage_health_insurance,
                 percentage_retirement_insurance, percentage_retirement_fund,devengado,deducido,amounttopay):
        self.name = name
        self.id = id
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
        self.devengado=devengado
        self.deducido=deducido
        self.amounttopay=amounttopay
    
    def Isequivalent(self, dbneon):
        """
        Check if two Employeroutput instances are equivalent in all attributes.

        Parameters:
        -----------
        dbneon : Employeroutput
            Another instance of Employeroutput to compare with.

        Returns:
        --------
        bool:
            True if all attributes are equivalent, False otherwise.
        """
        assert (self.name == dbneon.name)
        assert (self.id == dbneon.id)
        assert (self.basic_salary == dbneon.basic_salary)
        assert (self.workdays == dbneon.workdays)
        assert (self.sick_leave == dbneon.sick_leave)
        assert (self.transportation_aid == dbneon.transportation_aid)
        assert (self.dayshift_extra_hours == dbneon.dayshift_extra_hours) 
        assert (self.nightshift_extra_hours == dbneon.nightshift_extra_hours) 
        assert (self.dayshift_extra_hours_holidays == dbneon.dayshift_extra_hours_holidays)
        assert (self.nightshift_extra_hours_holidays == dbneon.nightshift_extra_hours_holidays)
        assert (self.leave_days == dbneon.leave_days) 
        assert (self.percentage_health_insurance == dbneon.percentage_health_insurance)
        assert (self.percentage_retirement_insurance == dbneon.percentage_retirement_insurance) 
        assert (self.percentage_retirement_fund == dbneon.percentage_retirement_fund) 
        assert (self.devengado == dbneon.devengado) 
        assert (self.deducido == dbneon.deducido)
        assert (self.amounttopay == dbneon.amounttopay)
        return True
    
    def employernotfound(query):
        """
        Raise an exception if the queried employer is not found.

        Parameters:
        -----------
        query : object
            The result of a query operation. If None, it indicates that the employer was not found.

        Raises:
        -------
        not_found:
            If the queried employer is not found.
        """
        if query is None:
            raise not_found("no se ha encontrado su busqueda")   
            
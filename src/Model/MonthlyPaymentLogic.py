from math import trunc

# Constants
# MINIMUM_WAGE this constant use for declaration the salary basic in colombia 
MINIMUM_WAGE = 1300000  # Minimum wage in Colombia
UVT = 47065  # Value of a Tax Value Unit (UVT)
# EXTRA_HOUR_DAYSHIFT use for calculate porcentaje hour free extra work 
EXTRA_HOUR_DAYSHIFT = 1.25  # Factor to calculate extra hours in day shift
EXTRA_HOUR_NIGHTSHIFT = 1.75  # Factor to calculate extra hours in night shift
EXTRA_HOUR_DAYSHIFT_HOLIDAYS = 2.00  # Factor to calculate extra hours in day shift on holidays
EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS = 2.50  # Factor to calculate extra hours in night shift on holidays
MONTH_DAYS = 30  # Average days in a month
MONTH_HOURS = 235  # Average hours in a month
PERCENTAGE_HEALTH_INSURANCE = 0.04  # Percentage of salary destined for health insurance
PERCENTAGE_RETIREMENT_INSURANCE = 0.04  # Percentage of salary destined for retirement insurance
PERCENTAGE_RETIREMENT_FUND= 0.01  # Percentage of salary destined for retirement fund
PERCENTAGE_SICK_LEAVE = 0.6666  # Percentage of salary paid during a sick leave
RETIREMENT_FUND_SALARY = 5000000 # Minimum salary thay pays retirement fund
MAXIMUM_DAYS_SICKLEAVE = 3 # Maximund days of sick leave that the business can pay
# List of salary holdback percentages for different salary ranges
SALARY_HOLDBACK_PERCENTAGES = [
    (0, 95, 0.0, 0.0),
    (95, 150, 0.19, 0.0),
    (150, 360, 0.28, 10.0),
    (360, 640, 0.33, 69.0),
    (640, 945, 0.35, 162.0),
    (945, 2300, 0.37, 268.0),
    (2300, float('inf'), 0.39, 770.0)
]


# Exceptions
# This exception class is used when the provided minimum wage is lower than the required minimum.
class LowerMinimumWageError(Exception):
    pass

# This exception class is used when no work days are provided for calculation.
class NoWorkDaysError(Exception):
    pass

# This exception class is used when the provided health insurance percentage is invalid.
class InvalidHealthInsurancePercentageError(Exception):
    pass

# This exception class is used when the provided retirement fund percentage is invalid.
class InvalidRetirementFundPercentageError(Exception):
    pass

# This exception class is used when the provided transportation aid is invalid.
class InvalidTransportationAidError(Exception):
    pass

# This exception class is used when the provided retirement fund percentage is valid but the salary is less than a specific value.
class InvalidRetirementFundPercentageErrorSalaryMenor(Exception):
    pass

# This exception class is used when there is a syntax error in the provided input.
class SintaxiError(Exception):
    pass

# This exception class is used when a negative number of work days is provided.
class NegativedayWork(Exception):
    pass

class workdayslimit(Exception):
    pass

class negativeparameter(Exception):
    pass

# Class for settlement parameters
# Constructor of the class that initializes the parameters necessary for salary settlement.
class SettlementParameters:
    def __init__(self, basic_salary, workdays, sick_leave, transportation_aid, dayshift_extra_hours,
                 nightshift_extra_hours, dayshift_extra_hours_holidays, nightshift_extra_hours_holidays,
                 leave_days, percentage_health_insurance, percentage_retirement_insurance, percentage_retirement_fund):
        
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
    
    # Static method to validate settlement parameters.
    
    @staticmethod
    def validate_parameters(basic_salary, workdays, transportation_aid, percentage_health_insurance,
                            percentage_retirement_insurance, percentage_retirement_fund):
       
        if not isinstance(basic_salary, (int, float)):
            raise SintaxiError("El salario base debe ser un número entero o flotante")
        
        # Verifies that the basic salary is greater than 0.
        if basic_salary == 0:
            raise LowerMinimumWageError("El salario base debe ser mayor que 0.")

        if workdays == 0:
            raise NoWorkDaysError("Los días de trabajo no pueden ser cero.")

        if percentage_health_insurance == 0:
            raise InvalidHealthInsurancePercentageError("El porcentaje de seguro de salud no puede ser cero.")

        if basic_salary >= RETIREMENT_FUND_SALARY and percentage_retirement_fund == 0:
            raise InvalidRetirementFundPercentageError(
                "El porcentaje de fondo de retiro debe ser mayor que cero para salarios superiores a 5.000.000.")

        if basic_salary < RETIREMENT_FUND_SALARY and percentage_retirement_fund != 0:
            raise InvalidRetirementFundPercentageErrorSalaryMenor(
                "El porcentaje de fondo de retiro debe ser cero para salarios inferiores a 5.000.000.")

        if basic_salary > 2*MINIMUM_WAGE and transportation_aid != 0:
            raise InvalidTransportationAidError(
                "El auxilio de transporte debe ser cero para salarios superiores a 2.600.000.")

        if workdays < 0:
            raise NegativedayWork("El número de días de trabajo no puede ser negativo.")
        elif workdays > 30:
            raise workdayslimit("Los dias de trabajo no puede ser superiores a 30 dias")
        

# Helper functions
def calculate_salary(basic_salary, workdays, leave_days, sick_leave): 
    """
    Calculate the salary based on workdays, leave days, and sick leave.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - workdays: The number of days the employee worked.
    - leave_days: The number of days the employee took leave.
    - sick_leave: The number of days the employee took sick leave.

    Returns:
    - The calculated salary.
    """
    
    return (basic_salary / MONTH_DAYS) * (workdays + leave_days + sick_leave)


def calculate_transportation_aid(transportation_aid, basic_salary): 
    """
    Calculate the transportation aid.

    Parameters:
    - transportation_aid: The amount of transportation aid provided.
    - basic_salary: The basic salary of the employee.

    Returns:
    - The calculated transportation aid.
    """
    if basic_salary >= 2*MINIMUM_WAGE:
        return 0
    return transportation_aid


def calculate_extra_hours(basic_salary, extra_hours, extra_hour_type): 
    """
    Calculate the extra hours pay based on the multiplier.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - extra_hours: The number of extra hours worked.
    - extra_hour_type: The multiplier for extra hours pay.

    Returns:
    - The calculated extra hours pay.
    """
    return (basic_salary / MONTH_HOURS) * extra_hours * extra_hour_type


def calculate_health_insurance(basic_salary, percentage_health_insurance):
    """
    Calculate the health insurance contribution.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - percentage_health_insurance: The percentage of the basic salary for health insurance.

    Returns:
    - The calculated health insurance contribution.
    """
    return basic_salary * percentage_health_insurance


def calculate_retirement_insurance(basic_salary, percentage_retirement_insurance): 
    """
    Calculate the retirement insurance contribution.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - percentage_retirement_insurance: The percentage of the basic salary for retirement insurance.

    Returns:
    - The calculated retirement insurance contribution.
    """
    return basic_salary * percentage_retirement_insurance


def calculate_retirement_fund(basic_salary, percentage_retirement_fund): 
    """
    Calculate the retirement fund contribution.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - percentage_retirement_fund: The percentage of the basic salary for retirement fund.

    Returns:
    - The calculated retirement fund contribution.
    """
    if basic_salary >= RETIREMENT_FUND_SALARY:
        return basic_salary * percentage_retirement_fund
    return 0


def calculate_sick_leave(basic_salary, days_sick_leave):
    """
    Calculate the sick leave pay.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - days_sick_leave: The number of sick leave days.

    Returns:
    - The calculated sick leave pay.
    """
    if days_sick_leave <= MAXIMUM_DAYS_SICKLEAVE and basic_salary >= MINIMUM_WAGE:
        return (basic_salary / MONTH_DAYS) * PERCENTAGE_SICK_LEAVE * days_sick_leave
    return 0


def calculate_leave(basic_salary, leave_days): 
    """
    Calculate the leave pay.

    Parameters:
    - basic_salary: The basic salary of the employee.
    - leave_days: The number of leave days.

    Returns:
    - The calculated leave pay.
    """
    return (basic_salary / MONTH_DAYS) * leave_days


def calculate_salary_holdback(basic_salary):
    """
    Calculate the salary holdback based on the salary range.

    Parameters:
    - basic_salary: The basic salary of the employee.

    Returns:
    - The calculated salary holdback.
    """
    salary_in_uvt = trunc(basic_salary / UVT)
    for lower_bound, upper_bound, percentage, number_of_uvt in SALARY_HOLDBACK_PERCENTAGES:
        if lower_bound <= salary_in_uvt < upper_bound:
            return (basic_salary/UVT) * percentage + (number_of_uvt * UVT)


def calculate_accrued_values(parameters): 
    """
    Calculate the total accrued values.

    Parameters:
    - parameters: An instance of SettlementParameters containing various parameters required for calculation.

    Returns:
    - The total accrued values.
    """
    basic_salary = parameters.basic_salary
    workdays = parameters.workdays
    sick_leave = parameters.sick_leave
    transportation_aid = parameters.transportation_aid
    dayshift_extra_hours = parameters.dayshift_extra_hours
    nightshift_extra_hours = parameters.nightshift_extra_hours
    dayshift_extra_hours_holidays = parameters.dayshift_extra_hours_holidays
    nightshift_extra_hours_holidays = parameters.nightshift_extra_hours_holidays
    leave_days = parameters.leave_days

    accrued_values = calculate_salary(basic_salary, workdays, leave_days, sick_leave)
    accrued_values += calculate_transportation_aid(transportation_aid, basic_salary)
    accrued_values += calculate_extra_hours(basic_salary, dayshift_extra_hours, EXTRA_HOUR_DAYSHIFT)
    accrued_values += calculate_extra_hours(basic_salary, nightshift_extra_hours, EXTRA_HOUR_NIGHTSHIFT)
    accrued_values += calculate_extra_hours(basic_salary, dayshift_extra_hours_holidays, EXTRA_HOUR_DAYSHIFT_HOLIDAYS)
    accrued_values += calculate_extra_hours(basic_salary, nightshift_extra_hours_holidays,
                                            EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS)
    return accrued_values


def calculate_deducted_values(parameters): 
    """
    Calculate the total deducted values.

    Parameters:
    - parameters: An instance of SettlementParameters containing various parameters required for calculation.

    Returns:
    - The total deducted values.
    """
    basic_salary = parameters.basic_salary
    percentage_health_insurance = parameters.percentage_health_insurance
    percentage_retirement_insurance = parameters.percentage_retirement_insurance
    percentage_retirement_fund = parameters.percentage_retirement_fund

    deducted_values = calculate_health_insurance(basic_salary, percentage_health_insurance)
    deducted_values += calculate_retirement_insurance(basic_salary, percentage_retirement_insurance)
    deducted_values += calculate_retirement_fund(basic_salary, percentage_retirement_fund)
    deducted_values += calculate_salary_holdback(basic_salary)
    return deducted_values


def calculate_settlement(parameters): 
    """
    Calculate the total settlement by subtracting deducted values from accrued values.

    Parameters:
    - parameters: An instance of SettlementParameters containing various parameters required for calculation.

    Returns:
    - The total settlement.
    """
    SettlementParameters.validate_parameters(parameters.basic_salary, parameters.workdays,
                                             parameters.transportation_aid,
                                             parameters.percentage_health_insurance,
                                             parameters.percentage_retirement_insurance,
                                             parameters.percentage_retirement_fund)

    accrued_values = calculate_accrued_values(parameters)
    deducted_values = calculate_deducted_values(parameters)
    return accrued_values - deducted_values
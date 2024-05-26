CREATE TABLE IF NOT EXISTS Employerinput (
    name varchar(300) NOT NULL,
    id varchar(300) PRIMARY KEY NOT NULL,
    basic_salary float NOT NULL,
    monthly_worked_days int NOT NULL,
    days_leave int NOT NULL,
    transportation_allowance float NOT NULL,
    daytime_overtime_hours int NOT NULL,
    nighttime_overtime_hours int NOT NULL,
    daytime_holiday_overtime_hours int NOT NULL,
    nighttime_holiday_overtime_hours int NOT NULL,
    sick_leave_days int NOT NULL,
    health_contribution_percentage float NOT NULL,
    pension_contribution_percentage float NOT NULL,
    solidarity_pension_fund_contribution_percentage float NOT NULL
);

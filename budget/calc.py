from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import case, func, select

# local
from budget.models import db, Income, Expense, Investments, Withholdings, Assets

# Budget functions
class Functions():
    def add(table_name,amount,frequency, description=""):
        try:
            match table_name:
                case "expense":
                    new_expense = Expense(amount=amount, description=description, frequency=frequency)
                    db.session.add(new_expense)
                case "income":
                    new_income = Income(amount=amount, description=description, frequency=frequency)
                    db.session.add(new_income)                
                case "investment":
                    new_investments = Investments(amount=amount, description=description)
                    db.session.add(new_investments)   
                case "asset":
                    new_asset = Assets(amount=amount, description=description)
                    db.session.add(new_asset)  
                case "withholding":
                    new_witholdings= Withholdings(amount=amount, description=description, frequency=frequency)
                    db.session.add(new_witholdings)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")

    def edit(editItem):
        try:
            db.session.add(editItem)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")
            
    def delete(deleteItem):
        try:
            db.session.delete(deleteItem)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")

class Sums():
    def get_frequency_case(table):
        return case(
            {
                "Annually": 1,
                "Bi-Annually": 2,
                "Quarterly": 4,
                "Monthly": 12,
            },
            value=table.frequency,
            else_=1
        )
    
    def total(table_name):
        try:
            match table_name:
                case "expenses":
                    return db.session.execute(select(func.sum(Expense.amount * Sums.get_frequency_case(Expense)))).scalar() or 0
                case "incomes":
                    return db.session.execute(select(func.sum(Income.amount * Sums.get_frequency_case(Income)))).scalar() or 0
                case "investments":
                    return db.session.execute(select(func.sum(Investments.amount))).scalar() or 0
                case "assets":
                    return db.session.execute(select(func.sum(Assets.amount))).scalar() or 0
                case "withholdings":
                    return db.session.execute(select(func.sum(Withholdings.amount * Sums.get_frequency_case(Withholdings)))).scalar() or 0
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")


    def net_worth():
        try:
            return (Sums.total('incomes')+Sums.total('investments')+Sums.total('assets'))-(Sums.total('expenses')+Sums.total('withholdings'))
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")
    
    def adjusted_total():
        try:
            return Sums.total('incomes')-(Sums.total('expenses')+Sums.total('withholdings'))
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")

class Reports():
    def get_report():
        try:
            return {
                # "expenses": Sums.total('expenses'),
                "incomes": Sums.total('incomes'),
                # "withholdings": Sums.total('withholdings'),
                "adjusted_total": Sums.adjusted_total()
            }
        except SQLAlchemyError as e:
            db.session.rollback()
            # log error and/or notify
            print(f"Database error occurred: {e}")
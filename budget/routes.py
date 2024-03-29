# Libraries 
import logging
from flask import Blueprint, current_app, render_template, jsonify, request

# Local imports
# from .__init__ import db
from .models import Income, Expense, Investments, Withholdings, Assets
from .calc import Functions, Sums, Reports

logging.basicConfig(filename='error.log', level=logging.ERROR)

bp = Blueprint('bp', __name__)

@bp.route('/')
def index():
    data = {}
    processes = [Income, Expense, Investments, Withholdings, Assets]

    for process in processes:
        process_sum = Sums.total(process.__tablename__)
        data["output_" + process.__tablename__] = "${:,.2f}".format(process_sum)
    data['net_worth'] = "${:,.2f}".format(Sums.net_worth())
    return render_template('index.html', data=data)

@bp.route('/table')
def overview():
    data = {}
    processes = [Income, Expense, Investments, Withholdings, Assets]

    for process in processes:
        records = process.query.all()
        formatted_records = []

        for record in records:
            # Convert the record to a dictionary
            record_dict = record.__dict__.copy()
            # Format the 'amount' field if it exists
            if 'amount' in record_dict:
                record_dict['amount'] = "${:,.2f}".format(record_dict['amount'])
            # Remove SQLAlchemy instance state
            record_dict.pop('_sa_instance_state', None)
            formatted_records.append(record_dict)

        data[process.__tablename__] = formatted_records
        process_sum = Sums.total(process.__tablename__)
        data["output_" + process.__tablename__] = "${:,.2f}".format(process_sum)
    return render_template('overview.html', data=data)

@bp.route('/api/data')
def data_api():
    data = Reports.get_report() 
    return jsonify(data)

@bp.route('/savings', methods=['GET'])
def savings():
    return render_template('savings.html')


@bp.route('/add', methods=['GET', 'POST'])
def add_item():
    data = request.get_json()
    # Update the db
    Functions.add(data['type'], data['amount'], data['frequency'], data['description'] )
    return jsonify({"message": f"${data['type']} added"}), 200


@bp.route('/edit/<int:id>', methods=['POST'])
def edit_item(id):
    data = request.get_json()
    process = data.get('type')
    match process:
        case "expense":
            item = Expense.query.get(id)
        case "income":
            item = Income.query.get(id)
        case "investment":
            item = Investments.query.get(id)
        case "asset":
            item = Assets.query.get(id)
        case "withholding":
            item = Withholdings.query.get(id)
    
    # Update the db
    item.description = data['description']
    item.amount = data['amount']
    item.frequency =  data['frequency']
    Functions.edit(item)
    return jsonify({"message": "${process} updated"}), 200


@bp.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    data = request.get_json()
    match data.get('type'):
        case "expense":
            Functions.delete(Expense.query.get(id))
        case "income":
            Functions.delete(Income.query.get(id))
        case "investment":
            Functions.delete(Investments.query.get(id))
        case "asset":
            Functions.delete(Assets.query.get(id))
        case "withholding":
            Functions.delete(Withholdings.query.get(id))
    return jsonify({"message": "${process} deleted"}), 200


@bp.errorhandler(404)
def page_not_found(e):
    current_app.logger.error(f"An error occurred: {e}")
    return render_template('errors/404.html'), 404

@bp.errorhandler(500)
def internal_server_error(e):
    current_app.logger.error(f"An error occurred: {e}")
    return render_template('errors/500.html'), 500

# @bp.errorhandler(Exception)
# def handle_exception(e):
#     # log the error
#     current_app.logger.error(f"An error occurred: {e}")
#     return render_template('errors/error.html')

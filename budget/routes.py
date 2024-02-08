# Libraries 
import logging
from flask import render_template, jsonify, request

# Local imports
from app import create_app
from models import db, Income, Expense, Investments, Withholdings, Assets
from calc import Functions, Sums

logging.basicConfig(filename='error.log', level=logging.ERROR)

app = create_app()

@app.route('/')
def index():
    data = {}
    processes = [Income, Expense, Investments, Withholdings, Assets]

    for process in processes:
        process_sum = Sums.total(process.__tablename__)
        data["output_" + process.__tablename__] = "${:,.2f}".format(process_sum)
    data['total'] = "${:,.2f}".format(Sums.balance())
    return render_template('index.html', data=data)

@app.route('/table')
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
    # data['total'] = "${:,.2f}".format(Sums.balance())
    return render_template('overview.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    data = request.get_json()
    # Update the db
    Functions.add(data['type'], data['amount'], data['frequency'], data['description'] )
    return jsonify({"message": f"${data['type']} added"}), 200


@app.route('/edit/<int:id>', methods=['POST'])
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
    db.session.commit()
    return jsonify({"message": "${process} updated"}), 200


@app.route('/delete/<int:id>', methods=['POST'])
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


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('errors/404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('errors/500.html'), 500

# @app.errorhandler(Exception)
# def handle_exception(e):
#     # log the error
#     app.logger.error(f"An error occurred: {e}")
#     return render_template('errors/error.html')

if __name__ == '__main__':
    app.run(debug=True)

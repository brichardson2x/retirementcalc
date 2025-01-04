from app import app
from flask import render_template, request, jsonify

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['POST']) # add methods=['POST']
def calculator():

    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    begin = data['current_age']
    retire = data['retirement_age']
    death = data['years_til_death']
    rate = data['average_annual_return']
    inflation = data['average_inflation_rate']
    spend_rate = data['spend_rate']
    four01k_principal = data['four01k_balance']
    four01k_contribution = data['four01k_monthly_contribution']
    employer_match_rate = data['company_match_rate']
    max_employer_match_rate = data['max_contribution_match_rate']
    ira_principal = data['ira_balance']
    ira_contribution = data['monthly_contribution_ira']
    hsa_principal = data['hsa_balance']
    hsa_contribution = data['monthly_contribution_hsa']
    employee_hsa_annual_contribution = data['annual_company_contribution']
    dividend_principal = data['dividend_balance']
    dividend_contribution = data['dividend_contribution']
    dividend_yield = data['dividend_yield_rate']

    print(data)
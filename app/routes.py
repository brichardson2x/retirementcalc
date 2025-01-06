from app import app
from flask import render_template, request, jsonify
from utils.calculations import pull_results

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['POST']) # add methods=['POST']
def calculator():
    try:
        data = request.json

        if not data:
            return jsonify({"message": "No data received"}), 437
    
        begin = float(data['current_age'])
        retire = float(data['retirement_age'])
        death = float(data['years_til_death'])
        rate = float(data['average_annual_return'])
        inflation = float(data['average_inflation_rate'])
        spend_rate = float(data['spend_rate'])
        four01k_principal = float(data['four01k_balance'])
        four01k_contribution = float(data['four01k_monthly_contribution'])
        employer_match_rate = float(data['company_match_rate'])
        max_employer_match_rate = float(data['max_contribution_match_rate'])
        ira_principal = float(data['ira_balance'])
        ira_contribution = float(data['monthly_contribution_ira'])
        hsa_principal = float(data['hsa_balance'])
        hsa_contribution = float(data['monthly_contribution_hsa'])
        employee_hsa_annual_contribution = float(data['annual_company_contribution'])
        dividend_principal = float(data['dividend_balance'])
        dividend_contribution = float(data['dividend_contribution'])
        dividend_yield = float(data['dividend_yield_rate'])

        sum_principal, sum_values, spend_values, years_left = pull_results(begin, retire, death, four01k_principal, ira_principal, hsa_principal, four01k_contribution, ira_contribution, hsa_contribution, dividend_principal, dividend_contribution, dividend_yield, rate, inflation, spend_rate, employer_match_rate, max_employer_match_rate, employee_hsa_annual_contribution)
        return jsonify({"sum_values": sum_principal, "sum_values": sum_values, "spend_values": spend_values, "years_left": years_left}, 200)
    
    except Exception as e:
        return jsonify({"error": f"Failed to decode JSON object: {str(e)}"}), 400
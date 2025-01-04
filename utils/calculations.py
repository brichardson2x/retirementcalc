def years_retirement(begin, retire, death):
    til_retire = retire - begin
    til_death = death - retire
    ssi_years = death - 65

    return til_retire, til_death, ssi_years

def definedbenefits_calc(principal, contribution, years, rate, employer_match_rate, max_employer_match_rate, employee_hsa_annual_contribution):
    match = employer_match_rate * max_employer_match_rate
    amount= principal
    values = []
    for i in range(years):
        values.append(amount)
        amount = amount*(1+rate) + contribution * 12 * (1 + match) + employee_hsa_annual_contribution

    return amount, values


def reinvest_dividend(principal, til_retire, rate, div_yield, contribution):
    amount = principal
    values = []
    for i in range(til_retire*4):
        values.append(amount)
        amount = amount*(1+rate/4) + contribution * 3 + amount * div_yield
    
    return amount, values

def liveoff_dividend(principal, rate, div_yield, til_death):
    amount = principal
    values = []
    for i in range(til_death*4):
        values.append(amount)
        amount = amount*(1+rate/4) - amount * div_yield

    return values

def include_ssi(ssi_years, til_retire, inflation):
    ssi_rate = (1 + inflation)**(til_retire) * 915
    ssi = 0
    values = []
    for i in range(ssi_years):
        values.append(ssi)
        ssi = ssi + ssi_rate
        ssi_rate = ssi_rate * (1 + inflation)

    return values

def sum_benefits_calc(four01k_principal, ira_principal, hsa_principal, four01k_contribution, ira_contribution, hsa_contribution, dividend_principal, dividend_contribution, dividend_yield, til_retire, rate, employer_match_rate, max_employer_match_rate, employee_hsa_annual_contribution):
    hsa_amount, hsa_values = definedbenefits_calc(hsa_principal, hsa_contribution, til_retire, rate, 0, 0, employee_hsa_annual_contribution)
    ira_amount, ira_values = definedbenefits_calc(ira_principal, ira_contribution, til_retire, rate, 0, 0, 0)
    four01k_amount, four01k_values = definedbenefits_calc(four01k_principal, four01k_contribution, til_retire, rate, employer_match_rate, max_employer_match_rate, 0)
    dividends_amount, dividends_values = reinvest_dividend(dividend_principal, til_retire, rate, dividend_yield, dividend_contribution)

    sum = hsa_amount + ira_amount + four01k_amount + dividends_amount
    sum_values = [hsa + ira + four01k + dividends for hsa, ira, four01k, dividends in zip(hsa_values, ira_values, four01k_values, dividends_values)]
    return sum, sum_values

def spend_benefits(principal, rate, ssi_years, til_retire, inflation, til_death, dividend_yield, spend_rate):
    years_left = 0
    dividends_values = []
    ssi_values = []
    values = []
    dividends_values = liveoff_dividend(principal, rate, dividend_yield, til_death)
    ssi_values = include_ssi(ssi_years, til_retire, inflation)
    for i in range(til_death):
        years_left =+ 1
        principal = principal*(1+rate) + ssi_values[i] + dividends_values[4 * i]- principal * spend_rate
        if principal < 0:
            values.append(0)
            break
        else:
            values.append(principal)

    return values, years_left

def pull_results(begin, retire, death, four01k_principal, ira_principal, hsa_principal, four01k_contribution, ira_contribution, hsa_contribution, dividend_principal, dividend_contribution, dividend_yield, rate, inflation, spend_rate, employer_match_rate, max_employer_match_rate, employee_hsa_annual_contribution):
    til_retire, til_death, ssi_years = years_retirement(begin, retire, death)
    sum_principal, sum_values = sum_benefits_calc(four01k_principal, ira_principal, hsa_principal, four01k_contribution, ira_contribution, hsa_contribution, dividend_principal, dividend_contribution, dividend_yield, til_retire, rate, employer_match_rate, max_employer_match_rate, employee_hsa_annual_contribution)
    spend_values, years_left = spend_benefits(sum_principal, rate, ssi_years, til_retire, inflation, til_death, dividend_yield, spend_rate)
    
    return sum_principal, sum_values, spend_values, years_left
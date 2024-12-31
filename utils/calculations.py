def years_retirement(begin, retire, death):
    til_retire = retire - begin
    til_death = death - retire
    ssi_years = death - 65

    return til_retire, til_death, ssi_years

def definedbenefits_calc(principal, contribution, years, rate, variance, match_upto, match_percent):
    rate = rate - (variance**2)/2
    match = match_upto * match_percent
    amount= principal
    values = []
    for i in range(years):
        values.append(amount)
        amount = amount*(1+rate) + contribution * 12 * (1 + match)

    return amount, values


def reinvest_dividend(principal, til_retire, rate, div_yield, contribution, variance):
    rate = rate - (variance**2)/2
    amount = principal
    values = []
    for i in range(til_retire*4):
        values.append(amount)
        amount = amount*(1+rate/4) + contribution * 3 + amount * div_yield
    
    return amount, values

def liveoff_dividend(principal, rate, div_yield, til_death, variance):
    rate = rate - (variance**2)/2
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

def sum_benefits_calc(four01k_principal, ira_principal, hsa_principal, four01k_contribution, ira_contribution, hsa_contribution, dividend_principal, dividend_contribution, dividend_yield, years, rate, variance):
    hsa_amount, hsa_values = definedbenefits_calc(hsa_principal, hsa_contribution, years, rate, variance)
    ira_amount, ira_values = definedbenefits_calc(ira_principal, ira_contribution, years, rate, variance)
    four01k_amount, four01k_values = definedbenefits_calc(four01k_principal, four01k_contribution, years, rate, variance)
    dividends_amount, dividends_values = reinvest_dividend(dividend_principal, years, rate, dividend_yield, dividend_contribution, variance)

    sum = hsa_amount + ira_amount + four01k_amount + dividends_amount
    sum_values = [hsa + ira + four01k + dividends for hsa, ira, four01k, dividends in zip(hsa_values, ira_values, four01k_values, dividends_values)]
    return sum, sum_values

def spend_benefits(principal, rate, ssi_years, til_retire, inflation, til_death, variance, dividend_yield, ssi, spend_rate):
    rate = rate - (variance**2)/2
    dividends_values = []
    ssi_values = []
    values = []
    dividends_values = liveoff_dividend(principal, rate, dividend_yield, til_death, variance)
    ssi_values = include_ssi(ssi_years, til_retire, inflation)
    for i in range(til_death):
        principal = principal*(1+rate) + ssi_values[i] + dividends_values[4 * i]- principal * spend_rate
        values.append(principal)
        if principal < 0:
            values.append(0)
            break

    return values


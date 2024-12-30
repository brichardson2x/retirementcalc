def years_retirement(begin, retire, death):
    til_retire = retire - begin
    til_death = death - retire

    return til_retire, til_death

def definedbenefits_calc(starting, contribution, years, rate, variance):
    rate = rate - (variance**2)/2
    return starting * (1 + rate)**years + contribution * ((1 + rate)**years - 1) / rate

def reinvest_dividend(begin, rate, div_yield, variance):
    ###

def liveoff_dividend(dividend, rate, div_yield, variance):
    ###

def include_ssi(death):
    
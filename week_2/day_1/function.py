def hello():
    '''print hello world '''
    print("Hello World!") 

hello() 






def country_info(country):
    '''print country name and capital'''
    if country == "USA":
        return "Country: USA, Capital: Washington D.C."
    elif country == "Naboo":
        return "the capital of Naboo is Theed"
    elif country == "France":
        return "Country: France, Capital: Paris"
    elif country == "Japan":
        return "Country: Japan, Capital: Tokyo"
    else:
        return "Country not found."


print(country_info("USA"))

class ExchangeRates: #creates ExchangeRates class

    def __init__(self, filename): #receives the name of the exchange rate file
        file = open(filename) #opens the csv file for reading
        lines = file.readlines() #reads all lines in the file and stores them in a list
        file.close() #closes the file
        #selects the USD/CAD exchange rate from the 27th column and row of the file 
        self.rate = float(lines[-1].split(",")[26]) #changes the rate from text to a decimal and saves it

    def convert(self, amount, base_cur, target_cur): #defines the convert method to convert between USD and CAD
        if base_cur == "USD" and target_cur == "CAD": #checks if the base currency is USD and the target currency is CAD
            return amount * self.rate #if true, returns the amount multiplied by the exchange rate
        elif base_cur == "CAD" and target_cur == "USD": #checks if the base currency is CAD and the target currency is USD
            return amount / self.rate #if true, returns the amount divided by the exchange rate
        else: #if the base and target currencies are the same or are neither CAD nor USD, raises an error
            raise ValueError("Invalid currency conversion") #stops the conversion if the inputted currency pair is invalid
        
print("") #formatting, blank line before title
print("Currency Converter") #title
print("") #formatting, blank line after title
base_cur = input("Step 1 | Enter your base currency (USD or CAD) in all CAPS: ") #uses input() to get the base currency (from)
target_cur = input("Step 2 | Enter your target currency (USD or CAD) in all CAPS: ") #uses input() to get the target currency (to)
amount = float(input("Step 3 | Enter the amount you'd like to convert: ")) #uses input() to get the amount to convert and converts it from text to a decimal
print("") #formatting, blank line before result
result = ExchangeRates("BankOfCanadaExchangeRate.2026.csv").convert(amount, base_cur, target_cur) #reads the rate and converts the amount using the convert() method of the ExchangeRates class
print(f"${amount:,.2f} {base_cur} is equal to ${result:,.2f} {target_cur}") #uses ,.2f to format the output to be rounded to the nearest penny, dollar sign and currency identifiers
print("") #formatting, blank line after result
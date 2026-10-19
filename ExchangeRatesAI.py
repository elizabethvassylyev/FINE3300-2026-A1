#This code is generated enitrely by AI
import csv
from decimal import Decimal, ROUND_HALF_UP

class ExchangeRates:
    CENT = Decimal("0.01")

    def __init__(self, exchange_rate_file):
        with open(exchange_rate_file, newline="", encoding="utf-8-sig") as csv_file:
            rows = list(csv.DictReader(csv_file))

        last_row = rows[-1]
        self.usd_cad_rate = Decimal(last_row["FXAUSDCAD"])
        self.rate_date = last_row["Date"]

    def convert(self, amount, base_currency, target_currency):
        amount = Decimal(str(amount)).quantize(
            self.CENT, rounding=ROUND_HALF_UP)
        base = base_currency.strip().upper()
        target = target_currency.strip().upper()

        if base == target:
            converted = amount
        elif base == "USD":
            converted = amount * self.usd_cad_rate
        else:  # CAD to USD
            converted = amount / self.usd_cad_rate

        return converted.quantize(self.CENT, rounding=ROUND_HALF_UP)

csv_path = r"C:\Users\LizaV\Downloads\BankOfCanadaExchangeRate.2026.csv"
rates = ExchangeRates(csv_path)

amount = input("Enter the amount: ")
base_currency = input("Enter the base currency (USD or CAD): ")
target_currency = input("Enter the target currency (USD or CAD): ")

converted = rates.convert(amount, base_currency, target_currency)
amount_display = Decimal(amount).quantize(
    ExchangeRates.CENT, rounding=ROUND_HALF_UP)

print(
    f"{base_currency.strip().upper()} ${amount_display:,.2f} = "
    f"{target_currency.strip().upper()} ${converted:,.2f} "
    f"(rate date: {rates.rate_date})")
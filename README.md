# FINE3300-2026-A1: Currency Converter

## Project Overview

This project converts currency amounts between United States dollars (USD) and Canadian dollars (CAD). It reads the latest USD/CAD exchange rate from the last row of the provided Bank of Canada CSV file, asks the user for their desired currencies and amount, and displays the result rounded to the nearest penny.

The project includes my independent solution for Part 1 (without the use of AI) and a separate AI-generated solution for Part 2. 

## Repository Link

https://github.com/elizabethvassylyev/FINE3300-2026-A1

## Project Files

- `ExchangeRates.py` - My solution for Part 1
- `ExchangeRatesAI.py` - The AI-generated solution for Part 2
- `BankOfCanadaExchangeRate.2026.csv` - Exchange-rate data
- `README.md` - Project description and results

## How It Works

Both programs define an `ExchangeRates` class and a `convert()` method. They use the latest USD/CAD rate of `1.3978` from the CSV file. The amount is multiplied by the rate for USD to CAD and divided by the rate for CAD to USD.

## Results

### My Code: $100,000 USD to CAD

```text
Currency Converter

Step 1 | Enter your base currency (USD or CAD) in all CAPS: USD
Step 2 | Enter your target currency (USD or CAD) in all CAPS: CAD
Step 3 | Enter the amount you'd like to convert: 100000

$100,000.00 USD is equal to $139,780.00 CAD
```

### My Code: $100,000 CAD to USD

```text
Currency Converter

Step 1 | Enter your base currency (USD or CAD) in all CAPS: CAD
Step 2 | Enter your target currency (USD or CAD) in all CAPS: USD
Step 3 | Enter the amount you'd like to convert: 100000

$100,000.00 CAD is equal to $71,540.99 USD
```

### AI Code: $100,000 USD to CAD

```text
Enter the amount: 100000
Enter the base currency (USD or CAD): USD
Enter the target currency (USD or CAD): CAD
USD $100,000.00 = CAD $139,780.00 (rate date: 2025-01-01)
```

### AI Code: $100,000 CAD to USD

```text
Enter the amount: 100000
Enter the base currency (USD or CAD): CAD
Enter the target currency (USD or CAD): USD
CAD $100,000.00 = USD $71,540.99 (rate date: 2025-01-01)
```

## AI Model/Vibe Coding

The model used for Part 2 was **ChatGPT Luna 6 on extra high effort**.

### Prompt

```
Listen to the following instructions and provide the code the me. Instructions: Open and view the structure of the csv exchange rate file. There are many currency parings listed but we are interested in the last row of USD/CAD conversion rates. Design a class (call it ExchangeRates) that takes an exchange rate file. Write a method/function (call it convert) that takes the amount and two currencies (USD or CAD) and converts from one currency to another using the exchange rate read from the file. You must ask the user for the specific amount and the base and target currency. Whether it's USD or CAD. Format your output (rounded to the nearest penny, dollar signs, and currency identifiers). Use any libraires and packages if needed. Use the input() function to prompt the user and read the entered values. We will assume that users will provide legitimate input values so no validation checks will be performed on the input values.
```

## Code Comparison

Both programs follow the main assignment requirements. They create an `ExchangeRates` class, read the latest USD/CAD exchange rate from the CSV file, ask the user for their desired exchange amount and currencies, and convert in both directions. They also produce the same answers for the two required $100,000 conversions.

My code is shorter and easier for me to understand. It uses `readlines()` to read the file, selects the exchange rate using column position `26`, and stores the rate as a `float`. It also checks specifically for USD to CAD and CAD to USD. If the user enters a different currency pair, my program displays an error.

The AI code is longer because it includes more features. Instead of finding the exchange rate by counting columns, it searches for the column named `FXAUSDCAD`. It uses `Decimal` to round money to the nearest penny and closes the file automatically. It also accepts lowercase currency entries, removes extra spaces, and shows the date of the exchange rate (meaning less user error and more accuracy in general). My code is simpler and easier to understand, while the AI code does a few extra things that are helpful, but aren't necessarily needed.

## References

- FINE 3300 (Fall 2026), Assignment #1 instructions, `FINE3300.F2026.A1.pdf`
- Bank of Canada, `BankOfCanadaExchangeRate.2026.csv`, provided through Canvas
- https://www.markdownguide.org/basic-syntax/
- https://cs.stanford.edu/people/nick/py/python-input.html

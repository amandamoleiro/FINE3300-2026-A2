
# FINE 3300 - Assignment #2

## Description

This project analyzes Canada's Consumer Price Index (CPI) using Python and monthly data from the Bank of Canada. The program reads the CPI data, calculates annual percentage changes, and creates a graph illustrating changes in the CPI and inflation over time.

An inflation calculator is also included to compare prices between two selected periods. Users can enter an original price along with the month and year for each period. The calculator uses the corresponding CPI values to determine the equivalent price, overall percentage change, and average annual inflation rate.

## Project Files

- **InflationCalculator.py**: Python program used to read and analyze CPI data, generate the graph, and run the inflation calculator.
- **STATIC_INFLATIONCALC.csv**: Monthly CPI data obtained from the Bank of Canada.
- **CPI_Graph.png**: Graph displaying CPI levels and annual percentage changes over time.
- **README.md**: Project overview, instructions, analysis, and sample output.


## How to Run the Program

1. **Download the project:** Download or clone the GitHub repository and save it to a folder on your computer.

2. **Open the project in Visual Studio Code:** Launch VS Code and select File > Open Folder. Choose the downloaded FINE3300-2026-A2 folder. Ensure that InflationCalculator.py and STATIC_INFLATIONCALC.csv are located in the same folder.

3. **Set up Python:** Ensure Python is installed and that the Python extension is enabled in VS Code. Select the appropriate Python interpreter using the interpreter selection menu.

4. **Install the required libraries:** Open the terminal in VS Code by selecting Terminal > New Terminal. Install Pandas, Matplotlib, and NumPy using the following command:

   ```bash
   python -m pip install pandas matplotlib numpy
   ```

5. **Run the Python program:** Open InflationCalculator.py and click the Run Python File button in the top-right corner of VS Code. The program will read the CPI dataset, calculate annual percentage changes, and save the graph as CPI_Graph.png.

6. **Enter the calculator inputs:** Once the program reaches the inflation calculator, enter the following information when prompted:
   - Original price of the goods or services in dollars
   - Starting year
   - Starting month (1-12)
   - Ending year
   - Ending month (1-12)

7. **View the results:** After all inputs have been entered, the program will display the CPI values for both dates, the equivalent price in the second period, the overall percentage change, the number of years between the dates, and the average annual inflation rate.

8. **View the CPI graph:** Open CPI_Graph.png from the project folder to view the graph showing historical CPI levels on the left axis and annual percentage changes on the right axis.

### Input Validation

The program checks that the original price is greater than zero and that both dates are available in the CPI dataset. Months must be between 1 and 12, and the selected dates must fall within the available data, from January 1914 to September 2026.

If an invalid price or date is entered, an error message will appear, and the program will prompt the user to enter a valid value.


## Consumer Price Index (CPI) Analysis

The dataset contains monthly CPI observations from January 1914 to September 2026. Annual percentage changes are calculated by comparing the CPI of each month with the corresponding month in the previous year.

### CPI Graph

![Canadian CPI and Annual Inflation](CPI_Graph.png)

### Observations

The graph shows a significant increase in Canada's CPI over time, particularly beginning in the 1970s. This reflects the long-term rise in the overall price level of goods and services.

Annual inflation has fluctuated throughout the period, with some of the largest increases and decreases occurring during the early twentieth century. Inflation was also relatively high during the 1970s and early 1980s.

A more recent increase in inflation occurred around 2021 and 2022, followed by a decline in the annual rate. However, CPI levels continued to rise, indicating that prices were still increasing, although at a slower rate.

## Inflation Calculator

The inflation calculator compares the cost of goods and services between two selected months and years using the corresponding CPI values.

The equivalent price is calculated as follows:

Equivalent Price = Original Price × (Second CPI / First CPI)

The calculator also determines the overall percentage change, the number of years between the selected dates, and the average annual inflation rate.

Input validation ensures that the original price is positive and that both dates fall within the available CPI data. Invalid entries prompt the user to enter new values.


## Sample Output

The following example compares the cost of $100 in September 2025 with September 2026.

### User Input

```text
Enter the original price ($): 100
Enter the first year: 2025
Enter the first month (1-12): 9
Enter the second year: 2026
Enter the second month (1-12): 9
```

### Calculator Output

```text
Original Price: $100.00 CAD
First Date: 2025 9
Second Date: 2026 9
CPI for the first date: 164.9
CPI for the second date: 170.0
Equivalent Price: $103.09 CAD
Percentage Change: 3.09%
Number of Years: 1.00
Average Annual Inflation Rate: 3.09%
```

Based on the CPI values, goods costing $100 in September 2025 would cost approximately $103.09 in September 2026, representing a 3.09% increase over the year.


## References

- Bank of Canada. Inflation Calculator.
  https://www.bankofcanada.ca/rates/related/inflation-calculator/
- Statistics Canada. Consumer Price Index.
  https://www.statcan.gc.ca/en/subjects-start/prices_and_price_indexes/consumer_price_indexes
- Mastrodomenico, R. (2022). The Python Book. Wiley.
- FINE 3300: Python for Finance Professionals, Fall 2026 lecture materials.


# FINE 3300 - Assignment #2
# Consumer Price Index Inflation Calculator

import pandas as pd
import matplotlib.pyplot as plt

# Read the CPI data from the CSV file
cpi_data = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)

# Display the first five rows
print(cpi_data.head(5))


# Keep only the regular monthly observations
cpi_data = cpi_data[cpi_data["date"].str.endswith("-01")].copy()

# Reset the row numbers after filtering
cpi_data = cpi_data.reset_index(drop=True)

# Display the number of monthly observations
print("Number of observations:", len(cpi_data))

# Display the last five rows
print(cpi_data.tail(5))


# Create a list to store annual percentage changes
annual_changes = []

# Calculate annual CPI changes
for i in range(len(cpi_data)):

    if i < 12:
        annual_changes.append(None)

    else:
        current_cpi = cpi_data["STATIC_INFLATIONCALC"].iloc[i]
        previous_cpi = cpi_data["STATIC_INFLATIONCALC"].iloc[i - 12]

        change = ((current_cpi / previous_cpi) - 1) * 100

        annual_changes.append(change)

# Add the annual changes as a new column
cpi_data["Annual Change (%)"] = annual_changes

# Display the last five rows
print(cpi_data.tail(5))


# Convert the date column into a date format
cpi_data["date"] = pd.to_datetime(cpi_data["date"])


# Create the CPI graph
fig, ax1 = plt.subplots(figsize=(11, 6))

# Plot CPI using the left axis
ax1.plot(cpi_data["date"], cpi_data["STATIC_INFLATIONCALC"],
         color="blue", label="Consumer Price Index")

# Add the CPI base level
ax1.axhline(y=100, linestyle=":", color="gray",
            label="Base Level (2002 = 100)")

ax1.set_xlabel("Year")
ax1.set_ylabel("CPI")

# Plot annual inflation using the right axis
ax2 = ax1.twinx()
ax2.plot(cpi_data["date"], cpi_data["Annual Change (%)"],
         color="red", label="Annual Percentage Change")

ax2.set_ylabel("Annual Percentage Change (%)")

# Add the title and legends
ax1.set_title("Canadian Consumer Price Index and Annual Inflation")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Save the graph
plt.tight_layout()
plt.savefig("CPI_Graph.png")



# Inflation Calculator

# Ask for a valid price
while True:
    try:
        original_price = float(input("Enter the original price ($): "))

        if original_price > 0:
            break
        else:
            print("Please enter a price greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# Ask for a valid starting date
while True:
    try:
        year1 = int(input("Enter the first year: "))
        month1 = int(input("Enter the first month (1-12): "))

        if month1 < 1 or month1 > 12:
            print("Invalid month. Please enter a number from 1 to 12.")
            continue

        date1 = pd.Timestamp(year1, month1, 1)

        # Check if the date is available in the CPI data
        first_period = cpi_data[cpi_data["date"] == date1]

        if first_period.empty:
            print("CPI data is not available for this date. Try again.")
        else:
            break

    except (ValueError, OverflowError):
        print("Invalid date. Please enter a valid year and month.")


# Ask for a valid ending date
while True:
    try:
        year2 = int(input("Enter the second year: "))
        month2 = int(input("Enter the second month (1-12): "))

        if month2 < 1 or month2 > 12:
            print("Invalid month. Please enter a number from 1 to 12.")
            continue

        date2 = pd.Timestamp(year2, month2, 1)

        # Check if CPI data is available for this date
        second_period = cpi_data[cpi_data["date"] == date2]

        if second_period.empty:
            print("CPI data is not available for this date. Try again.")
        else:
            break

    except (ValueError, OverflowError):
        print("Invalid date. Please enter a valid year and month.")


# Display the entered values
print("Original Price: ${:,.2f} CAD".format(original_price))
print("First Date:", year1, month1)
print("Second Date:", year2, month2)


# Get the CPI value for each period
cpi1 = first_period["STATIC_INFLATIONCALC"].iloc[0]
cpi2 = second_period["STATIC_INFLATIONCALC"].iloc[0]

# Display the CPI values
print("CPI for the first date:", cpi1)
print("CPI for the second date:", cpi2)


# Calculate the price of the same goods in the second period
new_price = original_price * (cpi2 / cpi1)

# Calculate the overall percentage change in prices
percent_change = ((cpi2 / cpi1) - 1) * 100

# Calculate the number of months and years between the two dates
months = abs((year2 - year1) * 12 + (month2 - month1))
years = months / 12

# Calculate the average annual inflation rate
if years == 0:
    annual_rate = 0
else:
    annual_rate = ((cpi2 / cpi1) ** (1 / years) - 1) * 100


# Display the results
print("Equivalent Price: ${:,.2f} CAD".format(new_price))
print("Percentage Change: {:.2f}%".format(percent_change))
print("Number of Years: {:.2f}".format(years))
print("Average Annual Inflation Rate: {:.2f}%".format(annual_rate))

# Display the CPI graph after the calculator results
plt.show()


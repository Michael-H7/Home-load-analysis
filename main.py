import numpy as np
import matplotlib.pyplot as plt


def calculate_loan_amount(weekly_repayment, annual_interest_rate, years):
    """
    Calculates the maximum loan amount based on weekly repayments, interest rate, and loan term.
    """
    if annual_interest_rate <= 0 or weekly_repayment <= 0 or years <= 0:
        return 0

    # Convert annual interest rate to a weekly rate
    weekly_interest_rate = (annual_interest_rate / 100) / 52
    # Total number of weeks
    total_weeks = years * 52

    # Using the present value of an ordinary annuity formula
    # P = R * [1 - (1 + i)^-n] / i
    # where:
    # P = Principal loan amount
    # R = Periodic repayment (weekly)
    # i = interest rate per period (weekly)
    # n = total number of payments
    if weekly_interest_rate > 0:
        loan_amount = (
            weekly_repayment
            * (1 - (1 + weekly_interest_rate) ** -total_weeks)
            / weekly_interest_rate
        )
    else:
        loan_amount = weekly_repayment * total_weeks

    return loan_amount


def create_loan_scenario_plot(max_weekly_repayment, annual_interest_rate):
    """
    Creates a plot showing the relationship between loan term and loan amount for a fixed weekly repayment.
    """
    years = np.arange(5, 31)  # Loan terms from 5 to 30 years
    loan_amounts = [
        calculate_loan_amount(max_weekly_repayment, annual_interest_rate, year)
        for year in years
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(years, loan_amounts, marker="o", linestyle="-")
    plt.title(
        f"Loan Amount vs. Loan Term for a Weekly Repayment of ${max_weekly_repayment}"
    )
    plt.xlabel("Loan Term (Years)")
    plt.ylabel("Maximum Loan Amount ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("loan_scenario_plot.png")

    return loan_amounts, years


# --- User Inputs ---
# You can change these values to explore different scenarios
max_weekly_repayment_input = 671  # Your maximum affordable weekly repayment
# Based on research, a typical interest rate is around 5.5%. You can adjust this.
interest_rate_input = 5.5

# Generate and save the plot
loan_amounts, years = create_loan_scenario_plot(
    max_weekly_repayment_input, interest_rate_input
)

# Display a summary of the data
print("Loan Amount vs. Loan Term")
print("-------------------------")
for year, amount in zip(years, loan_amounts):
    print(f"Year {year}: ${amount:,.2f}")


plt.show()

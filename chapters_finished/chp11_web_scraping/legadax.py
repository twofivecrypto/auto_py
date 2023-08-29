
def calculate_startup_value(investment_amount_one, stake_percentage, stage):
    pre_seed_valuation = 0  # Pre-seed valuation: $0
    seed_valuation = 50000  # Seed valuation: $50,000
    series_a_valuation = 1000000  # Series A valuation: $1,000,000

    if stage == "pre_seed":
        startup_value = pre_seed_valuation + investment_amount_one / stake_percentage
    elif stage == "seed":
        startup_value = seed_valuation + investment_amount_one / stake_percentage
    elif stage == "series_a":
        startup_value = series_a_valuation + investment_amount_one / stake_percentage
    else:
        print("Invalid stage provided.")
        return None

    return startup_value

investment_amount_one = 50000
stake_percentage = 0.1
stage = "pre_seed"


startup_value = calculate_startup_value(investment_amount_one, stake_percentage, stage)
if startup_value is not None:
    print("Startup value:", startup_value)


def calculate_gender_pay_gap(df, mapping):
    """Calculate the gender pay gap (percentage)."""
    means = df.groupby(mapping["gender"])["pay_level"].mean()

    avg_male = means.get("M", float("nan"))
    avg_female = means.get("F", float("nan"))

    return ((avg_male - avg_female) / avg_male) * 100


def calculate_variable_gender_pay_gap(df, mapping):
    """Calculate the gender pay gap in variable components (percentage)."""
    means = df.groupby(mapping["gender"])["variable_pay_level"].mean()

    avg_male = means.get("M", float("nan"))
    avg_female = means.get("F", float("nan"))

    return ((avg_male - avg_female) / avg_male) * 100

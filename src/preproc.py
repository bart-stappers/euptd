import pandas as pd


def build_pay_level(df, mapping):
    """Construct a pay level column as the gross annual pay (in cash and in kind)."""
    df = df.copy()

    monthly = pd.to_numeric(df[mapping["monthly"]], errors="coerce")
    vacation = pd.to_numeric(df[mapping["vacation"]], errors="coerce")
    bonus = pd.to_numeric(df[mapping["bonus"]], errors="coerce")
    car = pd.to_numeric(df[mapping["car"]], errors="coerce")

    df["pay_level"] = 12 * monthly + vacation + bonus + car
    return df


def build_variable_pay_level(df, mapping):
    """Construct a variable pay level column.

    Comprises the gross annual pay from complementary and variable components.
    """
    df = df.copy()

    bonus = pd.to_numeric(df[mapping["bonus"]], errors="coerce")
    car = pd.to_numeric(df[mapping["car"]], errors="coerce")

    df["variable_pay_level"] = bonus + car
    return df

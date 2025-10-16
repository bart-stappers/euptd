import streamlit as st
import pandas as pd

from src.preproc import build_pay_level
from src.preproc import build_variable_pay_level
from src.statistics import calculate_gender_pay_gap
from src.statistics import calculate_variable_gender_pay_gap


def set_page_config():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="EU Pay Transparency Directive Tool",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def read_data():
    """Read Excel input file from file uploader UI."""
    st.header("Data")
    file = st.file_uploader(
        "Choose an Excel file (.xlsx)", type=["xlsx"], accept_multiple_files=False
    )
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(df.head(10), width="stretch")
        return df
    else:
        st.warning("Please upload an Excel file to proceed.")
        return None


def column_mapping(df):
    """Render column mapping UI and return chosen names."""
    st.header("Column mapping")
    cols = list(df.columns)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender_col = st.selectbox("Gender (M/F)", options=cols)
        monthly_col = st.selectbox("Monthly pay (EUR)", options=cols)
    with col2:
        scale_col = st.selectbox("Scale (11-20)", options=cols)
        vacation_col = st.selectbox("Vacation allowance (EUR)", options=cols)
    with col3:
        fte_col = st.selectbox("FTE (0-1)", options=cols)
        bonus_col = st.selectbox("Bonus (EUR)", options=cols)
    with col4:
        sales_col = st.selectbox("Sales (0/1)", options=cols)
        car_col = st.selectbox("Car (EUR)", options=cols)

    mapping = {
        "gender": gender_col,
        "scale": scale_col,
        "fte": fte_col,
        "sales": sales_col,
        "monthly": monthly_col,
        "vacation": vacation_col,
        "bonus": bonus_col,
        "car": car_col,
    }
    return mapping


def render_statistics(df, mapping):
    """Render required statistics"""
    st.header("Unadjusted pay transparency statistics")

    df = build_pay_level(df, mapping)
    df = build_variable_pay_level(df, mapping)

    gpg = calculate_gender_pay_gap(df, mapping)
    st.metric("Gender pay gap", f"{gpg:.2f}%")

    var_gpg = calculate_variable_gender_pay_gap(df, mapping)
    st.metric(
        "Gender pay gap in complementary or variable components", f"{var_gpg:.2f}%"
    )

    return df

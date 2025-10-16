from src.app import set_page_config
from src.app import read_data
from src.app import column_selection


def main():
    """Run Streamlit app"""
    set_page_config()

    df = read_data()
    if df is None:
        return

    mapping = column_selection(df)
    if mapping is None:
        return


if __name__ == "__main__":
    main()

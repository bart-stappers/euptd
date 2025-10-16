from src.app import set_page_config
from src.app import read_data
from src.app import column_mapping
from src.app import render_statistics


def main():
    """Run Streamlit app"""
    set_page_config()

    df = read_data()
    if df is None:
        return

    mapping = column_mapping(df)
    if mapping is None:
        return

    stats = render_statistics(df, mapping)
    if stats is None:
        return


if __name__ == "__main__":
    main()

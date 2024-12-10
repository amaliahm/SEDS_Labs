import streamlit as st
import datetime

def date_range_selector():
    st.sidebar.header("Date Range Selector")

    min_date = datetime.date(2020, 1, 1)
    max_date = datetime.date(2024, 10, 31)
    
    start_date = st.sidebar.date_input(
        "Select Start Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date,
        key="start_date"
    )

    end_date = st.sidebar.date_input(
        "Select End Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date,
        key="end_date"
    )

    if start_date > end_date:
        st.sidebar.error("Start date cannot be after the end date. Please select valid dates.")
    else:
        if st.sidebar.button("Fetch Data"):
            return start_date, end_date

    return None, None

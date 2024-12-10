import streamlit as st

def select_and_plot_columns(data):
    if data is None or data.empty:
        st.warning("No data available to display. Please load data first.")
        return

    st.subheader("Column Selector for Line Chart")

    # x_axis = st.selectbox(
    #     "Select column for X-axis", 
    #     data.columns, 
    #     key="x_axis",
    #     index=0
    # )
    # y_axis = st.selectbox(
    #     "Select column for Y-axis", 
    #     data.columns, 
    #     key="y_axis",
    #     index=1
    # )
    # st.subheader("Line Chart")
    # st.line_chart(
    #     data=data,
    #     x=x_axis,
    #     y=y_axis,
    #     use_container_width=True
    # )


    st.subheader("Line Chart")
    st.line_chart(
        data=data,
        x='open',
        y='close',
        use_container_width=True
    )

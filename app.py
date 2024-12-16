import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go

db=DB()

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()
    with col1:

        source = st.selectbox('Source', sorted(city))

    with col2:

        dest = st.selectbox('Destination', sorted(city))


#     button
    if st.button('Search'):
        results = db.fetch_all_flights(source, dest)
        st.dataframe(results)

elif user_option == 'Analytics':
    st.title('Analytics')
    # pie chart

    airline, freq = db.fetch_airline_freq()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=freq,
            hoverinfo='label+percent',
            textinfo='value'
        )
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)

    # Bar

    city, freq = db.fetch_airline_freq()
    fig = go.Figure(
        go.Bar(
            x=city,
            y=freq,

        )
    )
    st.header("Bar Chart")
    st.plotly_chart(fig)

#     line chart

    date, freq = db.flights_per_day()
    fig = go.Figure(
        go.Line(
            x=date,
            y=freq
        )
    )
    st.header('Line Chart')
    st.plotly_chart(fig)

else:
    st.title("Welcome To The Flight Analytical Dashboard")
    st.subheader('< Explore Sidebar')

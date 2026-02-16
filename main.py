import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import plotly.express as px
from app.utils import fetch_coordinates
from app.feature_engineering import get_forecast_dataframe
from app.model import load_model, predict_aqi

# -------------------------------
# App configuration
# -------------------------------
st.set_page_config(
    page_title="AQI Forecast Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌿 AQI Prediction & Analysis Dashboard")
st.write("Predicting Air Quality Index for the next 3 days and visualizing recent trends.")

# -------------------------------
# Load model
# -------------------------------
MODEL_PATH = "model_registry/random_forest_retrained.pkl"
model = load_model(MODEL_PATH)

# -------------------------------
# Fetch coordinates
# -------------------------------
with st.spinner("Fetching your location..."):
    try:
        latitude, longitude = fetch_coordinates()
        st.success(f"Location fetched: Latitude {latitude}, Longitude {longitude}")
    except Exception as e:
        st.error(f"Error fetching coordinates: {e}")
        st.stop()

# -------------------------------
# Feature extraction & prediction
# -------------------------------
forecast_features = get_forecast_dataframe()
predictions = predict_aqi(model, forecast_features)

# Ensure predictions are in DataFrame format
if not isinstance(predictions, pd.DataFrame):
    predictions = pd.DataFrame(predictions, columns=['predicted_aqi', 'temperature', 'humidity', 'wind_speed'])

# Add dates
today = datetime.now().date()
predictions['Date'] = [today + timedelta(days=i+1) for i in range(len(predictions))]

# -------------------------------
# Sidebar controls
# -------------------------------
st.sidebar.header("Controls")
show_advanced_charts = st.sidebar.checkbox("Show Advanced Charts", True)
aqi_metric_view = st.sidebar.checkbox("Show AQI Metrics", True)

# -------------------------------
# Display predictions as metrics
# -------------------------------
if aqi_metric_view:
    st.subheader("📊 AQI Predictions for Next 3 Days")
    cols = st.columns(3)
    for i, row in predictions.iterrows():
        aqi = row['predicted_aqi']
        temp = row['temperature']
        hum = row['humidity']
        wind = row['wind_speed']

        # AQI color coding
        if aqi <= 50:
            color = "green"
        elif aqi <= 100:
            color = "yellow"
        elif aqi <= 150:
            color = "orange"
        elif aqi <= 200:
            color = "red"
        else:
            color = "purple"

        with cols[i]:
            st.metric(
                label=str(row['Date']),
                value=f"{aqi} AQI",
                delta=f"Temp: {temp}°C | Hum: {hum}% | Wind: {wind} m/s"
            )
            st.markdown(f"<div style='width:100%; height:10px; background-color:{color};'></div>", unsafe_allow_html=True)

# -------------------------------
# Load historical data
# -------------------------------
@st.cache_data
def load_data():
    try:
        data = pd.read_csv("processed_data.csv")
        data['timestamp'] = pd.to_datetime(data[['year', 'month', 'day']])
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

data = load_data()

# -------------------------------
# Historical AQI Analysis
# -------------------------------
if not data.empty:
    daily_data = data.groupby('timestamp', as_index=False)['aqi'].mean()
    latest_timestamp = daily_data['timestamp'].max()
    past_30_days_data = daily_data[daily_data['timestamp'] >= (latest_timestamp - pd.Timedelta(days=30))]

    st.subheader("📈 AQI Trends Over the Last 30 Days")
    
    if show_advanced_charts:
        # Interactive Plotly Line Chart
        fig = px.line(
            past_30_days_data,
            x='timestamp',
            y='aqi',
            title="Daily Average AQI (Last 30 Days)",
            markers=True,
            labels={"timestamp": "Date", "aqi": "AQI"}
        )
        fig.update_traces(line=dict(color="firebrick", width=3))
        fig.update_layout(xaxis_title="Date", yaxis_title="AQI", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
    else:
        # Streamlit native line chart
        st.line_chart(past_30_days_data.set_index('timestamp')['aqi'])

    # Optional: histogram of AQI levels
    st.subheader("📊 AQI Level Distribution")
    fig2 = px.histogram(
        past_30_days_data,
        x='aqi',
        nbins=10,
        title="AQI Frequency in Last 30 Days",
        color_discrete_sequence=['teal']
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No historical data available to display.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Made with ❤️ using **Streamlit** | AQI Dashboard")

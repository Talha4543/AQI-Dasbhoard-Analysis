🌫️ Islamabad AQI Forecasting Dashboard – Next 3 Days
=====================================================
![AQI Dashboard](AQI%20Dashboard.png)

Predict the **Air Quality Index (AQI)** for **Islamabad** over the next 3 days using a **serverless machine learning pipeline**. This project includes automated data collection, feature engineering, model training, and real-time predictions displayed through an interactive dashboard.

**Project Repo:** [GitHub – AQI Dashboard Analysis](https://github.com/Talha4543/AQI-Dasbhoard-Analysis)

🚀 Project Overview
-------------------

This system allows you to:

*   Collect **real-time weather and pollutant data** (PM2.5, PM10, NO₂, CO, SO₂, O₃) for Islamabad via **AQICN** or **OpenWeather APIs**
    
*   Process raw data into **engineered features** ready for ML models
    
*   Train and evaluate multiple AQI forecasting models
    
*   Provide **interactive predictions** for the next 3 days
    
*   Understand predictions using **SHAP** for feature importance
    

> ✅ All features are handled using **CSV files**, without Hopsworks.

🧩 Features
-----------

### 📊 Data Pipeline

*   Fetch pollutant and weather data for **Islamabad**
    
*   Compute **time-based features**: hour, day, month
    
*   Derive **AQI trends**, delta rates, and rolling averages
    
*   Store processed features in **CSV files**
    

### ⚙️ Model Training

*   Train models on historical data from Islamabad:
    
    *   Random Forest
        
    *   Ridge Regression
        
    *   TensorFlow Neural Network
        
*   Evaluate with **RMSE, MAE, R²**
    
*   Save trained models locally (models/ folder)
    

### 🚀 Automation

*   Feature pipeline runs **hourly**
    
*   Training pipeline runs **daily**
    
*   Orchestrated via **GitHub Actions** or **Airflow**
    

### 🖥️ Dashboard

*   Interactive **Streamlit dashboard** for Islamabad AQI predictions
    
*   Visualizes historical trends and forecasts for 3 days
    
*   Compares multiple model predictions
    
*   Sends alerts for hazardous AQI levels
    

### 🧠 Explainability

*   **SHAP** used to explain model predictions
    
*   Identify most important factors impacting AQI in Islamabad
    

🗂️ Repository Structure
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   AQI-Dasbhoard-Analysis/  ├── data/  │   ├── islamabad_weather.csv  │   ├── islamabad_pollutants.csv  │   └── islamabad_aqi_targets.csv  ├── models/  │   ├── random_forest.pkl  │   └── neural_network.h5  ├── pipelines/  │   ├── feature_pipeline.py  │   └── training_pipeline.py  ├── dashboard/  │   ├── streamlit_app.py  │   └── api_server.py  ├── requirements.txt  └── README.md   `

⚡ How to Run (Islamabad Edition)
--------------------------------

1️⃣ Clone the repository:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/Talha4543/AQI-Dasbhoard-Analysis.git  cd AQI-Dasbhoard-Analysis   `

2️⃣ Install dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

3️⃣ Generate features for Islamabad:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python pipelines/feature_pipeline.py   `

4️⃣ Train models on Islamabad data:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python pipelines/training_pipeline.py   `

5️⃣ Launch the interactive dashboard:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run dashboard/streamlit_app.py   `

> Visit http://localhost:8501 to view AQI forecasts for Islamabad.

🧪 Example Predictions for Islamabad
------------------------------------

DayPredicted AQICategoryDay 1190UnhealthyDay 2210Very UnhealthyDay 3175Unhealthy

_(Values update dynamically as new data is fetched.)_

📈 Sample Model Metrics
-----------------------

ModelRMSEMAER²Random Forest10.27.80.92Neural Network8.56.30.94

🛠️ Tech Stack
--------------

LayerToolsDataPython, Pandas, AQICN API, OpenWeather APIMLScikit-learn, TensorFlowAutomationGitHub Actions / Apache AirflowDashboardStreamlit + FlaskExplainabilitySHAPVersion ControlGit

📌 Contributions
----------------

Contributions are welcome! Ideas for improvement:

*   Multi-city AQI forecasting across Pakistan
    
*   Cloud deployment for real-time access
    
*   Push notifications for hazardous AQI alerts
    

📖 References
-------------

*   AQICN API: [https://aqicn.org/api/](https://aqicn.org/api/)
    
*   OpenWeather API: [https://openweathermap.org/api](https://openweathermap.org/api)
    
*   SHAP Library: [https://shap.readthedocs.io](https://shap.readthedocs.io)

# 🌤️ Weather Predictor

A simple **Weather Prediction Web App** built using **Streamlit** and a **Keras deep learning model**.  
The app predicts the type of weather (Drizzle, Fog, Rain, Snow, or Sun) based on user inputs such as precipitation, temperature, and wind speed.  

## 🚀 Features
- Interactive **Streamlit UI**
- Takes user input: precipitation, maximum temperature, minimum temperature, and wind speed
- Predicts weather conditions:
  - 🌧️ Drizzle
  - 🌫️ Fog
  - ☔ Rain
  - ❄️ Snow
  - ☀️ Sun
- Shows model accuracy (**82.60%**)

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (for the frontend web app)
- **TensorFlow/Keras** (for the trained ML model)
- **NumPy**

## 📂 Project Structure
├── weather_pred.h5 # Trained Keras model
├── app.py # Streamlit app script
├── requirements.txt # Dependencies
└── README.md # Project documentation

📊 Model Information

The model was trained on weather data.

Achieved 82.60% accuracy on test data.

Output classes:
{0: 'drizzle', 1: 'fog', 2: 'rain', 3: 'snow', 4: 'sun'}

📜 License

This project is licensed under the MIT License – feel free to use and modify it.

📸 Demo<img width="1919" height="837" alt="Screenshot 2025-09-21 202156" src="https://github.com/user-attachments/assets/763cd5cf-81da-4ea6-b17f-c0f8ac1cedf7" />

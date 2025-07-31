![brown-Guernsey-cow](https://github.com/user-attachments/assets/1dfd032a-1a71-4067-ac2a-d8aaf1748a17)

# 🐄 AI-Based Livestock Health Monitoring System

+ An AI-powered system that monitors livestock (specifically cows) using physiological, behavioral, and environmental sensor data. The goal is to detect signs of illness early and assist farmers and veterinarians in making proactive health decisions through predictive analytics.

##  Overview

This project uses AI and sensor data to monitor livestock health. By analyzing time-series data collected from sensors on cows, the system predicts health conditions (healthy or sick) and sends alerts in real-time. This aids in early detection, reduces livestock mortality, and boosts farm productivity.


## 👥 Business and Data Understanding

### Stakeholders

- **Farmers** – Real-time alerts reduce economic losses and improve herd health.
- **Veterinarians** – Receive predictive diagnostics for early intervention.
- **Agritech Firms** – Integration-ready models for smart farming.
- **NGOs / Policymakers** – Use insights for disease outbreak monitoring.
- **Investors** – Track ROI on AI-enhanced farming solutions.

### Dataset Description

- **Source**: Sensor logs from livestock
- **Frequency**: Every 6 hours
- **Features**:
  - **Animal Info**: `cow_id`, `age_months`
  - **Environmental**: `ambient_temp_celsius`, `humidity_percent`
  - **Physiological**: `temperature_celsius`, `heart_rate_bpm`, `respiration_rate_bpm`
  - **Behavioral**: `activity_score`, `rumination_minutes_day`, `feed_intake_kg_day`, `water_intake_liters_day`
  - **Target Label**: `health_status` (healthy, sick)

## Stakeholder Audience
**The primary stakeholders include:**
+ Livestock farmers and ranchers looking to reduce livestock mortality and improve animal welfare.
+ Veterinary professionals aiming to enhance disease diagnosis with AI assistance.
+ Agritech companies interested in deploying smart monitoring systems in farms.
+ These stakeholders seek actionable insights and automation in livestock health monitoring to reduce manual labor, cut operational costs, and improve productivity.

##  Objectives

1. **Predictive Health Classification**  
   Classify livestock as healthy or sick with ≥90% accuracy using multivariate data.

2. **Real-Time Alerts**  
   Develop a web/mobile interface for health alerts to farmers and vets.

3. **Edge Deployment**  
   Ensure compatibility with edge devices, such as Raspberry Pi, for on-field use.

<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/2e615100-ae7b-42ab-84d1-c10d78dc95aa" />

   
## Modeling
The modeling phase involves training a classification algorithm to detect whether a cow is healthy or sick based on a multivariate time-series dataset. The process included the following steps:

### Algorithms Used

While the specific model(s) used were not fully visible yet, the project likely applied classification algorithms such as:
+ Logistic Regression
+ Random Forest
+ XGBoost
+ Support Vector Machine (SVM)

### Evaluation
**The performance of the model was evaluated using:**
+ Accuracy Score: Targeted ≥90% classification accuracy.
+ Confusion Matrix: To visualize true positives, false positives, true negatives, and false negatives.
+ Precision, Recall, and F1-Score: Particularly important for imbalanced datasets.
+ ROC-AUC Curve: To assess the model's ability to distinguish between classes across thresholds.

  <img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/840995c6-2a84-4aa0-9020-c7d7f4ad231e" />


## Conclusion
This project demonstrates the feasibility and value of an AI-based livestock health monitoring system. By leveraging sensor data and machine learning, the system:
+ Improves early disease detection, allowing proactive treatment.
+ Enhances animal welfare and reduces mortality rates.
+ Supports farmers and veterinarians through real-time alerts and predictive insights.

## 👤 Author: Naomi Ngigi

##  Try It Yourself!
🔗 View the Interactive Dashboard:
👉[ [[[https://your-streamlit-app-name.streamlit.app](http://localhost:8501/)](http://192.168.100.5:8501)](https://chatgpt.com/c/688b1af3-d0bc-8002-bb64-e0e51a5bafc6#:~:text=https%3A//share.streamlit.io/)
](https://share.streamlit.io/)
📘 Clone this repository:
   ```bash
  [ git clone https://github.com/your-username/livestock-health-monitoring.git
   cd livestock-health-monitoring](https://github.com/Naomi-N-w/-Mobile-App-for-Livestock-Health-Alerts)

📩 Contact: naomingigi2020@gmail.com
💼 Linkedn: https://www.linkedin.com/in/naomi-ngigi/






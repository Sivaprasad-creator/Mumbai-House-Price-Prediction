
# 🏙️ Mumbai House Price Prediction

![image alt](https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction/blob/34f29cb2779f232673ad3dda3003523924a10c46/House%20price.jpg)

## 📌 Project Overview

This project predicts **property prices in Mumbai** using various regression algorithms and explores clustering to segment the housing market. It helps understand key drivers of price and provides an interactive **Streamlit web app** for instant predictions.

> 🔧 **Tools Used:** Python, Machine Learning, Clustering, Power BI, Streamlit

---

## 📁 Dataset Information

- **Source:** [Kaggle Mumbai House Data](https://www.kaggle.com/datasets/tilakjain/mumbai-house-data)  
- **Records:** 76,038+
- **Key Columns:**
  - `bhk` — Number of bedrooms, halls, and kitchens  
  - `type` — Property type (apartment, villa, etc.)  
  - `locality` — Area or neighborhood  
  - `area` — Size in square feet  
  - `region` — Geographic zone in Mumbai  
  - `price` — Property price in INR  
  - `status` — Construction stage (ready, under construction, etc.)

---

## 🎯 Objectives

- Predict house prices for new or custom inputs  
- Understand which factors impact pricing the most  
- Segment properties into clusters for market analysis  
- Build an interactive prediction app using Streamlit  
- Perform visual exploration of housing trends in Power BI

---

## Dashboard Preview

![image alt](https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction/blob/f72488139bac3a0bbf3c38a2e66491335f9303c2/House%20Price%20Dashboard.png)

---

## 📈 Power BI Dashboard Insights

- 📊 **Average Metrics**  
  - Average Price, Average Square Foot Area, ROI Calculation  
  - ROI Volatility and Spread (for investment outlook)

- 🧱 **Price Summaries by Category**  
  - Sum of Prices by `status` *(Ready to Move, Under Construction)*  
  - Sum of Prices by `bhk` *(1 BHK, 2 BHK, etc.)*  
  - Sum of Prices by `type` *(Apartment, Villa, etc.)*

- 🌍 **Top Trends**  
  - Top 5 Localities by **Average Price**  
  - Top 5 Regions by **Total Price Value**

- 📋 **Tabular Overview**  
  - Table combining:  
    - `locality`, `region`, `bhk`, `age` *(New, Resale, Unknown)*, `status`  
    - Sum of `price` for each grouping

> 📌 Power BI helps identify premium regions, demand clusters, construction status insights, and investment-worthy localities.

---

## 📊 Analysis Summary

- **EDA:** Visualized distributions, outliers, and correlations  
- **Feature Engineering:** Encoded categorical variables and scaled numeric features  
- **Model Training:** Applied and compared multiple regressors  
- **Clustering:** Grouped properties by similar price behavior  
- **Insights:** Found key patterns affecting Mumbai housing prices

---

## 🤖 Models Used

| Step                   | Libraries & Techniques                                                                                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Preprocessing**      | `pandas`, `numpy`, `seaborn`, `matplotlib`, `warnings`                                                                        |
| **Regression Models**  | `LinearRegression`, `Ridge`, `Lasso`, `DecisionTreeRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`, `XGBRegressor` |
| **Clustering Models**  | `MiniBatchKMeans`, `GaussianMixture`                                                                                          |
| **Evaluation**         | `mean_absolute_error`, `mean_absolute_percentage_error`, `mean_squared_error`, `r2_score`                                      |
| **Optimization**       | `GridSearchCV`, `cross_val_score`                                                                                             |
| **Deployment**         | **Streamlit** web app for real-time prediction and cluster exploration                                                         |

---

## 🚀 Streamlit Deployment

This project includes a **Streamlit web app** where you can:

- Input property details (BHK, type, area, region, locality)
- Instantly predict the estimated price  
- Visualize similar property prices  
- Explore market segmentation with clustering  

---

## Deployment Preview

![image alt](https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction/blob/8133f1cf2f61500d8b094bacfbd01064ddef41b2/Deployment1.png)

![image alt](https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction/blob/8133f1cf2f61500d8b094bacfbd01064ddef41b2/Deployment2.png)

![image alt](https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction/blob/8133f1cf2f61500d8b094bacfbd01064ddef41b2/Deployment3.png)

---

## 🛠️ How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sivaprasad-creator/Mumbai-House-Price-Prediction.git
   cd Mumbai-House-Price-Prediction
   ```

2. **Create and Activate Virtual Environment (optional but recommended)**  
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

---

## 📬 Author Info

**Sivaprasad T.R**  
📧 Email: sivaprasadtrwork@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sivaprasad-t-r)  
💻 [GitHub](https://github.com/Sivaprasad-creator)

---

## 📜 Data Source

Data sourced from: [Kaggle - Mumbai House Data](https://www.kaggle.com/datasets/tilakjain/mumbai-house-data)

---

## 🙏 Acknowledgements

Thanks to Kaggle and the dataset contributors for making this data publicly available.

---

## 💬 Feedback

Feel free to open issues or reach out for improvements, suggestions, or collaboration!

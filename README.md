# 🏡 Airbnb Data Analysis and Visualization

A comprehensive data analysis project designed to explore Airbnb listing data through MongoDB Atlas, Python, Streamlit, and visualization tools like Tableau or Power BI. This project enables stakeholders to gain insights into pricing trends, seasonal availability, and location-based booking patterns in the travel and tourism industry.

---

## 📌 Project Objective

To analyze Airbnb listings using Python and MongoDB, clean and process the dataset, and create interactive visualizations and dashboards that provide meaningful insights into:

- Pricing trends by location, season, and property type
- Availability and occupancy patterns across time
- Geospatial distribution of listings
- Location-based preferences and review trends

---

## 🧰 Skills & Tools

- **Languages & Libraries:** Python, Pandas, NumPy, Streamlit, Folium/GeoPandas
- **Database:** MongoDB Atlas
- **Visualization Tools:** Streamlit, Tableau, Power BI
- **Concepts:** Data Preprocessing, EDA, Geospatial Visualization, Web App Development

---

## 🗂️ Dataset Information

📦 [Download Airbnb Dataset](https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view?usp=sharing)

The dataset includes details such as:
- Listing ID, Title, Description
- Host Info (ID, Name)
- Neighborhood & Location Coordinates
- Price
- Availability Period
- Amenities
- Ratings & Reviews

Sample structure:
{
  "_id": "unique_listing_id",
  "name": "listing_title",
  "host_id": "unique_host_id",
  "neighbourhood": "Downtown",
  "location": { "type": "Point", "coordinates": [longitude, latitude] },
  "price": 120,
  "availability": { "start_date": "2023-01-01", "end_date": "2023-12-31" },
  "rating": 4.7,
  "reviews": [
    { "reviewer_name": "Alice", "comment": "Great stay!", "rating": 5 }
  ]
}

🔁 Project Workflow
-MongoDB Setup & Data Import
-Create a MongoDB Atlas account and cluster.
-Import sample Airbnb data into your collection.
-Data Cleaning & Preparation
-Handle missing values, remove duplicates.
-Standardize data types for consistent analysis.

Exploratory Data Analysis (EDA)
-Analyze pricing, availability, and review trends.
-Use groupby and aggregation techniques in MongoDB & Python.
-Geospatial Visualizations (Streamlit App)
-Create interactive maps showing price, rating, and availability distributions.
-Use libraries like Folium, Plotly, or Pydeck.
-Price & Availability Insights
-Visualize seasonal availability and pricing trends.
-Explore correlations by property type, neighborhood, etc.
-Location-Based Analysis
-Filter by region or city.
-Compare booking behavior across geographies.

Dashboard Development
-Build a final visual dashboard using Tableau or Power BI.
-Combine maps, charts, and filters to allow stakeholder-driven insights.

📊 Key Insights Goals
-Which neighborhoods have the highest-priced or most-rated listings?
-How does price vary by season and property type?
-Which areas have low availability or peak booking periods?
-What patterns can be identified in user reviews and ratings?

🎓 Learning Outcomes
-MongoDB Atlas setup, querying, and data manipulation.
-Data preprocessing with Python (Pandas, NumPy).
-Geospatial visualization using interactive Python libraries.
-Streamlit web app development for visual exploration.
-Dashboard creation using Tableau or Power BI.

🧪 Evaluation Criteria
Modular and maintainable code (PEP-8 standards).

Functional Python scripts for cleaning, EDA, and visualization.

Public GitHub repository with README and code.

Optional: Create a demo video and share on LinkedIn.

🗓 Timeline
Project Duration: 2–3 Weeks

📎 Project Guidelines & References
🧪 PEP-8 Coding Standards

📄 Skill Enhancement Resource

📤 Doubt Clarification Booking

✅ Live Evaluation Booking

📁 Project Structure
📦 Airbnb-Analysis
├── 📁 data/
│   └── airbnb_sample.json
├── 📁 scripts/
│   ├── data_cleaning.py
│   ├── eda.py
│   └── streamlit_app.py
├── 📊 dashboard/
│   └── airbnb_dashboard.pbix or .twbx
├── 📄 README.md
└── 📄 requirements.txt


By,
Yogeshwaran

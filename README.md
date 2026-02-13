# SUPPLY_CHAIN_AI

#  AI-Based Supply Chain Optimization System

##  Overview
The **AI-Based Supply Chain Optimization System** is a simple web-based application developed using **Python and Flask**.  
It helps in determining whether the available stock is sufficient or low by comparing **predicted demand** and **current stock** values.

## Problem Statement

Many organizations face difficulties in predicting product demand accurately. Poor demand forecasting results in excess inventory, increased storage costs, or loss of sales due to insufficient stock. There is a need for a simple system that can analyze past sales data and provide demand predictions to support better inventory decisions.

## Objectives

Forecast customer demand accurately using AI models
Avoid over-stocking and under-stocking of products
Monitor shipment movement in real time
Improve decision-making for suppliers, warehouses, and retailers

## Project Description

The system works by taking historical sales data as input, training a machine learning model, and predicting demand for upcoming days. The predicted demand is then compared with the current stock to determine whether the stock is sufficient or requires replenishment. All results are displayed in the terminal.

## Technologies Used

Programming Language:
Python
Libraries:
Pandas
Scikit-learn
Tkinter
Tools:
VS Code

## Installation Process

Step 1️⃣:Activate the Environment
## Windows
python -m venv venv
## Linux/Mac
source venv/bin/activate
Step 2️⃣: 
## Install Required Libraries
pip install numpy pandas matplotlib scikit-learn flask
Step 3️⃣:
## Run the html file
python app.py

## Project Structure

supply_chain_flask/
│
├── app.py

├── data.csv

└── templates/
    └── index.html

## how project works
Step 1️⃣ – Load Dataset

The system reads the CSV dataset (sales and stock data).
This is done using Pandas in Python.

Step 2️⃣ – Process the Data

It calculates:
Total demand (from sales data)
Total available stock
The system compares demand and stock values.

Step 3️⃣ – Apply Decision Logic

If demand > stock → LOW STOCK ⚠️
If stock ≥ demand → STOCK SUFFICIENT ✅
This logic helps identify inventory shortages.

Step 4️⃣ – Display Results on Web Page

The Flask web application sends results to the HTML page.
The user sees:
Total demand
Total stock
Stock status

## Future Enhancements

Adding support for multiple products
Integrating graphical dashboards
Using advanced machine learning models
Cloud-based deployment
Real-time data integration


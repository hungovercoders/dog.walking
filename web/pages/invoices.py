import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.title("Invoices")

tab1, tab2 = st.tabs(["View All Finances", "View Outstanding Invoices"])

# Generate random walks
dog_names = ["Mika", "Betty", "Bertie", "Bandit", "Haggis"]
walks = []

for _ in range(10):
    dog = random.choice(dog_names)
    duration = random.choice([30, 60])
    cost = 10 if duration == 30 else 15
    start_time = datetime(2025, 1, random.randint(1, 31), random.randint(6, 17), random.choice([0, 30]))
    end_time = start_time + timedelta(minutes=duration)
    walks.append({
        "Dog": dog,
        "Start Time": start_time.strftime("%Y-%m-%d %H:%M"),
        "End Time": end_time.strftime("%Y-%m-%d %H:%M"),
        "Duration (minutes)": duration,
        "Cost (£)": cost
    })

# Create DataFrame
df = pd.DataFrame(walks)

# Display table
st.table(df)

# Calculate and display total amount
total_amount = df["Cost (£)"].sum()
st.write(f"**Total Amount: £{total_amount}**")


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime

# Authenticate with Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the sheet (Make sure name matches your actual Google Sheet title)
sheet = client.open("Sleep tracker log").sheet1

# Streamlit UI
st.title("Sleep Tracker")

date = st.date_input("Date", datetime.today())
bed_time = st.time_input("Time to Bed")
wake_time = st.time_input("Time Woke Up")
col1, col2 = st.columns(2)
hours_slept = col1.number_input("Hours asleep", min_value=0, max_value=24, step=1)
minutes_slept = col2.number_input("Minutes asleep", min_value=0, max_value=59, step=1)
estimated_sleep_hours = hours_slept + minutes_slept / 60


if st.button("Submit"):
    total_time_in_bed = (datetime.combine(datetime.today(), wake_time) - datetime.combine(datetime.today(), bed_time)).seconds
    total_time_asleep = estimated_sleep_hours * 3600  # Convert hours to seconds
    sleep_efficiency = (total_time_asleep / total_time_in_bed) * 100 if total_time_in_bed else 0

    row = [str(date), str(bed_time), str(wake_time), round(total_time_in_bed, 2), round(total_time_asleep, 2), round(sleep_efficiency, 1)]
    sheet.append_row(row)
    st.success("Sleep data added!")


import streamlit as st
from datetime import datetime, timedelta

st.title("🛌 Sleep Efficiency Tracker")

st.markdown("""
Track how efficiently you're sleeping.  
Enter the time you went to bed and the time you woke up, plus how long you think you were actually asleep.
""")

# Inputs
bed_time = st.time_input("What time did you go to bed?")
wake_time = st.time_input("What time did you wake up?")
sleep_duration_hours = st.number_input("Estimated hours actually asleep:", min_value=0.0, max_value=24.0, step=0.25)

# Calculate total time in bed
if wake_time > bed_time:
    time_in_bed = datetime.combine(datetime.today(), wake_time) - datetime.combine(datetime.today(), bed_time)
else:
    time_in_bed = datetime.combine(datetime.today(), wake_time) + timedelta(days=1) - datetime.combine(datetime.today(), bed_time)

time_in_bed_hours = time_in_bed.total_seconds() / 3600

# Calculate efficiency
if time_in_bed_hours > 0:
    efficiency = (sleep_duration_hours / time_in_bed_hours) * 100
    st.metric("Sleep Efficiency", f"{efficiency:.1f}%")
else:
    st.warning("Time in bed must be greater than zero.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

ººººººººº


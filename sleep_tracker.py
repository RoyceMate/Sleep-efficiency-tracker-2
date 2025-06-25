import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sleep Efficiency Tracker", layout="centered")
st.title("😴 Sleep Efficiency Tracker")
st.write("Track your sleep duration and efficiency here.")

# Inputs
sleep_hours = st.number_input("How many hours did you sleep last night?", min_value=0.0, max_value=24.0, step=0.25)
time_in_bed = st.number_input("How many hours were you in bed?", min_value=0.0, max_value=24.0, step=0.25)

# Initialize session state for record storage
if "records" not in st.session_state:
    st.session_state.records = []

# Compute efficiency
if time_in_bed > 0:
    efficiency = (sleep_hours / time_in_bed) * 100
    st.metric("Sleep Efficiency (%)", f"{efficiency:.2f}%")

    # Color-coded feedback
    if efficiency >= 85:
        st.success("Great sleep efficiency!")
    elif efficiency >= 75:
        st.info("Decent sleep efficiency.")
    else:
        st.error("Try to improve your sleep efficiency.")

    # Save button
    if st.button("💾 Save Entry"):
        st.session_state.records.append({
            "Sleep Hours": sleep_hours,
            "Time in Bed": time_in_bed,
            "Efficiency (%)": round(efficiency, 2)
        })
else:
    st.warning("Enter a non-zero time in bed to calculate efficiency.")

# Show saved records
if st.session_state.records:
    st.subheader("📊 Sleep History")
    df = pd.DataFrame(st.session_state.records)
    st.dataframe(df)

    st.line_chart(df[["Efficiency (%)"]])

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Sleep History as CSV",
        data=csv,
        file_name="sleep_history.csv",
        mime="text/csv"
    )


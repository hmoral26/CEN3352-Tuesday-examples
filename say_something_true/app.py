# week 3 — thursday page + the 6 widgets from class
# form so it only reruns when I hit submit

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Say Something True Week 3", page_icon="✎", layout="wide")

st.title("Something I Know Is True")
st.caption("Thursday tabs, plus a parking report form for week 3")

with st.sidebar:
    st.header("Quick note")
    st.write("For commuter students at NCF.")
    st.write("Parking is basically a guess every morning.")
    st.caption("sidebar stays when I switch tabs")

commute_log = pd.DataFrame({
    "Morning": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Minutes spent searching for parking": [15, 12, 8, 6, 3],
})
worst = commute_log["Minutes spent searching for parking"].max()

tab1, tab2, tab3, tab4 = st.tabs(["The Problem", "A Fact", "Who It's For", "Report"])

with tab1:
    st.subheader("The Problem")
    st.write(
        "Commuter students at New College plan their whole morning around a "
        "guess about parking availability, because there's still no reliable "
        "way to check ahead of time."
    )
    st.write("How might we let people know if parking is bad before they leave home?")

with tab2:
    st.subheader("A Fact")
    left, right = st.columns([2, 1])
    with left:
        st.bar_chart(commute_log.set_index("Morning"))
    with right:
        st.metric("Worst morning", str(int(worst)) + " min")
    st.caption("timed it myself for 5 mornings. mon and tue were the worst")

with tab3:
    st.subheader("Who It's For")
    st.write("Persona: commuter student at New College")
    st.write("Goal: get to 9am class on time without leaving super early every day")
    st.write("Frustration: some days parking takes like 3 min and some days almost 20")
    st.write('Quote: "I plan my whole morning around a guess."')
    with st.expander("Where this came from"):
        st.write("Just my own mornings. Not an official parking study.")

# week 3 widgets — all 6, inside a form like the class demo
with tab4:
    st.subheader("Report a Parking Problem")
    st.caption("app only reruns when I click submit, not on every keystroke")

    with st.form("parking_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Your name")
            minutes = st.number_input(
                "Minutes searching", min_value=0, max_value=60, value=10
            )
            frustration = st.slider("Frustration (1-10)", 1, 10, value=5)

        with col2:
            lot = st.selectbox(
                "Which lot?", ["Lot A", "Lot B", "Lot C", "Lot D"]
            )
            time = st.radio(
                "What time?", ["Morning", "Midday", "Evening"]
            )
            would_use = st.checkbox(
                "I would use a real-time parking app"
            )

        submitted = st.form_submit_button("Submit report")

    if submitted:
        st.divider()
        who = name if name else "An anonymous student"
        st.write(
            f"**{who}** spent **{minutes} min** in **{lot}** "
            f"during the **{time}**, frustration **{frustration}/10**."
        )
        if would_use:
            st.success("Thanks — noted you'd use a real-time version.")

            
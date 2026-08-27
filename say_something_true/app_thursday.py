# thursday 
# same parking page as tuesday but split into tabs
# columns, tabs, sidebar, expander

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Say Something True Thursday", page_icon="✎", layout="wide")

st.title("Something I Know Is True: ")
st.caption("Same parking page from tuesday, just not one long page anymore.")

# sidebar stays no matter which tab is open
with st.sidebar:
    st.header("Quick note")
    st.write("For commuter students at NCF.")
    st.write("Parking is basically a guess every morning.")
    st.caption("This side is not supposed to change when I switch tabs ")


#table (dataFrame using panda)
commute_log = pd.DataFrame({
    "Morning": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Minutes spent searching for parking": [15, 12, 8, 6, 3],
})
worst = commute_log["Minutes spent searching for parking"].max()

tab1, tab2, tab3 = st.tabs(["The Problem", "A Fact", "Who It's For"])


#tab 1; The problem
with tab1:
    st.subheader("The Problem")
    st.write(
        "Commuter students at New College plan their whole morning around a "
        "guess about parking availability, because there's still no reliable "
        "way to check ahead of time."
    )
    st.write("How might we let people know if parking is bad before they leave home?")


#tab 2; A fact
with tab2:
    st.subheader("A Fact")

    left, right = st.columns([2, 1])

    with left:
        st.bar_chart(commute_log.set_index("Morning"))

    with right:
        st.metric("Worst morning", str(int(worst)) + " min")

    st.caption("timed it myself for 5 mornings. mon and tue were the worst")


#tab 3; WHo is it for
with tab3:
    st.subheader("Who It's For")
    st.write("Persona: commuter student at New College")
    st.write("Goal: get to 9am class on time without leaving super early every day")
    st.write("Frustration: some days parking takes like 3 min and some days almost 20")
    st.write('Quote: "I plan my whole morning around a guess."')

    # expander
    with st.expander("Where this came from"):
        st.write("Just my own mornings. Not an official parking study.")


        
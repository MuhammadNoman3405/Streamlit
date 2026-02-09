## Chapter 01>>>>>>>>>>>>>>>>>>

import streamlit as st

st.title("That is  the header of the app")
st.subheader("This is the sub header of the app")
st.text("That is the text heading")
st.write("This is the write heading")
st.header("This is header")

## selective box>>>>>>>>>>>>>>>>>

fruit = st.selectbox(
    " Choose Your favourite fruits:", ["Apple", "Banana", "Orange", "Mango", "Grapes"]
)
st.write(f"you choose {fruit}. nice choice")

## success but static box>>>>>>>>

st.success(f"Your fruit is {fruit}")


##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#####
## Chapter 2 has been started

st.title("Now i am going to make button")

## button>>>>>>>>>>>>>>>>>>>>>

if st.button("Your Fruite"):
    st.success(f"Your favourite fruite is: {fruit}")

## checkbox>>>>>>>>>>>>>>>>>>>>

check = st.checkbox("check your fav fruite")
if check:
    st.write("You checked the fav fruite")

## now radio>>>>>>>>>>>>>

choose_fruit = st.radio(
    "choose you fav fruite", ["Apple", "Banana", "Orange", "Mango", "Grapes"]
)
st.write(f"you choose the {choose_fruit}")


# slider>>>>>>>>>>>>>>>>>

st.slider(
    "How much the sweetness was?", 0, 10, 5
)  # 0 is min 10 is max and 5 is by default

# number_input>>>>>>>>>>>>>>

num_input = st.number_input(
    "How many fruite you want to eat?", min_value=1, max_value=10, step=1
)
st.write(f"your selected value is {num_input}")

# text_input>>>>>>>>>>>>>

name_input = st.text_input("Enter your name")
st.write(f"Hello {name_input} How are you?")

# Date of Birth Calculator>>>>>>>>>>>>

from datetime import date

min_value = date(1990, 1, 1)
max_value = date.today()
default = date(2006, 1, 1)

if "clicked" not in st.session_state:
    st.session_state.clicked = False

if st.button("Click to enter age:"):
    st.session_state.clicked = True


if st.session_state.clicked:
    dob = st.date_input(
        "select your age:",
        value=default,
        min_value=min_value,
        max_value=max_value,
    )
    st.success(f"You Select the age: {dob}")
    age_year = max_value.year - dob.year
    days = max_value.day - dob.day

    today = date.today()

    this_year_birthday = date(today.year, dob.month, dob.day)
    if this_year_birthday < today:
        next_year_birthday = date(today.year + 1, dob.month, dob.day)
    else:
        next_year_birthday = this_year_birthday

    days_remaining = (next_year_birthday - today).days
    if days_remaining == 0:
        st.balloons()
        st.success("Happy Birthday, Noman! It's today! 🎂")

    else:
        st.success(f"Your next birthday days remaing are {days_remaining}")


##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Column Making
st.title("Welcome to the voting poll")
col1, col2 = st.columns(2)
with col1:
    st.header("Vote the Apple Fruite")
    st.image(r"images/apple.jpg", width=100)
    vot1 = st.button("Click to vote1")

with col2:
    st.header("Vote the Orange Fruite")
    st.image(
        r"images/orange.jpg",
        width=100,
    )
    vot2 = st.button("Click to vote2")

if vot1:  ## as it is button
    st.success("Thanks for voting Apple")
elif vot2:  ## as it is also button
    st.success("Thanks for voting Orange")

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Sidebar Making

name = st.sidebar.text_input("Enter your name:")
choice = st.sidebar.selectbox(
    "choose your fav fruite", ["Apple", "Banana", "Mango", "Grapes", "Orange"]
)

st.write(f"Welcome {name} your fav fruite is {choice}")


##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## expander

with st.expander("Instruction to eat fruite:"):
    st.write(
        """ 
Eat fruit on an empty stomach to ensure your body absorbs all the nutrients efficiently.

Always wash fruits thoroughly under running water to remove dirt, wax, or pesticides.

Prefer eating whole fruits over drinking juice to get the full benefit of dietary fiber.

Try to eat fruit before meals rather than immediately after a heavy lunch or dinner.

Consume a variety of different colored ruits to get a diverse range of vitamins and antioxidants.

Eat fruits at room temperature instead of chilled to keep your digestive enzymes active.
             """
    )

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Markdown

st.markdown("## Hello Noman")
st.markdown("> step 01")
st.markdown("> step 02")

st.markdown(
    """
### My Tech Stack
* Python & C++
* Machine Learning
* SQL
"""
)

st.markdown(
    """
### Project Steps
1. Data Collection
2. Data Preprocessing
3. Model Training
"""
)

st.markdown(
    """
| Exam | Marks Obtained | Total Marks |
| :--- | :--- | :--- |
| Matric | 1093 | 1100 |
| FSc | 474 | 520 |
| ECAT | 176 | 400 |
"""
)

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Uploading csv file

import pandas as pd
import streamlit as st

st.title("Fruite Data")

file = st.file_uploader("Upload your csv file", type=["csv"])

if file is not None:
    file.seek(0)  #  REQUIRED
    df = pd.read_csv(file)
    st.header("Data Preview")
    st.dataframe(df)

if file is not None:
    st.subheader("Summary")
    st.write(df.describe())

    st.subheader("Now Some Headers")
    st.write(df.head(5))

    st.subheader("Column Types")
    st.write(df.dtypes)
## Now make df for the unique fruite
if file is not None:
    uniq = df["Fruit_Name"].unique()
    choose_fruit = st.selectbox("Choose the Fruite:", uniq)
    new_df = df[df["Fruit_Name"] == choose_fruit]
    st.dataframe(new_df)


##>>>>>>>>>>>>>>>>>>> Currency Calculator viva Api Server>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import requests

# A list of frequently used currency codes (ISO 4217)
currency_codes = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "INR",
    "PKR",
    "CAD",
    "AUD",
    "CHF",
    "CNY",
    "SAR",
    "AED",
    "TRY",
    "NZD",
    "SGD",
    "HKD",
    "MYR",
    "KWD",
]

st.title("Currency Converter")

amount_entered = st.number_input("Enter the amount in Pkr", min_value=1)
selected_currency = st.selectbox("Select the Currency:", currency_codes)
if st.button("Click to convert"):
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][selected_currency]

        final_result = amount_entered * rate  ## formula for conversion

        # this shows final output
        st.write(
            f"{selected_currency} Rate: {data['rates'][selected_currency]} And Converted Amount :{final_result:,.2f}"
        )

    else:
        st.write("Failed to retrieve data")

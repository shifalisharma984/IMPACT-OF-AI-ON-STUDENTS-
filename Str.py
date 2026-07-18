import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu
import requests
import base64
import plotly.figure_factory as ff



df = pd.read_csv("ai_student_impact_dataset (1).csv")

st.set_page_config(
    page_title="Impact of AI on Students",
    page_icon="🎓",
    layout="wide"
)

with st.sidebar:
    opt = option_menu(
        "Main Menu",
        ["Home","Dataset","Processing","Visualization","About"],
        icons=["house","table","gear","bar-chart","person"],
        default_index=0
    )
if opt == "Home":
    from PIL import Image

# ------------------ PAGE CONFIG ------------------
    st.set_page_config(
        page_title="AI Impact on Students",
        page_icon="🎓",
        layout="wide"
    )

    # ------------------ CUSTOM CSS ------------------
    st.markdown("""
    <style>

    .main{
        background-color:#F5F7FA;
    }

    .title{
        text-align:center;
        color:#1F4E79;
        font-size:42px;
        font-weight:bold;
    }

    .subtitle{
        text-align:center;
        font-size:20px;
        color:#555555;
    }

    .card{
        background:white;
        padding:20px;
        border-radius:12px;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
    }

    .metric{
        background:#E8F0FE;
        padding:15px;
        border-radius:10px;
        text-align:center;
    }

    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
<style>

/* ==============================
   MAIN BACKGROUND
============================== */

.stApp{
    background: linear-gradient(135deg,#F4F7FC,#E8EEF8,#F8FAFC);
}

/* ==============================
   MAIN CONTAINER
============================== */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* ==============================
   TITLE
============================== */

.title{
    font-size:48px;
    font-weight:800;
    text-align:center;
    color:#0F172A;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    color:#64748B;
    font-size:20px;
    margin-bottom:30px;
}

/* ==============================
   HEADINGS
============================== */

h1,h2,h3{
    color:#1E3A8A;
    font-weight:700;
}

/* ==============================
   PARAGRAPH
============================== */

p{
    font-size:17px;
    color:#334155;
    line-height:1.8;
}

/* ==============================
   METRIC CARDS
============================== */

div[data-testid="metric-container"]{

    background:white;
    border-radius:18px;
    padding:20px;
    border:1px solid #E2E8F0;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

    transition:0.3s;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-8px);

    box-shadow:0 15px 35px rgba(37,99,235,.25);

    border:1px solid #2563EB;
}

/* ==============================
   SUCCESS / INFO / WARNING BOXES
============================== */

div[data-testid="stAlert"]{

    border-radius:15px;

    border:none;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ==============================
   IMAGE
============================== */

img{

    border-radius:20px;

    box-shadow:0 10px 25px rgba(0,0,0,.15);
}

/* ==============================
   BUTTONS
============================== */

.stButton>button{

    border-radius:12px;

    background:#2563EB;

    color:white;

    font-weight:bold;

    border:none;

    transition:.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

    transform:scale(1.03);
}

/* ==============================
   SIDEBAR
============================== */

section[data-testid="stSidebar"]{

    background:#0F172A;
}

section[data-testid="stSidebar"] *{

    color:white;
}

/* ==============================
   DATAFRAME
============================== */

div[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;
}

/* ==============================
   EXPANDER
============================== */

details{

    border-radius:15px;

    background:white;
}

/* ==============================
   HORIZONTAL LINE
============================== */

hr{

    border:1px solid #CBD5E1;
}

/* ==============================
   SCROLLBAR
============================== */

::-webkit-scrollbar{

    width:10px;
}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:10px;
}

::-webkit-scrollbar-track{

    background:#E2E8F0;
}

</style>
""", unsafe_allow_html=True)

    # ------------------ TITLE ------------------

    st.markdown("<div class='title'>🎓 Analysis of AI Impact on Students</div>", unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Using Data Science and Streamlit Dashboard</div>", unsafe_allow_html=True)

    st.write("")

    # ------------------ IMAGE ------------------

    image = Image.open("ai.jpg")

    col1,col2 = st.columns([1.5,2])

    with col1:
        st.image(image,use_container_width=True)

    with col2:

        st.markdown("""
        ## 📖 Project Overview

        Artificial Intelligence has transformed modern education.
        Students increasingly rely on AI tools for assignments,
        coding, research, note-making and exam preparation.

        This dashboard analyzes how AI usage influences:

        ✔ Academic Performance

        ✔ Study Habits

        ✔ AI Dependency

        ✔ Burnout Risk

        ✔ Skill Retention

        ✔ Prompt Engineering Skills

        ✔ Traditional Study Hours

        ✔ Institutional Policies
        """)

    st.write("---")

    # ------------------ OBJECTIVES ------------------

    st.header("🎯 Project Objectives")

    c1,c2,c3=st.columns(3)

    with c1:
        st.info("""
        Analyze AI usage among students.
        """)

        st.info("""
        Study traditional study habits.
        """)

    with c2:
        st.success("""
        Compare GPA before and after AI usage.
        """)

        st.success("""
        Measure AI dependency.
        """)

    with c3:
        st.warning("""
        Analyze burnout risk.
        """)

        st.warning("""
        Generate meaningful insights.
        """)

    st.write("---")

    # ------------------ DATASET INFO ------------------

    st.header("📂 Dataset Information")

    left,right=st.columns(2)

    with left:

        st.markdown("""
    **Dataset Features**

    - Student_ID
    - Major_Category
    - Year_of_Study
    - Pre_Semester_GPA
    - Weekly_GenAI_Hours
    - Primary_Use_Case
    - Prompt_Engineering_Skill
    - Tool_Diversity
    - Paid_Subscription
    - Traditional_Study_Hours
        """)

    with right:

        st.markdown("""
    **Additional Columns**

    - Perceived_AI_Dependency
    - Institutional_Policy
    - Anxiety_Level_During_Exams
    - Post_Semester_GPA
    - Skill_Retention_Score
    - Burnout_Risk_Level
        """)

    st.write("---")

    # ------------------ DASHBOARD FEATURES ------------------

    st.header("📊 Dashboard Features")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Visualizations","15+")

    with col2:
        st.metric("Dataset Features","16")

    with col3:
        st.metric("EDA","Complete")

    with col4:
        st.metric("Machine Learning","No")

    st.write("---")

    # ------------------ TECHNOLOGIES ------------------

    st.header("🛠 Technologies Used")

    st.write("""
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    """)

    st.write("---")

    # ------------------ FOOTER ------------------

    st.success("✔ Navigate through the left sidebar to explore Data Analysis, Visualizations and Insights.")

    st.caption("Developed using Streamlit | AI Impact on Students Project")












elif opt == "Dataset":
   
    st.markdown("""
<style>

/* ==========================
   DATASET PAGE BACKGROUND
========================== */

.stApp{
    background: linear-gradient(135deg,#F8FAFC,#EEF4FF,#F8FAFC);
}

/* ==========================
   MAIN CONTAINER
========================== */

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
    padding-bottom:2rem;
}

/* ==========================
   TITLE
========================== */

h1{
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:800;
}

h2,h3{
    color:#2563EB;
    font-weight:700;
}

/* ==========================
   PARAGRAPH
========================== */

p{
    color:#475569;
    font-size:17px;
    line-height:1.7;
}

/* ==========================
   METRIC CARDS
========================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    padding:18px;

    border:1px solid #E2E8F0;

    box-shadow:0 8px 18px rgba(0,0,0,.08);

    transition:.3s;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-6px);

    box-shadow:0 15px 30px rgba(37,99,235,.25);

    border:1px solid #2563EB;
}

/* ==========================
   DATAFRAME
========================== */

div[data-testid="stDataFrame"]{

    background:white;

    border-radius:15px;

    border:1px solid #CBD5E1;

    padding:10px;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ==========================
   ALERT BOXES
========================== */

div[data-testid="stAlert"]{

    border-radius:15px;

    border:none;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ==========================
   DOWNLOAD BUTTON
========================== */

.stDownloadButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    font-size:16px;

    font-weight:bold;

    border:none;

    border-radius:12px;

    padding:10px;

    transition:.3s;
}

.stDownloadButton>button:hover{

    background:#1D4ED8;

    transform:scale(1.03);
}

/* ==========================
   SLIDER
========================== */

.stSlider{

    padding-top:10px;

    padding-bottom:15px;
}

/* ==========================
   EXPANDER
========================== */

details{

    background:white;

    border-radius:12px;

    padding:10px;
}

/* ==========================
   HORIZONTAL LINE
========================== */

hr{

    border:1px solid #CBD5E1;
}

/* ==========================
   SCROLLBAR
========================== */

::-webkit-scrollbar{

    width:10px;
}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:10px;
}

::-webkit-scrollbar-track{

    background:#E5E7EB;
}

</style>
""", unsafe_allow_html=True)
    # ---------------- PAGE CONFIG ----------------
    st.set_page_config(
        page_title="Dataset",
        page_icon="📂",
        layout="wide"
    )

    # ---------------- TITLE ----------------
    st.title("📂 Dataset Information")
    st.markdown("---")

    # ---------------- LOAD DATA ----------------
    @st.cache_data
    def load_data():
        return pd.read_csv("ai_student_impact_dataset (1).csv")   

    # ---------------- DATASET OVERVIEW ----------------
    st.header("📖 Dataset Overview")

    st.write("""
    This dataset contains information about students' use of Artificial Intelligence
    tools in education. It helps analyze how AI affects academic performance,
    study habits, anxiety, skill retention, and burnout risk.
    """)

    st.markdown("---")

    # ---------------- DATASET METRICS ----------------
    st.header("📊 Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    st.markdown("---")

    # ---------------- PREVIEW ----------------
    st.header("👀 Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("---")

    # ---------------- SHAPE ----------------
    st.header("📏 Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Number of Rows : **{df.shape[0]}**")

    with col2:
        st.info(f"Number of Columns : **{df.shape[1]}**")

    st.markdown("---")

    # ---------------- COLUMN NAMES ----------------
    st.header("📝 Column Names")

    columns = pd.DataFrame({
        "Column Number": range(1, len(df.columns)+1),
        "Column Name": df.columns
    })

    st.dataframe(columns, use_container_width=True)

    st.markdown("---")

    # ---------------- DATA TYPES ----------------
    st.header("🔤 Data Types")

    dtype = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype, use_container_width=True)

    st.markdown("---")

    # ---------------- MISSING VALUES ----------------
    st.header("❗ Missing Values")

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum(),
        "Percentage": round((df.isnull().sum()/len(df))*100,2)
    })

    st.dataframe(missing, use_container_width=True)

    st.markdown("---")

    # ---------------- DESCRIPTIVE STATISTICS ----------------
    st.header("📈 Statistical Summary")

    st.dataframe(df.describe(), use_container_width=True)

    st.markdown("---")

    # ---------------- CATEGORICAL COLUMNS ----------------
    st.header("📌 Categorical Columns")

    cat = df.select_dtypes(include="object").columns.tolist()

    st.write(cat)

    st.markdown("---")

    # ---------------- NUMERICAL COLUMNS ----------------
    st.header("🔢 Numerical Columns")

    num = df.select_dtypes(exclude="object").columns.tolist()

    st.write(num)

    st.markdown("---")

    # ---------------- RANDOM SAMPLE ----------------
    st.header("🎲 Random Sample")

    sample_size = st.slider("Select Number of Rows", 5, 20, 5)

    st.dataframe(df.sample(sample_size), use_container_width=True)

    st.markdown("---")

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        label="⬇ Download Dataset",
        data=df.to_csv(index=False),
        file_name="ai_student_impact_dataset(1).csv",
        mime="text/csv"
    )

    st.success("Dataset Loaded Successfully ✅")






elif opt == "Processing":
    st.markdown("""
<style>

/* ===========================
   PROCESSING PAGE
=========================== */

.stApp{
    background:linear-gradient(135deg,#F8FAFC,#EEF5FF,#F8FAFC);
}

/* Main Container */
.block-container{
    padding:2rem 3rem;
}

/* ===========================
   TITLES
=========================== */

h1{
    text-align:center;
    color:#1E40AF;
    font-size:42px;
    font-weight:800;
}

h2,h3{
    color:#2563EB;
    font-weight:700;
}

/* Paragraph */
p{
    color:#475569;
    font-size:17px;
    line-height:1.8;
}

/* ===========================
   METRIC CARDS
=========================== */

div[data-testid="metric-container"]{

    background:#FFFFFF;

    border-radius:18px;

    padding:20px;

    border:1px solid #E2E8F0;

    box-shadow:0 8px 20px rgba(0,0,0,.08);

    transition:0.3s;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-6px);

    border:1px solid #2563EB;

    box-shadow:0 15px 35px rgba(37,99,235,.25);
}

/* ===========================
   DATAFRAMES
=========================== */

div[data-testid="stDataFrame"]{

    background:white;

    border-radius:15px;

    border:1px solid #CBD5E1;

    padding:10px;

    box-shadow:0 8px 18px rgba(0,0,0,.08);
}

/* ===========================
   ALERT BOXES
=========================== */

div[data-testid="stAlert"]{

    border-radius:15px;

    border:none;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ===========================
   SUCCESS MESSAGE
=========================== */

div[data-baseweb="notification"]{

    border-radius:15px;
}

/* ===========================
   BUTTONS
=========================== */

.stButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    font-weight:bold;

    border:none;

    border-radius:12px;

    transition:.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

    transform:scale(1.03);
}

/* ===========================
   MARKDOWN LISTS
=========================== */

ul{

    color:#334155;

    font-size:16px;

    line-height:1.8;
}

/* ===========================
   DIVIDER
=========================== */

hr{

    border:1px solid #CBD5E1;
}

/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{

    width:10px;
}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:10px;
}

::-webkit-scrollbar-track{

    background:#E5E7EB;
}

</style>
""", unsafe_allow_html=True)
# ---------------- PAGE CONFIG ----------------
    st.set_page_config(
        page_title="Data Processing",
        page_icon="⚙️",
        layout="wide"
    )

    # ---------------- LOAD DATA ----------------
    
    # ---------------- TITLE ----------------
    st.title("⚙️ Data Processing")
    st.markdown("---")

    st.write("""
    Data preprocessing is an important step in Data Science.
    This page shows how the dataset is cleaned and prepared before analysis.
    """)

    # ---------------- ORIGINAL DATA ----------------
    st.header("📄 Original Dataset")

    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")

    # ---------------- DATA INFORMATION ----------------
    st.header("📋 Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Total Missing Values", df.isnull().sum().sum())

    st.markdown("---")

    # ---------------- DUPLICATES ----------------
    st.header("🔁 Duplicate Records")

    duplicates = df.duplicated().sum()

    if duplicates == 0:
        st.success("No duplicate records found.")
    else:
        st.warning(f"{duplicates} duplicate records found.")
        df = df.drop_duplicates()
        st.success("Duplicate records removed.")

    st.markdown("---")

    # ---------------- MISSING VALUES ----------------
    st.header("❗ Missing Values")

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(missing, use_container_width=True)

    st.markdown("---")

    # ---------------- DATA TYPES ----------------
    st.header("🔤 Data Types")

    st.dataframe(df.dtypes.astype(str).reset_index().rename(
        columns={"index":"Column",0:"Data Type"}
    ), use_container_width=True)

    st.markdown("---")

    # ---------------- CLEANED DATA ----------------
    st.header("🧹 Cleaned Dataset Preview")

    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")

    # ---------------- NUMERICAL COLUMNS ----------------
    st.header("🔢 Numerical Columns")

    num_cols = df.select_dtypes(include=["int64","float64"]).columns.tolist()

    st.write(num_cols)

    st.markdown("---")

    # ---------------- CATEGORICAL COLUMNS ----------------
    st.header("📌 Categorical Columns")

    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

    st.write(cat_cols)

    st.markdown("---")

    # ---------------- SUMMARY ----------------
    st.header("📑 Processing Summary")

    st.success("""
    ✔ Dataset Loaded Successfully

    ✔ Checked Dataset Shape

    ✔ Verified Data Types

    ✔ Checked Missing Values

    ✔ Removed Duplicate Records (if any)

    ✔ Identified Numerical and Categorical Features

    ✔ Dataset Ready for Visualization
    """)





elif opt == "Visualization":

    st.markdown("""
<style>

/* ===========================
   BACKGROUND
=========================== */

.stApp{
    background: linear-gradient(135deg,#F8FAFC,#EEF4FF,#F8FAFC);
}

/* ===========================
   MAIN CONTAINER
=========================== */

.block-container{
    padding-top:1.5rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:2rem;
}

/* ===========================
   TITLES
=========================== */

h1{
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:800;
}

h2,h3{
    color:#2563EB;
    font-weight:700;
}

/* ===========================
   TABS
=========================== */

button[data-baseweb="tab"]{

    background:white;

    border-radius:12px;

    margin-right:8px;

    border:1px solid #CBD5E1;

    font-weight:600;

    transition:.3s;
}

button[data-baseweb="tab"]:hover{

    background:#DBEAFE;

    color:#2563EB;
}

button[aria-selected="true"]{

    background:#2563EB !important;

    color:white !important;

    border:none;
}

/* ===========================
   SELECT BOX
=========================== */

div[data-baseweb="select"]{

    border-radius:10px;
}

/* ===========================
   SLIDER
=========================== */

.stSlider{

    padding-top:10px;
}

/* ===========================
   PLOTLY CHART
=========================== */

div[data-testid="stPlotlyChart"]{

    background:white;

    padding:15px;

    border-radius:18px;

    border:1px solid #E2E8F0;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

    margin-bottom:20px;
}

/* ===========================
   DATAFRAME
=========================== */

div[data-testid="stDataFrame"]{

    background:white;

    border-radius:15px;

    border:1px solid #CBD5E1;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ===========================
   METRIC CARDS
=========================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    border:1px solid #E2E8F0;

    box-shadow:0 8px 20px rgba(0,0,0,.08);

    transition:.3s;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-5px);

    border:1px solid #2563EB;
}

/* ===========================
   INFO / SUCCESS / WARNING
=========================== */

div[data-testid="stAlert"]{

    border-radius:15px;

    border:none;

    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* ===========================
   BUTTONS
=========================== */

.stButton>button{

    background:#2563EB;

    color:white;

    border-radius:10px;

    border:none;

    transition:.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

    transform:scale(1.03);
}

/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#2563EB;
    border-radius:10px;
}

::-webkit-scrollbar-track{
    background:#E5E7EB;
}

    </style>
    """, unsafe_allow_html=True) 

    # st.set_page_config(
    #     page_title="AI Impact on Students",
    #     page_icon="🎓",
    #     layout="wide"
    # )

    st.title("🎓 AI Impact on Students Dashboard")
    st.markdown("Interactive visualization of AI usage and its impact on students.")

    # Load Dataset
    df = pd.read_csv("ai_student_impact_dataset (1).csv")
    # If your file is CSV, use:
    # df = pd.read_csv("ai_student_impact_dataset.csv")

    # Tabs
    distribution, comparison, relationship, composition, correlation = st.tabs([
        "Distribution",
        "Comparison",
        "Relationship",
        "Composition",
        "Correlation"
    ])

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    # ====================================================
    # DISTRIBUTION
    # ====================================================

    with distribution:

        st.header("📊 Distribution Analysis")

        # ---------------- FILTERS ----------------

        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Bar Chart",
                "Line Chart",
                "Scatter Plot",
                "Pie Chart",
                "Histogram",
                "Box Plot"
            ]
        )

        # Slider for number of rows
        rows = st.slider(
            "Select Number of Records",
            min_value=10,
            max_value=len(df),
            value=min(100, len(df)),
            step=10
        )

        filter_df = df.head(rows)

        st.info(f"Showing first **{rows}** records")

        # ---------------- BAR CHART ----------------

        if chart_type == "Bar Chart":

            x_col = st.selectbox(
                "X-Axis",
                categorical_cols,
                key="barx"
            )

            y_col = st.selectbox(
                "Y-Axis",
                numeric_cols,
                key="bary"
            )

            bar_df = filter_df.groupby(x_col)[y_col].mean().reset_index()

            fig = px.bar(
                bar_df,
                x=x_col,
                y=y_col,
                color=x_col,
                text_auto=".2f",
                title=f"Average {y_col} by {x_col}"
            )

            fig.update_layout(
                xaxis_title=x_col,
                yaxis_title=f"Average {y_col}",
                height=550
            )

            st.plotly_chart(fig, use_container_width=True)

        # ---------------- LINE CHART ----------------

        elif chart_type == "Line Chart":

            x_col = st.selectbox(
                "X-Axis",
                numeric_cols,
                key="linex"
            )

            y_col = st.selectbox(
                "Y-Axis",
                numeric_cols,
                key="liney"
            )

            fig = px.line(
                filter_df.sort_values(x_col),
                x=x_col,
                y=y_col,
                markers=True,
                title=f"{y_col} vs {x_col}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ---------------- SCATTER PLOT ----------------

        elif chart_type == "Scatter Plot":

            x_col = st.selectbox(
                "X-Axis",
                numeric_cols,
                key="scatterx"
            )

            y_col = st.selectbox(
                "Y-Axis",
                numeric_cols,
                key="scattery"
            )

            color_col = st.selectbox(
                "Color By",
                categorical_cols,
                key="scattercolor"
            )

            fig = px.scatter(
                filter_df,
                x=x_col,
                y=y_col,
                color=color_col,
                size_max=15,
                hover_data=filter_df.columns,
                title=f"{y_col} vs {x_col}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ---------------- PIE CHART ----------------

        elif chart_type == "Pie Chart":

            cat_col = st.selectbox(
                "Category",
                categorical_cols,
                key="pie"
            )

            pie_df = filter_df[cat_col].value_counts().reset_index()
            pie_df.columns = [cat_col, "Count"]

            fig = px.pie(
                pie_df,
                names=cat_col,
                values="Count",
                hole=0.45,
                title=f"{cat_col} Distribution"
            )

            fig.update_traces(textposition="inside", textinfo="percent+label")

            st.plotly_chart(fig, use_container_width=True)

        # ---------------- HISTOGRAM ----------------

        elif chart_type == "Histogram":

            num_col = st.selectbox(
                "Numeric Column",
                numeric_cols,
                key="hist"
            )

            fig = px.histogram(
                filter_df,
                x=num_col,
                nbins=25,
                color_discrete_sequence=["royalblue"],
                marginal="box",
                title=f"Distribution of {num_col}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ---------------- BOX PLOT ----------------

        elif chart_type == "Box Plot":

            num_col = st.selectbox(
                "Numeric Column",
                numeric_cols,
                key="box"
            )

            fig = px.box(
                filter_df,
                y=num_col,
                color_discrete_sequence=["crimson"],
                points="outliers",
                title=f"Box Plot of {num_col}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

    # ====================================================
    # COMPARISON
    # ====================================================

    with comparison:

        st.header("📊 Comparison Analysis")

        # ---------------- SETTINGS ----------------

        chart_type = st.selectbox(
            "Select Comparison Chart",
            [
                "Bar Chart",
                "Line Chart",
                "Scatter Plot",
                "Pie Chart",
                "Box Plot",
                "Violin Plot"
            ],
            key="comparison_chart"
        )

        rows = st.slider(
            "Number of Records",
            min_value=10,
            max_value=len(df),
            value=min(100, len(df)),
            step=10,
            key="comparison_rows"
        )

        filter_df = df.head(rows)

        category = st.selectbox(
            "Select Category",
            categorical_cols,
            key="category"
        )

        value = st.selectbox(
            "Select Numeric Column",
            numeric_cols,
            key="value"
        )

        # ------------------------------------------------
        # BAR CHART
        # ------------------------------------------------

        if chart_type == "Bar Chart":

            avg_df = (
                filter_df.groupby(category)[value]
                .mean()
                .reset_index()
            )

            fig = px.bar(
                avg_df,
                x=category,
                y=value,
                color=category,
                text_auto=".2f",
                title=f"Average {value} by {category}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ------------------------------------------------
        # LINE CHART
        # ------------------------------------------------

        elif chart_type == "Line Chart":

            avg_df = (
                filter_df.groupby(category)[value]
                .mean()
                .reset_index()
            )

            fig = px.line(
                avg_df,
                x=category,
                y=value,
                markers=True,
                title=f"{value} Comparison"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ------------------------------------------------
        # SCATTER PLOT
        # ------------------------------------------------

        elif chart_type == "Scatter Plot":

            fig = px.scatter(
                filter_df,
                x=category,
                y=value,
                color=category,
                hover_data=filter_df.columns,
                title=f"{value} by {category}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ------------------------------------------------
        # PIE CHART
        # ------------------------------------------------

        elif chart_type == "Pie Chart":

            pie_df = (
                filter_df.groupby(category)[value]
                .mean()
                .reset_index()
            )

            fig = px.pie(
                pie_df,
                names=category,
                values=value,
                hole=0.45,
                title=f"{value} Distribution"
            )

            fig.update_traces(textinfo="percent+label")

            st.plotly_chart(fig, use_container_width=True)

        # ------------------------------------------------
        # BOX PLOT
        # ------------------------------------------------

        elif chart_type == "Box Plot":

            fig = px.box(
                filter_df,
                x=category,
                y=value,
                color=category,
                points="outliers",
                title=f"{value} by {category}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)

        # ------------------------------------------------
        # VIOLIN PLOT
        # ------------------------------------------------

        elif chart_type == "Violin Plot":

            fig = px.violin(
                filter_df,
                x=category,
                y=value,
                color=category,
                box=True,
                points="all",
                title=f"{value} Distribution by {category}"
            )

            fig.update_layout(height=550)

            st.plotly_chart(fig, use_container_width=True)
        with relationship:

            st.header("🔗 Relationship Analysis")

            # ---------------- SETTINGS ----------------

            chart_type = st.selectbox(
                "Select Relationship Chart",
                [
                    "Scatter Plot",
                    "Bubble Chart",
                    "Line Chart",
                    "Heatmap",
                    "Hexbin Style",
                    "Trend Scatter"
                ],
                key="relationship_chart"
            )

            rows = st.slider(
                "Number of Records",
                min_value=10,
                max_value=len(df),
                value=min(200, len(df)),
                step=10,
                key="relationship_rows"
            )

            filter_df = df.head(rows)

            x_col = st.selectbox(
                "Select X-Axis",
                numeric_cols,
                key="rel_x"
            )

            y_col = st.selectbox(
                "Select Y-Axis",
                numeric_cols,
                index=1,
                key="rel_y"
            )

            color_col = st.selectbox(
                "Color By",
                categorical_cols,
                key="rel_color"
            )

            # --------------------------------------------------------
            # Scatter Plot
            # --------------------------------------------------------

            if chart_type == "Scatter Plot":

                fig = px.scatter(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    color=color_col,
                    hover_data=filter_df.columns,
                    title=f"{y_col} vs {x_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # --------------------------------------------------------
            # Bubble Chart
            # --------------------------------------------------------

            elif chart_type == "Bubble Chart":

                size_col = st.selectbox(
                    "Bubble Size",
                    numeric_cols,
                    key="bubble_size"
                )

                fig = px.scatter(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    size=size_col,
                    color=color_col,
                    hover_data=filter_df.columns,
                    title=f"{y_col} vs {x_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # --------------------------------------------------------
            # Line Chart
            # --------------------------------------------------------

            elif chart_type == "Line Chart":

                fig = px.line(
                    filter_df.sort_values(x_col),
                    x=x_col,
                    y=y_col,
                    color=color_col,
                    markers=True,
                    title=f"{y_col} vs {x_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # --------------------------------------------------------
            # Heatmap
            # --------------------------------------------------------

            elif chart_type == "Heatmap":

                corr = filter_df[numeric_cols].corr()

                fig = px.imshow(
                    corr,
                    text_auto=".2f",
                    color_continuous_scale="RdBu_r",
                    title="Correlation Heatmap"
                )

                fig.update_layout(height=650)

                st.plotly_chart(fig, use_container_width=True)

            # --------------------------------------------------------
            # Hexbin Style (Density Heatmap)
            # --------------------------------------------------------

            elif chart_type == "Hexbin Style":

                fig = px.density_heatmap(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    color_continuous_scale="Viridis",
                    title=f"Density of {x_col} and {y_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # --------------------------------------------------------
            # Trend Scatter
            # --------------------------------------------------------

            elif chart_type == "Trend Scatter":

                fig = px.scatter(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    color=color_col,
                    trendline="ols",
                    title=f"Relationship between {x_col} and {y_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)
        with composition:

            st.header("🥧 Composition Analysis")

            # ---------------- SETTINGS ----------------

            chart_type = st.selectbox(
                "Select Composition Chart",
                [
                    "Pie Chart",
                    "Donut Chart",
                    "Treemap",
                    "Sunburst",
                    "Funnel Chart",
                    "Stacked Bar Chart"
                ],
                key="composition_chart"
            )

            rows = st.slider(
                "Number of Records",
                min_value=10,
                max_value=len(df),
                value=min(200, len(df)),
                step=10,
                key="composition_rows"
            )

            filter_df = df.head(rows)

            category = st.selectbox(
                "Select Category",
                categorical_cols,
                key="comp_category"
            )

            value = st.selectbox(
                "Select Numeric Column",
                numeric_cols,
                key="comp_value"
            )

            comp_df = (
                filter_df.groupby(category)[value]
                .sum()
                .reset_index()
            )

            # ---------------------------------------------------
            # PIE CHART
            # ---------------------------------------------------

            if chart_type == "Pie Chart":

                fig = px.pie(
                    comp_df,
                    names=category,
                    values=value,
                    title=f"{value} Composition by {category}"
                )

                fig.update_traces(textinfo="percent+label")

                st.plotly_chart(fig, use_container_width=True)

            # ---------------------------------------------------
            # DONUT CHART
            # ---------------------------------------------------

            elif chart_type == "Donut Chart":

                fig = px.pie(
                    comp_df,
                    names=category,
                    values=value,
                    hole=0.45,
                    title=f"{value} Composition"
                )

                fig.update_traces(textinfo="percent+label")

                st.plotly_chart(fig, use_container_width=True)

            # ---------------------------------------------------
            # TREEMAP
            # ---------------------------------------------------

            elif chart_type == "Treemap":

                fig = px.treemap(
                    comp_df,
                    path=[category],
                    values=value,
                    color=value,
                    title=f"Treemap of {value}"
                )

                st.plotly_chart(fig, use_container_width=True)

            # ---------------------------------------------------
            # SUNBURST
            # ---------------------------------------------------

            elif chart_type == "Sunburst":

                fig = px.sunburst(
                    comp_df,
                    path=[category],
                    values=value,
                    title=f"Sunburst of {value}"
                )

                st.plotly_chart(fig, use_container_width=True)

            # ---------------------------------------------------
            # FUNNEL CHART
            # ---------------------------------------------------

            elif chart_type == "Funnel Chart":

                fig = px.funnel(
                    comp_df.sort_values(value, ascending=False),
                    x=value,
                    y=category,
                    title=f"{value} Funnel"
                )

                st.plotly_chart(fig, use_container_width=True)

            # ---------------------------------------------------
            # STACKED BAR CHART
            # ---------------------------------------------------

            elif chart_type == "Stacked Bar Chart":

                fig = px.bar(
                    comp_df,
                    x=category,
                    y=value,
                    color=category,
                    title=f"{value} by {category}"
                )

                fig.update_layout(barmode="stack")

                st.plotly_chart(fig, use_container_width=True)
        with correlation:

            st.header("📈 Correlation Analysis")

            # ---------------- SETTINGS ----------------

            chart_type = st.selectbox(
                "Select Correlation Chart",
                [
                    "Correlation Heatmap",
                    "Scatter Matrix",
                    "Pair Scatter",
                    "Bubble Correlation",
                    "Correlation Table"
                ],
                key="corr_chart"
            )

            rows = st.slider(
                "Number of Records",
                min_value=10,
                max_value=len(df),
                value=min(200, len(df)),
                step=10,
                key="corr_rows"
            )

            filter_df = df.head(rows)

            # -------------------------------------------------
            # CORRELATION HEATMAP
            # -------------------------------------------------

            if chart_type == "Correlation Heatmap":

                corr = filter_df[numeric_cols].corr()

                fig = px.imshow(
                    corr,
                    text_auto=".2f",
                    color_continuous_scale="RdBu_r",
                    aspect="auto",
                    title="Correlation Heatmap"
                )

                fig.update_layout(height=650)

                st.plotly_chart(fig, use_container_width=True)

            # -------------------------------------------------
            # SCATTER MATRIX
            # -------------------------------------------------

            elif chart_type == "Scatter Matrix":

                selected_cols = st.multiselect(
                    "Select up to 5 Numeric Columns",
                    numeric_cols,
                    default=numeric_cols[:4]
                )

                if len(selected_cols) >= 2:

                    fig = px.scatter_matrix(
                        filter_df,
                        dimensions=selected_cols,
                        color="Major_Category" if "Major_Category" in filter_df.columns else None,
                        title="Scatter Matrix"
                    )

                    fig.update_layout(height=700)

                    st.plotly_chart(fig, use_container_width=True)

                else:
                    st.warning("Please select at least 2 columns.")

            # -------------------------------------------------
            # PAIR SCATTER
            # -------------------------------------------------

            elif chart_type == "Pair Scatter":

                x_col = st.selectbox(
                    "X-Axis",
                    numeric_cols,
                    key="pair_x"
                )

                y_col = st.selectbox(
                    "Y-Axis",
                    numeric_cols,
                    index=1,
                    key="pair_y"
                )

                fig = px.scatter(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    color="Major_Category" if "Major_Category" in filter_df.columns else None,
                    trendline="ols",
                    title=f"{y_col} vs {x_col}"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # -------------------------------------------------
            # BUBBLE CORRELATION
            # -------------------------------------------------

            elif chart_type == "Bubble Correlation":

                x_col = st.selectbox(
                    "X-Axis",
                    numeric_cols,
                    key="bubble_x"
                )

                y_col = st.selectbox(
                    "Y-Axis",
                    numeric_cols,
                    index=1,
                    key="bubble_y"
                )

                size_col = st.selectbox(
                    "Bubble Size",
                    numeric_cols,
                    index=2,
                    key="bubble_size"
                )

                fig = px.scatter(
                    filter_df,
                    x=x_col,
                    y=y_col,
                    size=size_col,
                    color="Major_Category" if "Major_Category" in filter_df.columns else None,
                    hover_data=filter_df.columns,
                    title="Bubble Correlation"
                )

                fig.update_layout(height=550)

                st.plotly_chart(fig, use_container_width=True)

            # -------------------------------------------------
            # CORRELATION TABLE
            # -------------------------------------------------

            elif chart_type == "Correlation Table":

                corr = filter_df[numeric_cols].corr().round(2)

                st.dataframe(
                    corr,
                    use_container_width=True,
                    height=500
                )








elif opt == "About":
    st.markdown("""
<style>

/* ---------- Main Background ---------- */
.stApp{
    # background: linear-gradient(135deg,#0f172a,#1e293b,#0f172a);
}

/* ---------- Headers ---------- */
h1{
    color:#4FC3F7;
    text-align:center;
    font-weight:800;
}

h2,h3{
    color:white;
}

/* ---------- Paragraph ---------- */
p{
    color:#d1d5db;
    font-size:17px;
}

/* ---------- Metric Cards ---------- */
div[data-testid="metric-container"]{
    background:#1E293B;
    border-radius:15px;
    padding:20px;
    border:1px solid #334155;
    box-shadow:0 5px 15px rgba(0,0,0,0.35);
    transition:0.3s;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-5px);
    border:1px solid #38BDF8;
}

/* ---------- Info / Success ---------- */
div[data-testid="stAlert"]{
    border-radius:12px;
}

/* ---------- Divider ---------- */
hr{
    border:1px solid #334155;
}

/* ---------- Buttons ---------- */
.stButton>button{
    width:100%;
    border-radius:10px;
    background:#2563EB;
    color:white;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* ---------- Cards ---------- */
.about-card{
    background:#1E293B;
    padding:25px;
    border-radius:15px;
    color:white;
    border-left:6px solid #38BDF8;
    margin-bottom:20px;
    box-shadow:0 5px 15px rgba(0,0,0,.3);
}

/* ---------- Footer ---------- */
.footer{
    text-align:center;
    color:#9CA3AF;
    margin-top:40px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

    st.title("ℹ️ About This Project")

    st.markdown("""
    ## 🎓 AI Impact on Students Dashboard

    This project analyzes how Artificial Intelligence (AI) tools influence
    students' learning, academic performance, study habits, and overall
    educational experience through interactive visualizations.
    """)

    st.divider()

    st.subheader("🎯 Project Objectives")

    st.markdown("""
    - Analyze AI usage among students.
    - Compare students' academic performance.
    - Study AI dependency and study habits.
    - Explore burnout and anxiety levels.
    - Discover relationships between variables.
    - Present insights using interactive charts.
    """)

    st.divider()

    st.subheader("📊 Dashboard Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        ✔ Distribution Analysis

        ✔ Comparison Analysis

        ✔ Relationship Analysis
        """)

    with col2:
        st.info("""
        ✔ Composition Analysis

        ✔ Correlation Analysis

        ✔ Summary Dashboard
        """)

    st.divider()

    st.subheader("📂 Dataset Information")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Records", len(df))

    with c2:
        st.metric("Features", len(df.columns))

    with c3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    st.divider()

    st.subheader("🛠️ Technologies Used")

    st.markdown("""
    - 🐍 Python
    - 🎈 Streamlit
    - 📊 Plotly
    - 🐼 Pandas
    - 🔢 NumPy
    """)

    st.divider()

    st.subheader("📌 Project Modules")

    st.markdown("""
    - 📊 Distribution Analysis
    - 📈 Comparison Analysis
    - 🔗 Relationship Analysis
    - 🥧 Composition Analysis
    - 📉 Correlation Analysis
    - 📋 Summary Report
    """)

    st.divider()

    st.success("✅ AI Impact on Students Dashboard | Developed using Python, Streamlit & Plotly.")        
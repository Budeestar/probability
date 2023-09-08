from pathlib import Path

import streamlit as st


current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"



PAGE_TITLE = "Statistical Data mining (Written by your ENVY)"
PAGE_ICON = "random"
NAME = "Statistical Data mining"
DESCRIPTION = """
This is a web page created and updated daily based on the topics discussed during the class.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("NV's page")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
BOOK = {
    "Introduction to Statistical learning": "https://github.com/ENVY0010/datamining/blob/main/An%20Introduction%20To%20Statistical%20Learning%20with%20Applications%20in%20R%20(ISLR%20Seventh%20Printing).pdf",
    "Elements of statistical learning":"https://github.com/ENVY0010/datamining/blob/main/The%20Elements%20of%20Statistical%20Learning%20-%20Data%20Mining%2C%20Inference%20and%20Prediction%20-%202nd%20Edition%20(ESLII_print4).pdf",
    }
GITHUB_R_DOCUMENT = {
    "R_files": "Currently not available.",
}

SUMMARY_DOC={
    "SUMMARY":"https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3162758/View",
    }
st.title(NAME)
st.write('\n')
cols = st.columns(len(BOOK))
for index, (book, link) in enumerate(BOOK.items()):
    cols[index].write(f"[{book}]({link})")

st.write('\n')
st.subheader("Day-1 (29 Aug 2023)")

st.write("""
    An Introduction to the class and a summary of what we people will be doing or working on in the whole semester!. Its just an overview
    Refer to the document below.
""")
cols = st.columns(len(SUMMARY_DOC))
for index, (summary, link) in enumerate(SUMMARY_DOC.items()):
    cols[index].write(f"[{summary}]({link})")
st.write('\n')
st.subheader("Required softwares and others (gradescope)")
st.write('\n')
st.write("""
     Before this lets download R and make it work on our local machine.
     
     Download [R_for_windows](https://cran.r-project.org/bin/windows/base/)
""")

st.write("""
     Download [R_for_MAC](https://cran.r-project.org/bin/macosx/big-sur-arm64/base/R-4.3.1-arm64.pkg)
    
""")

st.write("""
     Assignments will be graded on [gradescope](https://gradescope.wistia.com/medias/oljo3t2hsy)
    
""")

st.subheader("Day-2 31 Aug 2023)")

st.write('\n')
st.write("""
    What is data mining: Tools, methodologies and theories for revealing patterns in the data.(In short, it is the use of tools and technologies to find patterns from a large dataset)
    Types:
    Descriptive Data mining:finding unexpected structures or relationships, patterns, trends, clusters, and outliers in the data.
    predictive data mining: regression, classification, pattern recognition, or machine learning tasks, and assess the predictive accuracy or those models and procedures when applied to fresh data
""")

st.write('\n')
st.write("""
    Supervised and unsupervised learning.
""")
st.write("""
    What is a Data Scientist?:It is a science which involves analysis and identify patterns and create models.
""")

st.write("\n")
st.write("""
    Knowledge Discovery in Databases (KDD):
    1. Finding dataset
    2. cleaning the data
    3. preprocessing the data
    4. decide the technique
    5. create model and analyse the results
""")
st.write("""
    Analyst should look for:
    1. Outliers of the data
    2. Missing values
    3. finding clusters.
    4. finding patterns.
    5. find the trends associated with the order of data collection.
""")

st.write("\n")
st.write("""
    Exploratory Data Analysis (EDA) to describe the use of graphs to display and help understand data.
    example: histogram, box plot,
    \n
    Views of groups of data: Univariate and bivariate data.
    \n
    density plots between two variables
    \n
    finding two variables for plots
    \n
    box plot: InterQuartileRange(IQR), lower quartile, median, upper quartile, lies from lowerquartile-1.5IQR to upperquartile+1.5IQR. Data points which doesnot lie in this are called outliers.
""")

st.write("\n")
st.write("""
     find more details and ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3149757/View)
""")
st.write("Day-3")
st.write("\n")
st.write("""
     refer to ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3225529/View)\n
     no further explanation needed.
""")


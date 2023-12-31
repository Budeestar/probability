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
    What is data mining: Tools, methodologies and theories for revealing patterns in the data.(In short, it is the use of tools and technologies to find patterns from a large dataset).\n
    Types:\n
    Descriptive Data mining:finding unexpected structures or relationships, patterns, trends, clusters, and outliers in the data.\n
    predictive data mining: regression, classification, pattern recognition, or machine learning tasks, and assess the predictive accuracy or those models and procedures when applied to fresh data.\n
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
st.subheader("Day-3")
st.write("\n")
st.write("""
     refer to ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3225529/View)\n
     no further explanation needed.
""")

st.subheader("Day -4")
st.write("\n")
st.write("""
     Linear Regression for advertising and sales data and maths behind linear regression. \n
     How to find errors and minimize the error....\n
     find the coefficinet and the constant value...\n
     Error formulas and other formulas.\n
     Theory and math behind the linea regression and multiple linear regression. \n
     for details please find ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3405718/View) for this week
     
""")

st.subheader("Day -5")
st.write("\n")

st.write("""
    Gram-Schmidt-orthogonalization.\n
    It is based on orthogonalisation where the dot product is 0.
    the vectors (z1=X1-X) and the dot product of Xi*Yi/Xi*Xi is 0
    but practically it is not possible.\n
    based on the summation of Xi*Yi/Xi*Xi gives us the coefficient.\n
    Gauss Markov theorem similar to above
    assuming linear model is true and the constant is zero.\n
    Do model selection using 2 methods.\n
    1.forward selection -(0 predictors, 1 predictors.... n predictors)\n
    2.backward selection -(n predictors, n-1 predictors..... 1 predictor)\n
    taking factors or parameters into consideration for regression. \n
    for categorical do one hot encoding.\n
    same for multi linear regression.\n
    Taking persons from different continents 
    example: y=m1x1+m2x2..... m1 for african, m2 for american.....\n
    Interpretation of model.\n
    plotting the graphs, manly surface graphs..\n
    
    for details please find ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3405718/View) for this week
    
""")

st.subheader("Day -6")
st.write("\n")

st.write("""
    collinearity: refers to situation where two variables are closely related(predictor variables)\n
    It is greater than 1 \n
    check VIF formula form slides where R^2 = mean square error.\n
    refer to the slides [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3405718/View) for this week
    subset selection and interpretation.\n
    choosing the optimal model with less RSS and more R^2 for training error because model with low training error does well with prediction.\n
    so for more featires RSS and R^2 are not suitable.\n
    Estimate test errors:\n
    refer to ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3551522/View)\n
    mallow's cp and AIC should be low for better prediction where in the case the "L" value should be more.\n
    BIC (check details of BIC in the above ppt)\n
    mallows cp, AIC, BIC should be less for better prediction and model\n
    Adjusted R^2 (checkppt) should be more for better model.\n
    approaches for better models:
    subset selection,
    shrinkage,
    dimension reduction.\n
    Ways of subset selection:\n
    1. Exhaustive --based of forward selection select number of predictors with smallest RSS and large R^2--- loop in for different k values and select k value.\n 
    2. leaps and bounds algorithm.---- plot RSS and sub set size and based on graph select the number of predictors.\n
    3. forward stepwise.--- specify k value explicitly.\n
    4. backward stepwise.(check ppt for difference between exhaustive and forward stepwise.)\n

    Check the R code for better understanding.
    
""")

st.subheader("Day -7")
st.write("\n")

st.write("""
    Model Selection:\n
    K-fold cross validation.\n
    penalized regression--> LASSO regression and RIDGE regression(shrinkage methods)\n
    
    refer to ppt [here](https://ublearns.buffalo.edu/d2l/le/content/125941/viewContent/3557692/View)
    
""")

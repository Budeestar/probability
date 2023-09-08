from pathlib import Path

import streamlit as st


current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
#st.title("Probability and data analysis")


PAGE_TITLE = "Probability and data analysis (Written by your ENVY)"
PAGE_ICON = "random"
NAME = "Probability and data analysis"
DESCRIPTION = """
This is a web page created and updated daily based on the topics discussed during the class.
"""

EMAIL="jamesliv@buffalo.edu"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("NV's page")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

BOOK = {
    "A Fresh Approach Using R": "https://mathstat.slu.edu/~speegle/_book/preface.html",
    }
GITHUB_R_DOCUMENT = {
    "R_files": "Currently not available.",
}
GITHUB_R_DOCUMENT = {
    "R_files": "Currently not available.",
}
SUMMARY_DOC={
    "SUMMARY":"https://ublearns.buffalo.edu/d2l/le/content/107411/viewContent/3223725/View",
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

st.subheader("Day-2 31 Aug 2023)")
st.write('\n')
st.subheader("Introduction to R")
st.write('\n')
st.write("""
     Before this lets download R and make it work on our local machine.
     
     Download [R_for_windows](https://cran.r-project.org/bin/windows/base/)
""")

st.write("""
     Download [R_for_MAC](https://cran.r-project.org/bin/macosx/big-sur-arm64/base/R-4.3.1-arm64.pkg)
    
""")

st.write("""
     Please find the [R](https://github.com/ENVY0010/R/blob/main/R_1_310823.R) file for the first day.
    
""")


st.subheader("Day-3&4 both 5 sep & 7 sep 2023)")
st.write('\n')

st.subheader("Basics of probability using R")
st.write('\n')
st.write("""
    Probability basics
    - An experiment is a process that produces an observation.
- An outcome is a possible observation.
- The set of all possible outcomes is called the sample space.
- An event is a subset of the sample space.
- A trial is a single running of an experiment.
""")


st.write('\n')
st.write("""
    refer to sets venn diagrams for detailed understanding of probability.
""")
st.write('\n')
st.write("""
    refers to the pics for axioms \n
    [probability-1](https://github.com/ENVY0010/R/blob/main/probability-1.PNG) \n
    [probability-2](https://github.com/ENVY0010/R/blob/main/probability-2.PNG) \n
    [probability-3](https://github.com/ENVY0010/R/blob/main/probability-3.PNG) \n
    [probability-4](https://github.com/ENVY0010/R/blob/main/probability-4.PNG) \n
    refer to [conditional probability](https://mathstat.slu.edu/~speegle/_book/probchapter.html#simulating-conditional-probability) \n
    refer to r file on [sep-5](https://github.com/ENVY0010/R/blob/main/20230905-probability.R) \n
    refer to r file on [sep-7](https://github.com/ENVY0010/R/blob/main/20230907.R) \n
""")

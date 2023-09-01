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
     Please find the R file for the first day.
    
""")






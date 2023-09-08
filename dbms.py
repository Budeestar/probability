from pathlib import Path

import streamlit as st


current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
#st.title("Probability and data analysis")


PAGE_TITLE = "DBMS (Written by your ENVY)"
PAGE_ICON = "random"
NAME = "DBMS"
DESCRIPTION = """
This is a web page created and updated daily based on the topics discussed during the class.
"""
EMAIL="cckeaton@buffalo.edu"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("NV's page")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

BOOK = {
    "Modern Database Management": "https://drive.google.com/file/d/1oP1d6X0cw1-J-ZpOkeUx-V5ooCSePeMz/view?usp=sharing",
    }
st.title(NAME)

st.write('\n')
cols = st.columns(len(BOOK))
for index, (book, link) in enumerate(BOOK.items()):
    cols[index].write(f"[{book}]({link})")
    
st.write('\n')
st.subheader("Day-1 (30 Aug 2023)")

st.write("""
    An Introduction to the class and a summary of what we people will be doing or working on in the whole semester!. Its just an overview
    Refer to the document [here](https://ublearns.buffalo.edu/d2l/le/content/142289/viewContent/3127460/View)

    refer below for [KEY_TERMINOLOGY](https://ublearns.buffalo.edu/d2l/le/content/142289/viewContent/3127445/View)
    
""")

st.write('\n')
st.subheader("WEEK-2 ")

st.write("""
    Discussed on AGILE and WATERFALL models.
    refer to the document [here](https://ublearns.buffalo.edu/d2l/le/content/142289/viewContent/3127446/View)
    
""")

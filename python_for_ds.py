from pathlib import Path

import streamlit as st


current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
#st.title("Python for Data science")


PAGE_TITLE = "Programming DB Data science (Written by your ENVY)"
PAGE_ICON = "random"
NAME = "Programming for Data science"
DESCRIPTION = """
This is a web page created and updated daily based on the topics discussed during the class.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("NV's page")
BOOK = {
    "EAS_503_github": "https://mkzia.github.io/eas503-book/chapters/01/fundamentals.html",
    }
st.title(NAME)
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
st.write('\n')
st.subheader("Day-1 (29 Aug 2023)")
st.write("""
    An Introduction to the class and detailed discussion on some of the to-do things
""")
st.write('\n')
st.write("""
    1. Access to UBLearns.
    2. Course book access on [this](https://mkzia.github.io/eas503-book/chapters/01/fundamentals.html).
    3. Create account on Codio (Paid account of 48 USD) using this [invite](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcodio.com%2Fp%2Fsignup%3FcourseToken%3Dharmony-basic&data=05%7C01%7Cnithinya%40buffalo.edu%7C57abe353967946c65a7808dba8a753f4%7C96464a8af8ed40b199e25f6b50a20250%7C0%7C0%7C638289208857596159%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=en50VZ2XL5QkqIEFkuFBdJMOGy3MuMNqCKUFKgNT2gQ%3D&reserved=0)
    4. Piazza [login](https://piazza.com/first_login?token=3karDDOTmZ0&mc_id=pw_2)(engaging course discussion, ask questions).
    5. Anaconda Installation - Individual Edition from [here](https://www.anaconda.com/blog/anaconda-individual-edition-2021-11)
    6. Install [VSCode](https://code.visualstudio.com/download) based on Windows, MAC.
    7. Install Python [IDE](https://www.python.org/downloads/)
    8. Download lockdown browser for quizzes and assignments.
""")

st.write('\n')
st.write("""
    Refer to the [repo](https://github.com/mkzia/eas503/tree/master/week1)
""")

st.write('\n')
st.subheader("Day-2 (31 Aug 2023)")
st.write('\n')
st.write("""
    Basics of python on Arithmetic, Numeric operators and small functions. Details on (/ , // ,%) operators.
    Types(int, float and others)
    getsizeof() for getting size.
    inbuilt statements (example: print, pi...)
    swapping of two elements.
    defining and calling functions.(squaring, Simple intrest,...)
    ceiling and flooring.

    Refer to the ipynb [here](https://github.com/mkzia/eas503/blob/master/week1/week1_b.ipynb).
""")

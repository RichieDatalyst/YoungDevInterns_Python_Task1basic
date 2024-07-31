import streamlit as st

#personal information

st.title("Ameer Abdullah")
st.caption("Junior Data Scientist")
st.write("")
st.write("📧 [abcxyz@gmail.com](mailto:abcxyz@gmail.com)")
Social_Media = {
  "LinkedIn" : "https://linkedin.com/in/ameer-abdullah-502955294",
  "Github" : "https://github.com/RichieDatalyst"
}

num_columns = st.columns(len(Social_Media))
for i, (platform, link) in enumerate(Social_Media.items()):
        num_columns[i].write(f"{platform}: [{link}]({link})")


#Educational Information
st.header("Education")
st.title("Bs Data Science")
st.caption("Fast Nuces Lahore")
st.write("I am a motivated Data Science student from Fast-NUCES Lahore, skilled in harnessing data for insights and driving advancements in AI and machine learning. My academic journey has honed my ability to unravel intricate patterns. I thrive in dynamic environments and aspire to collaborate with like-minded professionals for a positive global impact.")

#CSS Styles
st.markdown(
    """
    <style>
    .box {
        color: white;
        display: inline-block;
        border: 2px solid black;
        border-radius: 12px;
        padding: 6px 8px;
        margin: 5px;
        background-color: black;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Languages")
languages = ["Urdu", "English"]
language_boxes = "".join([f'<span class="box">{language}</span>' for language in languages])
st.markdown(language_boxes, unsafe_allow_html=True)

#Skills
st.header("Skills")
skills = ["Leadership", "Artificial Intelligence", "Machine Learning", "Python", "SQL", 
          "C++", "Big Data Analytics", "Deep Learning", "Analytical Thinking", "Data Analysis and Visualization"]

skills_boxes = "".join([f'<span class="box">{skill}</span>' for skill in skills])

st.markdown(skills_boxes, unsafe_allow_html=True)

st.header("Projects")
projects = {
    "AI Intelligent Snake Solver": "Developed an AI-powered Snake game using A*, Greedy Best First, and BFS algorithms for optimized pathfinding.",
    "Cricket Data Analytics": "Analyzed cricket data to identify the top 15 modern-day players who could form an unbeatable team using data visualization techniques.",
    "Inventory Management System": "Developed an object-oriented inventory management system with classes for products and stock levels, featuring functionalities for tracking inventory, managing reorder points, and generating reports.",
    "Friendship Network Analyzer": "Designed an object-oriented program to analyze and visualize friendship networks, identifying key individuals and analyzing network structure.",
    "Dots and Boxes Game using minimax algorithm": "Implemented the 'Make Squares' game using the MINIMAX algorithm, featuring game state management, heuristic evaluation, and AI decision-making."
}

for project, description in projects.items():
    st.subheader(project)
    st.write(description)







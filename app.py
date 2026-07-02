import streamlit as st
from config import APP_TITLE
from llm import generate_response


def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🎓",
        layout="centered"
    )
    st.title(APP_TITLE)
    st.write(
        "Generate a personalized learning plan with the help of Artificial Intelligence."
    )
    st.divider()
    topic = st.text_input(
        "Enter a topic",
        placeholder="For example: Machine Learning"
    )
    level = st.radio(
        "Select your current level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )
    goal = st.selectbox(
        "Learning goal",
        [
        "Learn from scratch",
        "Prepare for interview",
        "Prepare for exam",
        "University course"
        ]
    )
    generate_button = st.button("Generate study plan")

    with st.spinner("AI is generating your study plan..."):
        answer = generate_response(topic)
    with st.container():
        st.markdown(answer)









if __name__ == "__main__":
    main()
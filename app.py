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
    st.markdown(
    """
    Generate a personalized study plan with the help of AI.

    Choose your topic, current level and learning goal, then let the assistant create a structured roadmap for your learning.
    """
)
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
    generate_button = st.button(
         "🚀 Generate Study Plan",
        use_container_width=True
    )

    if generate_button:

        if not topic:
            st.warning("⚠️ Please enter a study topic.")

        else:
            with st.spinner("AI is generating your study plan..."):
                answer = generate_response(
                    topic,
                    level,
                    goal
                )

            with st.container():
                st.divider()
                st.subheader("📚 Your Personalized Study Plan")
                st.markdown(answer)

    with st.sidebar:

        st.header("About")
        st.write(
            """
            AI Study Assistant helps students create structured learning plans using Large Language Models.

            Technologies

            • Python 3.13

            • Streamlit

            • OpenRouter API

            • Large Language Models (LLMs)

            • Prompt Engineering
            """
        )
        









if __name__ == "__main__":
    main()
import streamlit as st
import openai

openai.api_key =  st.secrets["mykey"]

# Define neutral product features, benefits, pain points, and desires
product_features = ["heart rate monitoring", "sleep tracking", "GPS", "sleep tracking, GPS, personalized workout recommendations"]
product_benefits = ["Convenience", "Accurate Tracking for Progress Monitoring", "Improved Sleep Quality", "Energy efficiency", "Seamless Integration"]
target_audience = ["Fitness enthusiasts who are serious about their training and looking for data-driven insights"]
pain_points = ["Optimize Training", "Lack of Personalization", "Time constraints", "Overtraining/Undertraining"]
desires = ["Accurate Data", "Improve Performance", "Achieve Fitness Goals", "Personalized Guidance"]
channels = ["Instagram", "Facebook", "Twitter", "Email"]
tones = ["Casual", "Informative", "Enthusiastic", "Humorous", "Inspirational"]

# Function to generate marketing copy
def generate_copy(product_name, product_features, product_benefits, target_audience, pain_points, desires, channel, tone):
    prompt = f"""
    You're a marketing copywriter. Write a {channel} post caption and image description to promote the {product_name}, a new smart PulseActive.

    **Target audience:** {target_audience}

    **Highlight:**
    * Key features: {', '.join(product_features)}
    * Benefits: {', '.join(product_benefits)}
    * Address these pain points: {', '.join(pain_points)}
    * Appeal to these desires: {', '.join(desires)}

    **Tone:** {tone}

    **Image description:** A close-up shot of the {product_name} fitness tracker displaying key metrics like heart rate and steps. The background should be a clean, modern design, perhaps with subtle digital elements. The image should convey a sense of precision, data-driven insights, and advanced technology.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing copywriter."},
            {"role": "user", "content": prompt}
        ]
    )
    copy = response['choices'][0]['message']['content']
    caption, image_description = copy.split("\n\n")
    return caption, image_description

# Streamlit UI
st.title("Health Smart PulseActive")

product_name = st.text_input("Product Name:", value="Smart PulseActive Pro")
selected_features = st.multiselect("Product Features:", product_features)
selected_benefits = st.multiselect("Product Benefits:", product_benefits)
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)
selected_channel = st.selectbox("Channel:", channels)
selected_tone = st.selectbox("Tone:", tones)

if st.button("Generate Marketing Copy"):
    caption, image_description = generate_copy(product_name, selected_features, selected_benefits, selected_audience, selected_pain_points, selected_desires, selected_channel, selected_tone)
    st.subheader("Caption:")
    st.write(caption)
    st.subheader("Image Description:")
    st.write(image_description)

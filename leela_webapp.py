import streamlit as st
import google.generativeai as genai

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("Google API-sleutel niet gevonden. Zorg ervoor dat je de GOOGLE_API_KEY hebt ingesteld in de Streamlit Secrets.")
    st.stop()

def generate_ai_lesson(niveau, les, hero):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt = f"""Jij bent een vriendelijke en creatieve leraar Nederlands voor NT2-studenten...""" # (rest van de prompt is hetzelfde)
    with st.spinner(f"✨ Magie in de maak..."):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Oeps, er ging iets mis bij het aanroepen van de Google AI: {e}"

st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")

# (De rest van de interface-code blijft exact hetzelfde)
with st.sidebar:
    st.header("1. Gegevens van de Student")
    # ... (alle input velden)

if st.sidebar.button("🚀 Genereer Les met AI! 🚀"):
    hero_data = { ... } # (data verzamelen)
    generated_lesson = generate_ai_lesson(gekozen_niveau, gekozen_les, hero_data)
    st.markdown(generated_lesson)
else:
    st.info("...")

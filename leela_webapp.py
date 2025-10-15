import streamlit as st
import google.generativeai as genai

# ===================================================================
# CONFIGURATIE - Verbind de app met de Google AI-motor
# ===================================================================
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("Google API-sleutel niet gevonden. Zorg ervoor dat je de GOOGLE_API_KEY hebt ingesteld in de Streamlit Secrets.")
    st.stop()

# ===================================================================
# DE AI-GENERATOR FUNCTIE (MET DE JUISTE MODELNAAM)
# ===================================================================
def generate_ai_lesson(niveau, les, hero):
    """Bouwt een prompt en roept de Gemini AI aan om een les te genereren."""
    
    # --- DE ALLERLAATSTE FIX: Het meest stabiele en universele model ---
    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""
    Jij bent een vriendelijke en creatieve leraar Nederlands voor NT2-studenten.
    Jouw taak is om een korte, gepersonaliseerde en motiverende les te genereren op {niveau}-niveau.

    **Gegevens van de student:**
    - Naam: {hero['name']}
    - Leeftijd: {hero['age']}
    - Land van herkomst: {hero['country']}
    - Rol of Missie: {hero['occupation']}

    **Instructies voor de les:**
    1.  **Lesonderwerp:** "{les}".
    2.  **Structuur:** De les moet de volgende onderdelen bevatten, in deze volgorde:
        - Een korte, duidelijke **Theorie** met NT2-termen (bv. subject, verbum).
        - Een relevante **Woordenschat**-tabel (Nederlands/Engels).
        - Een **Praktische Oefening** met 3-5 zinnen die relevant zijn voor de rol/missie van de student.
    3.  **Toon:** De toon moet positief, aanmoedigend en creatief zijn, in de stijl van Leela (spel van zelfkennis) en levenskunst. Spreek de student direct aan met 'jij' en 'jouw'.
    4.  **Opmaak:** Gebruik Markdown voor de opmaak. Gebruik headers (##), subheaders (###), vetgedrukte tekst en tabellen.

    Genereer nu de les.
    """

    with st.spinner(f"✨ Magie in de maak... Ik genereer een les over '{les}' voor {hero['name']}..."):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Oeps, er ging iets mis bij het aanroepen van de Google AI: {e}"

# ===================================================================
# DE STREAMLIT INTERFACE (ONGEWIJZIGD)
# ===================================================================
st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")

with st.sidebar:
    st.header("1. Gegevens van de Student")
    gender = st.selectbox("Aanspreekvorm", ["vrouwelijk (ze/haar)", "mannelijk (hij/zijn)", "neutraal (die/hun)"])
    name = st.text_input("Naam", "Garsett")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=62)
    country = st.text_input("Land van herkomst", "België")
    occupation = st.text_input("Rol of Missie", "leraar levenskunst")
    
    st.markdown("---")
    st.header("2. Kies je Les")
    
    gekozen_niveau = st.selectbox("Niveau", ["A1", "A2", "B1"])
    
    les_onderwerpen = [
        "👋 Kennismaken (jezelf voorstellen)",
        "🏡 Familie & vrienden",
        "🕰️ De tijd (klok, dagen, seizoenen)",
        "🛒 Winkelen (prijzen, vragen)",
        "💼 Werk & Studie (dagelijkse taken)",
        "📘 Grammatica: Subject & Verbum",
        "📘 Grammatica: De/Het lidwoorden"
    ]
    gekozen_les = st.selectbox("Kies een lesonderwerp", les_onderwerpen)

if st.sidebar.button("🚀 Genereer Les met AI! 🚀"):
    hero_data = {
        "name": name, "age": age, "country": country, "occupation": occupation, "gender": gender
    }
    
    generated_lesson = generate_ai_lesson(gekozen_niveau, gekozen_les, hero_data)
    st.markdown(generated_lesson)
    
else:
    st.info("Vul links je gegevens in, kies een les en klik op de knop om jouw unieke AI-les te genereren!")

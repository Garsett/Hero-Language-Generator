import streamlit as st
import openai

# ===================================================================
# CONFIGURATIE - Verbind de app met de OpenAI-motor
# ===================================================================
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except Exception as e:
    st.error("OpenAI API-sleutel niet gevonden. Zorg ervoor dat je de OPENAI_API_KEY hebt ingesteld in de Streamlit Secrets.")
    st.stop()

# ===================================================================
# DE NIEUWE AI-GENERATOR FUNCTIE (MET OPENAI)
# ===================================================================
def generate_ai_lesson(niveau, les, hero):
    """Bouwt een prompt en roept de OpenAI AI aan om een les te genereren."""

    system_prompt = """Jij bent een vriendelijke en creatieve leraar Nederlands voor NT2-studenten. Jouw taak is om een korte, gepersonaliseerde en motiverende les te genereren. De toon moet positief, aanmoedigend en creatief zijn, in de stijl van Leela (spel van zelfkennis) en levenskunst. Spreek de student direct aan met 'jij' en 'jouw'. Gebruik Markdown voor de opmaak (headers, tabellen, etc.)."""
    
    user_prompt = f"""
    Genereer een les op **{niveau}-niveau** over het onderwerp **"{les}"**.

    **Gegevens van de student:**
    - Naam: {hero['name']}
    - Leeftijd: {hero['age']}
    - Land van herkomst: {hero['country']}
    - Rol of Missie: {hero['occupation']}

    **Structuur van de les:**
    1.  Een korte, duidelijke **Theorie** met NT2-termen (bv. subject, verbum).
    2.  Een relevante **Woordenschat**-tabel (Nederlands/Engels).
    3.  Een **Praktische Oefening** met 3-5 zinnen die relevant zijn voor de rol/missie van de student.
    """

    with st.spinner(f"✨ Magie in de maak... Ik genereer een les over '{les}' voor {hero['name']}..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Oeps, er ging iets mis bij het aanroepen van de OpenAI AI: {e}"

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
    
    # --- DE FIX IS HIER: We geven nu alle 3 de argumenten correct door ---
    generated_lesson = generate_ai_lesson(gekozen_niveau, gekozen_les, hero_data)
    st.markdown(generated_lesson)
    
else:
    st.info("Vul links je gegevens in, kies een les en klik op de knop om jouw unieke AI-les te genereren!")

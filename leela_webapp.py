import streamlit as st
import random
import json

# ===================================================================
# DEFINITIES EN DATA INLADEN
# ===================================================================
class HeroProfile:
    def __init__(self, name, age, country, occupation, gender):
        self.name = name
        self.age = age
        self.country = country
        self.occupation = occupation
        self.gender = gender

def load_leerstof():
    """Laadt de lesstof uit het externe JSON-bestand."""
    with open('leerstof.json', 'r') as f:
        return json.load(f)

# Laad de database bij het starten van de app
leerstof_database = load_leerstof()

# ===================================================================
# DE OEFENING-GENERATORS - MET TABEL-ONDERSTEUNING
# ===================================================================
def generate_vocabulary_exercise(hero, niveau, thema):
    data = leerstof_database[niveau]["themas"][thema]
    st.header(f"Les (Niveau {niveau}): {thema}", divider='rainbow')
    
    st.subheader("1. Theorie")
    st.info(data["uitleg"])

    # Controleer of er een tabel is en toon deze
    if "tabel" in data:
        st.markdown(data["tabel"])

    st.subheader("2. Woordenschat")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Nederlands**")
        for nl in data["vocab"].keys():
            st.write(nl)
    with col2:
        st.write("**Engels**")
        for en in data["vocab"].values():
            st.write(en)

    st.subheader("3. Praktische Oefening")
    st.write("Lees de volgende zinnen hardop:")
    for zin in data["oefenzinnen"]:
        zin = zin.replace("{naam}", hero.name).replace("{leeftijd}", str(hero.age)).replace("{land}", hero.country).replace("{beroep}", hero.occupation)
        st.write(f"- {zin}")

def generate_grammar_exercise(hero, niveau, onderwerp):
    data = leerstof_database[niveau]["grammatica"][onderwerp]
    st.header(f"Les (Niveau {niveau}): {onderwerp}", divider='rainbow')

    st.subheader("1. Theorie")
    st.info(data["uitleg"])
    
    st.subheader("2. Praktische Oefening")
    st.write("Maak de zinnen af of zet de woorden in de juiste volgorde:")
    for i, zin in enumerate(data["oefening"]):
        zin = zin.replace("{naam}", hero.name)
        st.write(f"{i+1}. {zin}")
        
    with st.expander("Klik hier voor de antwoorden"):
        antwoorden = [ant.replace("{naam}", hero.name) for ant in data["antwoorden"]]
        st.write(antwoorden)

# ===================================================================
# DE STREAMLIT INTERFACE
# ===================================================================
st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")

with st.sidebar:
    st.header("1. Gegevens van de Student")
    gender = st.selectbox("Aanspreekvorm", ["vrouwelijk (ze/haar)", "mannelijk (hij/zijn)", "neutraal (die/hun)"])
    name = st.text_input("Naam", "Garsett")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=62)
    country = st.text_input("Land", "België")
    occupation = st.text_input("Beroep", "leraar levenskunst")
    
    st.markdown("---")
    st.header("2. Kies je Les")
    
    gekozen_niveau = st.selectbox("Niveau", list(leerstof_database.keys()))
    
    if gekozen_niveau:
        type_keuzes = ["-- Kies een type --"] + list(leerstof_database[gekozen_niveau].keys())
        gekozen_type = st.selectbox("Oefeningstype", type_keuzes)
        
        if gekozen_type and gekozen_type != "-- Kies een type --":
            les_keuzes = ["-- Kies een les --"] + list(leerstof_database[gekozen_niveau][gekozen_type].keys())
            gekozen_les = st.selectbox("Les", les_keuzes)

if st.sidebar.button("🚀 Genereer Oefening! 🚀"):
    hero = HeroProfile(name=name, age=age, country=country, occupation=occupation, gender=gender)

    if 'gekozen_les' in locals() and gekozen_les != "-- Kies een les --":
        if gekozen_type == "themas":
            generate_vocabulary_exercise(hero, gekozen_niveau, gekozen_les)
        elif gekozen_type == "grammatica":
            generate_grammar_exercise(hero, gekozen_niveau, gekozen_les)
    else:
        st.warning("Maak alsjeblieft een volledige keuze in de sidebar (Niveau > Type > Les).")
else:
    st.info("Vul links je gegevens in, kies een volledige les en klik op 'Genereer Oefening!'")

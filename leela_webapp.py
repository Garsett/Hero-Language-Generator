import streamlit as st
import random
import json

# ===================================================================
# DEFINITIES EN DATA INLADEN
# ===================================================================
class HeroProfile:
    def __init__(self, name, age, country, occupation, gender):
        self.name = name; self.age = age; self.country = country; self.occupation = occupation; self.gender = gender

def load_leerstof():
    with open('leerstof.json', 'r', encoding='utf-8') as f:
        return json.load(f)

leerstof_database = load_leerstof()

# ===================================================================
# DE OEFENING-GENERATORS - MET FIX VOOR NULL-WAARDEN
# ===================================================================
def generate_thema_exercise(hero, niveau, thema):
    data = leerstof_database[niveau]["themas"][thema]
    st.header(f"Les (Niveau {niveau}): {thema}", divider='rainbow')

    if "uitleg_sv" in data:
        st.subheader("1. Theorie: Subject & Verbum"); st.info(data["uitleg_sv"])
    if "tabel_persoonlijk" in data:
        st.markdown(data["tabel_persoonlijk"])
    if "oefenzinnen_sv" in data:
        st.write("Lees de volgende zinnen hardop:")
        for zin in data["oefenzinnen_sv"]:
            zin = zin.replace("{naam}", hero.name).replace("{leeftijd}", str(hero.age)).replace("{land}", hero.country)
            st.write(f"- {zin}")
    if "vocab" in data:
        st.subheader("2. Woordenschat")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Nederlands**")
            # --- DE FIX IS HIER ---
            for nl in data["vocab"].keys():
                st.write(nl)
        with col2:
            st.write("**Engels**")
            # --- EN HIER ---
            for en in data["vocab"].values():
                st.write(en)
    if "uitleg_bezittelijk" in data:
        st.subheader("3. Theorie: Bezittelijke Voornaamwoorden"); st.info(data["uitleg_bezittelijk"])
    if "tabel_bezittelijk" in data:
        st.markdown(data["tabel_bezittelijk"])
    if "oefening_invul" in data:
        st.subheader("4. Praktische Oefening")
        st.write("Vul de juiste vorm in:")
        for i, zin in enumerate(data["oefening_invul"]):
            st.write(f"{i+1}. {zin}")
        with st.expander("Klik hier voor de antwoorden"):
            st.write(data["antwoorden_invul"])

def generate_grammar_exercise(hero, niveau, onderwerp):
    # (Deze functie is ongewijzigd)
    data = leerstof_database[niveau]["grammatica"][onderwerp]
    st.header(f"Les (Niveau {niveau}): {onderwerp}", divider='rainbow')
    st.subheader("1. Theorie"); st.info(data["uitleg"])
    st.subheader("2. Praktische Oefening")
    st.write("Maak de zinnen af:")
    for i, zin in enumerate(data["oefening"]):
        zin = zin.replace("{naam}", hero.name)
        st.write(f"{i+1}. {zin}")
    with st.expander("Klik hier voor de antwoorden"):
        st.write(data["antwoorden"])

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
            generate_thema_exercise(hero, gekozen_niveau, gekozen_les)
        elif gekozen_type == "grammatica":
            generate_grammar_exercise(hero, gekozen_niveau, gekozen_les)
    else:
        st.warning("Maak alsjeblieft een volledige keuze in de sidebar.")
else:
    st.info("Vul links je gegevens in, kies een les en klik op 'Genereer Oefening!'")

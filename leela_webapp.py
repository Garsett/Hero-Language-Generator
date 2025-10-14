import streamlit as st
import random

# ===================================================================
# DEFINITIES
# ===================================================================
class HeroProfile:
    def __init__(self, name, age, country, occupation, gender):
        self.name = name
        self.age = age
        self.country = country
        self.occupation = occupation
        self.gender = gender

# ===================================================================
# DE KENNISBANK (DATABASE) - MET UITGEBREIDE LES 'FAMILIE'
# ===================================================================
leerstof_database = {
    "A1": {
        "themas": {
            "👋 Kennismaken": {
                "uitleg": "Om jezelf voor te stellen in het Nederlands, gebruik je eenvoudige zinnen. Je begint vaak met 'Ik ben...' of 'Mijn naam is...'. Daarna vertel je je leeftijd, waar je vandaan komt en wat je doet.",
                "vocab": {"de naam": "name", "de leeftijd": "age", "de nationaliteit": "nationality", "het beroep": "profession", "de taal": "language", "komen uit": "to come from"},
                "oefenzinnen": ["Mijn naam is {naam}.", "Ik ben {leeftijd} jaar oud.", "Ik kom uit {land}.", "Ik werk als {beroep}."]
            },
            "🏡 Familie & vrienden": {
                "uitleg": "Praten over je familie en vrienden is een goede manier om te oefenen. Je leert de namen voor familieleden en gebruikt bezittelijke voornaamwoorden zoals 'mijn', 'zijn' en 'haar'.",
                "vocab": {
                    "de familie": "family", "de ouders": "parents", "de vader": "father", "de moeder": "mother",
                    "de broer": "brother", "de zus": "sister", "de zoon": "son", "de dochter": "daughter",
                    "een vriend": "a (male) friend", "een vriendin": "a (female) friend"
                },
                "oefenzinnen": [
                    "Dit is mijn broer.",
                    "De moeder van {naam} is lief.",
                    "Haar zus woont in {land}.",
                    "Ik heb één zoon en twee dochters.",
                    "Zijn vader is mijn leraar."
                ]
            },
        },
        "grammatica": {
            "📘 Persoonsvorm & onderwerp": {
                "uitleg": "In een Nederlandse zin staat het onderwerp (wie/wat?) vaak vooraan, gevolgd door de persoonsvorm (het werkwoord). Voorbeeld: 'Ik werk'.",
                "oefening": ["ik ... (werken)", "jij ... (wonen)", "{naam} ... (spreken)", "wij ... (leren)"],
                "antwoorden": ["werk", "woont", "spreekt", "leren"]
            },
            "📘 Zinsvolgorde (S-V-O)": {
                "uitleg": "De standaard zinsvolgorde is Onderwerp - Werkwoord - Object. Voorbeeld: Ik (S) drink (V) koffie (O).",
                "oefening": ["(ik / koffie / drinken)", "(jij / een boek / lezen)", "({naam} / Nederlands / leren)"],
                "antwoorden": ["Ik drink koffie.", "Jij leest een boek.", "{naam} leert Nederlands."]
            },
        }
    }
}

# ===================================================================
# DE OEFENING-GENERATORS
# ===================================================================
def generate_vocabulary_exercise(hero, thema):
    data = leerstof_database["A1"]["themas"][thema]
    
    st.header(f"Les: {thema}", divider='rainbow')
    
    # Stap 1: Toon de theorie
    st.subheader("1. Theorie")
    st.info(data["uitleg"])

    # Stap 2: Toon de woordenschat
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
    
    # Stap 3: Toon de praktische oefening
    st.subheader("3. Praktische Oefening")
    st.write("Lees de volgende zinnen hardop:")
    for zin in data["oefenzinnen"]:
        zin = zin.replace("{naam}", hero.name).replace("{leeftijd}", str(hero.age)).replace("{land}", hero.country).replace("{beroep}", hero.occupation)
        st.write(f"- {zin}")

def generate_grammar_exercise(hero, onderwerp):
    data = leerstof_database["A1"]["grammatica"][onderwerp]
    
    st.header(f"Les: {onderwerp}", divider='rainbow')
    
    # Stap 1: Toon de theorie
    st.subheader("1. Theorie")
    st.info(data["uitleg"])
    
    # Stap 2: Toon de oefening
    st.subheader("2. Praktische Oefening")
    st.write("Maak de zinnen af of zet de woorden in de juiste volgorde:")
    for i, zin in enumerate(data["oefening"]):
        zin = zin.replace("{naam}", hero.name)
        st.write(f"{i+1}. {zin}")
    
    # Stap 3: Toon de antwoorden (verborgen)
    with st.expander("Klik hier voor de antwoorden"):
        antwoorden = [ant.replace("{naam}", hero.name) for ant in data["antwoorden"]]
        st.write(antwoorden)

# ===================================================================
# DE STREAMLIT INTERFACE
# ===================================================================
st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")
st.write("Creëer een persoonlijke taalles en een mini-avontuur voor elke student.")

with st.sidebar:
    st.header("1. Gegevens van de Student")
    gender = st.selectbox("Aanspreekvorm", ["vrouwelijk (ze/haar)", "mannelijk (hij/zijn)", "neutraal (die/hun)"])
    name = st.text_input("Naam", "Lilla")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=25)
    country = st.text_input("Land", "Hongarije")
    occupation = st.text_input("Beroep", "leraar levenskunst")
    st.markdown("---")
    st.header("2. Kies je Oefening (A1)")
    thema_keuzes = ["-- Maak een keuze --"] + list(leerstof_database["A1"]["themas"].keys())
    grammatica_keuzes = ["-- Maak een keuze --"] + list(leerstof_database["A1"]["grammatica"].keys())
    gekozen_thema = st.selectbox("Kies een Thema", thema_keuzes)
    gekozen_grammatica = st.selectbox("Kies een Grammatica-onderwerp", grammatica_keuzes)

if st.sidebar.button("🚀 Genereer Oefening! 🚀"):
    hero = HeroProfile(name=name, age=age, country=country, occupation=occupation, gender=gender)

    if gekozen_thema != "-- Maak een keuze --":
        generate_vocabulary_exercise(hero, gekozen_thema)
    elif gekozen_grammatica != "-- Maak een keuze --":
        generate_grammar_exercise(hero, gekozen_grammatica)
    else:
        st.warning("Kies alsjeblieft een thema of een grammatica-onderwerp in de sidebar.")
else:
    st.info("Vul links je gegevens in, kies een oefening en klik op 'Genereer Oefening!'")

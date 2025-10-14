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
# DE KENNISBANK (DATABASE) - KLAAR VOOR MEERDERE NIVEAUS
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
                "oefenzinnen": ["Dit is mijn broer.", "De moeder van {naam} is lief.", "Haar zus woont in {land}."]
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
    # --- HIER KAN LATER A2, B1, ETC. KOMEN ---
}

# ===================================================================
# DE OEFENING-GENERATORS - NU FLEXIBEL VOOR ELK NIVEAU
# ===================================================================
def generate_vocabulary_exercise(hero, niveau, thema):
    data = leerstof_database[niveau]["themas"][thema]
    st.header(f"Les (Niveau {niveau}): {thema}", divider='rainbow')
    
    st.subheader("1. Theorie"); st.info(data["uitleg"])
    st.subheader("2. Woordenschat")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Nederlands**"); [st.write(nl) for nl in data["vocab"].keys()]
    with col2:
        st.write("**Engels**"); [st.write(en) for en in data["vocab"].values()]
    st.subheader("3. Praktische Oefening")
    st.write("Lees de volgende zinnen hardop:")
    for zin in data["oefenzinnen"]:
        zin = zin.replace("{naam}", hero.name).replace("{leeftijd}", str(hero.age)).replace("{land}", hero.country).replace("{beroep}", hero.occupation)
        st.write(f"- {zin}")

def generate_grammar_exercise(hero, niveau, onderwerp):
    data = leerstof_database[niveau]["grammatica"][onderwerp]
    st.header(f"Les (Niveau {niveau}): {onderwerp}", divider='rainbow')

    st.subheader("1. Theorie"); st.info(data["uitleg"])
    st.subheader("2. Praktische Oefening")
    st.write("Maak de zinnen af of zet de woorden in de juiste volgorde:")
    for i, zin in enumerate(data["oefening"]):
        zin = zin.replace("{naam}", hero.name)
        st.write(f"{i+1}. {zin}")
    with st.expander("Klik hier voor de antwoorden"):
        antwoorden = [ant.replace("{naam}", hero.name) for ant in data["antwoorden"]]
        st.write(antwoorden)

# ===================================================================
# DE STREAMLIT INTERFACE - MET LOGISCHE HIËRARCHIE
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
    
    # --- STAP 1: KIES NIVEAU ---
    gekozen_niveau = st.selectbox("Niveau", list(leerstof_database.keys()))
    
    # --- STAP 2: KIES TYPE (Thema of Grammatica) ---
    if gekozen_niveau:
        type_keuzes = ["-- Kies een type --"] + list(leerstof_database[gekozen_niveau].keys())
        gekozen_type = st.selectbox("Oefeningstype", type_keuzes)
        
        # --- STAP 3: KIES SPECIFIEKE LES ---
        if gekozen_type and gekozen_type != "-- Kies een type --":
            les_keuzes = ["-- Kies een les --"] + list(leerstof_database[gekozen_niveau][gekozen_type].keys())
            gekozen_les = st.selectbox("Les", les_keuzes)

if st.sidebar.button("🚀 Genereer Oefening! 🚀"):
    hero = HeroProfile(name=name, age=age, country=country, occupation=occupation, gender=gender)

    # Controleer of alle keuzes zijn gemaakt
    if 'gekozen_les' in locals() and gekozen_les != "-- Kies een les --":
        if gekozen_type == "themas":
            generate_vocabulary_exercise(hero, gekozen_niveau, gekozen_les)
        elif gekozen_type == "grammatica":
            generate_grammar_exercise(hero, gekozen_niveau, gekozen_les)
    else:
        st.warning("Maak alsjeblieft een volledige keuze in de sidebar (Niveau > Type > Les).")
else:
    st.info("Vul links je gegevens in, kies een volledige les en klik op 'Genereer Oefening!'")

import streamlit as st
import random

# ===================================================================
# STAP 1: DE KENNISBANK - DE HERSENEN VAN DE APP
# Hier bouwen we al jouw lesstof in. Dit kunnen we oneindig uitbreiden.
# ===================================================================
leerstof_database = {
    "A1": {
        "themas": {
            "👋 Kennismaken": {
                "vocab": {"de naam": "name", "de leeftijd": "age", "de nationaliteit": "nationality", "het beroep": "profession", "de taal": "language"},
                "zinnen": ["Mijn naam is {naam}.", "Ik ben {leeftijd} jaar oud.", "Ik kom uit {land}.", "Ik werk als {beroep}."]
            },
            "🏡 Familie & vrienden": {
                "vocab": {"de familie": "family", "de vader": "father", "de moeder": "mother", "de broer": "brother", "de zus": "sister", "een vriend": "a friend"},
                "zinnen": ["{naam} heeft een broer.", "De moeder van {naam} is lief.", "Ik stel mijn familie voor."]
            },
            # --- HIER KUNNEN WE ALLE ANDERE THEMA'S TOEVOEGEN ---
        },
        "grammatica": {
            "📘 Persoonsvorm & onderwerp": {
                "uitleg": "In een Nederlandse zin staat het onderwerp (wie/wat?) vaak vooraan, gevolgd door de persoonsvorm (het werkwoord).",
                "oefening": ["ik ... (werken)", "jij ... (wonen)", "{naam} ... (spreken)", "wij ... (leren)"],
                "antwoorden": ["werk", "woont", "spreekt", "leren"]
            },
            "📘 Zinsvolgorde (S-V-O)": {
                "uitleg": "De standaard zinsvolgorde is Onderwerp - Werkwoord - Object. Bv: Ik (S) drink (V) koffie (O).",
                "oefening": ["(ik / koffie / drinken)", "(jij / een boek / lezen)", "({naam} / Nederlands / leren)"],
                "antwoorden": ["Ik drink koffie.", "Jij leest een boek.", "{naam} leert Nederlands."]
            },
            # --- HIER KUNNEN WE ALLE ANDERE GRAMMATICA TOEVOEGEN ---
        }
    }
    # --- HIER KUNNEN WE LATER B1, B2, C1 TOEVOEGEN ---
}


# ===================================================================
# STAP 2: DE SLIMME OEFENING-GENERATORS
# Aparte functies voor elk type oefening.
# ===================================================================

def generate_vocabulary_exercise(hero, thema):
    """Genereert een woordenschatoefening op basis van een gekozen thema."""
    data = leerstof_database["A1"]["themas"][thema]
    vocab = data["vocab"]
    
    st.subheader(f"📚 Woordenschat: {thema}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Nederlands**")
        for nl in vocab.keys():
            st.write(nl)
    with col2:
        st.write("**Engels**")
        for en in vocab.values():
            st.write(en)
    
    st.markdown("---")
    st.write("**Oefenzinnen:**")
    for zin in data["zinnen"]:
        # Personaliseer de zinnen met de gegevens van de student
        zin = zin.replace("{naam}", hero.name).replace("{leeftijd}", str(hero.age)).replace("{land}", hero.country).replace("{beroep}", hero.occupation)
        st.write(f"- {zin}")

def generate_grammar_exercise(hero, onderwerp):
    """Genereert een grammatica-oefening op basis van een gekozen onderwerp."""
    data = leerstof_database["A1"]["grammatica"][onderwerp]
    
    st.subheader(f"🧠 Grammatica: {onderwerp.split(' ')[1]}")
    st.info(f"**Uitleg:** {data['uitleg']}")
    
    st.write("**Maak de zinnen af:**")
    for i, zin in enumerate(data["oefening"]):
        zin = zin.replace("{naam}", hero.name)
        st.write(f"{i+1}. {zin}")
    
    with st.expander("Klik hier voor de antwoorden"):
        antwoorden = [ant.replace("{naam}", hero.name) for ant in data["antwoorden"]]
        st.write(antwoorden)


# ===================================================================
# STAP 3: DE STREAMLIT INTERFACE
# De interface wordt uitgebreid met de nieuwe keuzemenu's.
# ===================================================================

st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")
st.write("Creëer een persoonlijke taalles en een mini-avontuur voor elke student.")

# --- SIDEBAR MET ALLE KEUZES ---
with st.sidebar:
    st.header("1. Gegevens van de Student")
    gender = st.selectbox("Aanspreekvorm", ["vrouwelijk (ze/haar)", "mannelijk (hij/zijn)", "neutraal (die/hun)"])
    name = st.text_input("Naam", "Lilla")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=25)
    country = st.text_input("Land", "Hongarije")
    occupation = st.text_input("Beroep", "studente")

    st.markdown("---")
    
    st.header("2. Kies je Oefening (A1)")
    # Maak een lijst van de beschikbare thema's en grammatica-onderwerpen
    thema_keuzes = ["-- Maak een keuze --"] + list(leerstof_database["A1"]["themas"].keys())
    grammatica_keuzes = ["-- Maak een keuze --"] + list(leerstof_database["A1"]["grammatica"].keys())

    gekozen_thema = st.selectbox("Kies een Thema", thema_keuzes)
    gekozen_grammatica = st.selectbox("Kies een Grammatica-onderwerp", grammatica_keuzes)


# --- HOOFDPAGINA DIE DE GEKOZEN OEFENING TOONT ---
if st.sidebar.button("🚀 Genereer Oefening! 🚀"):
    hero = HeroProfile(name, age, country, city="stad", occupation=occupation, languages=[], character="", daily_routine="", learning_goals=[], level="A1", tone="realistisch", gender=gender)

    # Check welke oefening is gekozen en roep de juiste generator aan
    if gekozen_thema != "-- Maak een keuze --":
        generate_vocabulary_exercise(hero, gekozen_thema)
    
    elif gekozen_grammatica != "-- Maak een keuze --":
        generate_grammar_exercise(hero, gekozen_grammatica)
        
    else:
        st.warning("Kies alsjeblieft een thema of een grammatica-onderwerp in de sidebar.")

else:
    st.info("Vul links de gegevens in, kies een oefening en klik op 'Genereer Oefening!'")

# Dummy HeroProfile class (vereenvoudigd, omdat we niet alle functies meer gebruiken)
class HeroProfile:
    def __init__(self, name, age, country, city, occupation, languages, character, daily_routine, learning_goals, level, tone, gender):
        self.name = name; self.age = age; self.country = country; self.city = city; self.occupation = occupation;
        self.languages = languages; self.character = character; self.daily_routine = daily_routine;
        self.learning_goals = learning_goals; self.level = level; self.tone = tone; self.gender = gender;

import streamlit as st
import random

# ===================================================================
# KERNLOGICA - NU MET GESLACHTSBEWUSTZIJN
# ===================================================================

class HeroProfile:
    def __init__(self, name, age, country, city, occupation, languages, character, daily_routine, learning_goals, level, tone, gender):
        self.name = name; self.age = age; self.country = country; self.city = city; self.occupation = occupation;
        self.languages = languages; self.character = character; self.daily_routine = daily_routine;
        self.learning_goals = learning_goals; self.level = level; self.tone = tone;
        self.gender = gender # Nieuwe eigenschap toegevoegd!

# --- VERBETERDE GENERATOR FUNCTIES ---

def generate_intro_story(hero):
    # --- PRONOUNS (VOORNAAMWOORDEN) INSTELLEN OP BASIS VAN GENDER ---
    if "vrouwelijk" in hero.gender:
        p_sub = "ze"  # zij
        p_pos = "haar" # haar
    elif "mannelijk" in hero.gender:
        p_sub = "hij"   # hij
        p_pos = "zijn"  # zijn
    else: # neutraal
        p_sub = "die"   # die
        p_pos = "hun"   # hun

    # --- SFEER (TONE) IMPLEMENTATIE ---
    if hero.tone == "grappig":
        opening = f"Zet je schrap voor het knotsgekke verhaal van {hero.name}!"
    elif hero.tone == "poëtisch":
        opening = f"In de straten van {hero.city} danst een nieuw verhaal, dat van {hero.name}."
    else: # Realistisch / Standaard
        opening = f"Dit is het verhaal van {hero.name}."

    # --- NIVEAU (LEVEL) IMPLEMENTATIE ---
    if hero.level == "A2":
        context = f"{p_sub.capitalize()} woont nu in {hero.city}, een stad die {p_sub} elke dag een beetje beter leert kennen, terwijl {p_sub} {p_pos} talen oefent."
        goal_desc = f"{p_pos.capitalize()} ambitie is helder: {p_sub} wil {p_pos} doelen bereiken, zoals {', '.join(hero.learning_goals)}, en voelt zich daar steeds zelfverzekerder over."
    else: # A1 / Standaard
        context = f"Nu woont {p_sub} in {hero.city} en werkt {p_sub} als {hero.occupation}."
        goal_desc = f"{p_sub.capitalize()} is hier om Nederlands te leren en {p_pos} belangrijkste doelen zijn: {', '.join(hero.learning_goals)}."

    # Bouw het verhaal op met de juiste voornaamwoorden
    story = (f"{opening} {hero.name} is {hero.age} jaar oud en komt uit het mooie {hero.country}. "
             f"{context} {p_pos.capitalize()} karakter is {hero.character}. "
             f"{goal_desc} Laten we {hero.name} helpen op {p_pos} avontuur!\n")
    return story

# De andere functies blijven voor nu hetzelfde (de dialoog is al neutraal)
def generate_daily_dialogue(hero):
    goal = random.choice(hero.learning_goals)
    dialogue_starters = [
        f"**Leraar:** 'Dag {hero.name}, hoe gaat het met je leerdoel om te oefenen met \"{goal}\"?'\n\n**{hero.name}:** 'Hallo! Het gaat steeds beter.'",
        f"**Vriend:** 'Hey {hero.name}, heb je al kunnen oefenen met '{goal}'?'\n\n**{hero.name}:** 'Zeker! Ik heb gisteren een gesprek gehad.'",
    ]
    return random.choice(dialogue_starters)

def generate_vocabulary_block(hero):
    vocab = {"opstaan": "to get up", "ontbijten": "to have breakfast", "de les": "the class", "studeren": "to study"}
    output = "Nederlands | Engels\n---|---\n"
    for nl, en in vocab.items():
        output += f"{nl} | {en}\n"
    return output

def generate_fill_in_exercise(hero):
    return (f"1. Ik heet _______________ (Jouw naam is {hero.name}).\n"
            f"2. Ik kom uit _______________.\n")

def generate_mini_mission(hero):
    goal = random.choice(hero.learning_goals)
    return (f"**🎯 DOEL:** Vandaag ga je oefenen met '{goal}'.")


# ===================================================================
# DE STREAMLIT INTERFACE - NU COMPLEET MET ALLE KEUZES
# ===================================================================

st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")
st.write("Creëer een persoonlijke taalles en een mini-avontuur voor elke student.")

with st.sidebar:
    st.header("Gegevens van de Student")
    
    # --- NIEUW: GESLACHTSKEUZE BOVENAAN ---
    gender = st.selectbox("Aanspreekvorm", ["vrouwelijk (ze/haar)", "mannelijk (hij/zijn)", "neutraal (die/hun)"])
    
    name = st.text_input("Naam", "Lilla")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=25)
    country = st.text_input("Land", "Hongarije")
    city = st.text_input("Stad", "Brussel")
    occupation = st.text_input("Beroep", "studente Nederlands")
    languages_str = st.text_input("Talen (gescheiden door komma's)", "Hongaars, Engels")
    character = st.text_input("Karakter", "nieuwsgierig, vriendelijk, dromerig")
    daily_routine = st.text_area("Dagelijkse Routine", "Ze staat op om 7 uur, ontbijt, en gaat naar de les.")
    learning_goals_str = st.text_area("Leerdoelen (één per lijn)", "sollicitatiegesprek oefenen\nmet de leraar praten\nvrienden maken")
    
    level = st.selectbox("Taalniveau", ["A1", "A2"])
    tone = st.selectbox("Sfeer van het verhaal", ["realistisch", "grappig", "poëtisch"])
    
if st.button("🚀 Genereer Persoonlijke Les! 🚀"):
    if not name or not learning_goals_str:
        st.error("Vul alsjeblieft minimaal een naam en een leerdoel in.")
    else:
        languages = [lang.strip() for lang in languages_str.split(',')]
        learning_goals = [goal.strip() for goal in learning_goals_str.splitlines()]

        # Maak het profiel aan met ALLE keuzes
        hero = HeroProfile(name, age, country, city, occupation, languages, character, daily_routine, learning_goals, level, tone, gender)

        # Toon de output
        st.header("✨ Jouw Persoonlijke Taalles ✨", divider='rainbow')
        st.subheader("🌸 Introductieverhaal")
        st.write(generate_intro_story(hero))
        st.subheader("💬 Dagelijkse Dialoog")
        st.markdown(generate_daily_dialogue(hero))
        st.subheader("📚 Woordenschatblok")
        st.markdown(generate_vocabulary_block(hero))
        st.subheader("✍️ Invuloefening")
        st.text(generate_fill_in_exercise(hero))
        st.subheader("🎯 Mini-Missie (Leela-stijl)")
        st.markdown(generate_mini_mission(hero))

import streamlit as st
import random

# ===================================================================
# DE KERNLOGICA - DEZE BLIJFT 100% HETZELFDE!
# ===================================================================

class HeroProfile:
    def __init__(self, name, age, country, city, occupation, languages, character, daily_routine, learning_goals, level, tone):
        self.name = name; self.age = age; self.country = country; self.city = city; self.occupation = occupation;
        self.languages = languages; self.character = character; self.daily_routine = daily_routine;
        self.learning_goals = learning_goals; self.level = level; self.tone = tone

def generate_intro_story(hero):
    return (f"Dit is het verhaal van {hero.name}. {hero.name} is {hero.age} jaar oud en komt uit het mooie {hero.country}. "
            f"Nu woont ze in {hero.city}, waar ze hard werkt als {hero.occupation}. "
            f"Haar karakter is {hero.character}, en dat zie je terug in alles wat ze doet. "
            f"Een typische dag voor haar? {hero.daily_routine} "
            f"Ze is hier om Nederlands te leren en haar belangrijkste doelen zijn: {', '.join(hero.learning_goals)}. "
            f"Laten we haar helpen op haar avontuur!\n")

def generate_daily_dialogue(hero):
    goal = random.choice(hero.learning_goals)
    return (f"**Leraar:** 'Dag {hero.name}, hoe gaat het met je leerdoel om te oefenen met \"{goal}\"?'\n\n"
            f"**{hero.name}:** 'Hallo! Het gaat goed. Ik heb gisteren al een beetje geoefend.'\n\n"
            f"**Leraar:** 'Super! Wat was moeilijk?'\n\n"
            f"**{hero.name}:** 'Ik vind de uitspraak soms nog lastig, maar ik blijf proberen!'\n")

def generate_vocabulary_block(hero):
    vocab = {"opstaan": "to get up", "ontbijten": "to have breakfast", "de les": "the class", "studeren": "to study",
             "praten": "to talk / to speak", "oefenen": "to practice", "de leraar": "the teacher", "koken": "to cook"}
    # Using a formatted string that looks like a table in markdown
    output = "Nederlands | Engels\n---|---\n"
    for nl, en in vocab.items():
        output += f"{nl} | {en}\n"
    return output

def generate_fill_in_exercise(hero):
    return (f"1. Ik heet _______________ (Jouw naam is {hero.name}).\n"
            f"2. Ik kom uit _______________.\n"
            f"3. Ik woon nu in _______________.\n"
            f"4. Ik ben een _______________ (Jouw beroep).\n")

def generate_mini_mission(hero):
    goal = random.choice(hero.learning_goals)
    return (f"**🎯 DOEL:** Vandaag ga je oefenen met '{goal}'.\n\n"
            f"**💬 OPDRACHT:** Zoek een moment om een kort gesprek te beginnen.\n\n"
            f"**✨ SUCCES:** Je missie is geslaagd als je minimaal drie zinnen in het Nederlands hebt gezegd!\n")

# ===================================================================
# DE NIEUWE INTERFACE - GEBOUWD MET STREAMLIT!
# ===================================================================

# Titel en introductie van de webpagina
st.set_page_config(page_title="Hero Language Generator", page_icon="🌸")
st.title("🌸 Hero Language Generator 🌸")
st.write("Creëer een persoonlijke taalles en een mini-avontuur voor elke student.")

# Input velden in de sidebar voor een opgeruimde look
with st.sidebar:
    st.header("Gegevens van de Student")
    name = st.text_input("Naam", "Lilla")
    age = st.number_input("Leeftijd", min_value=1, max_value=120, value=25)
    country = st.text_input("Land", "Hongarije")
    city = st.text_input("Stad", "Brussel")
    occupation = st.text_input("Beroep", "studente Nederlands")
    languages_str = st.text_input("Talen (gescheiden door komma's)", "Hongaars, Engels")
    character = st.text_input("Karakter", "nieuwsgierig, vriendelijk, dromerig")
    daily_routine = st.text_area("Dagelijkse Routine", "Ze staat op om 7 uur, ontbijt, en gaat naar de les.")
    learning_goals_str = st.text_area("Leerdoelen (één per lijn)", "sollicitatiegesprek oefenen\nmet de leraar praten\nvrienden maken")
    
# Een grote knop om de magie te starten
if st.button("🚀 Genereer Persoonlijke Les! 🚀"):
    # Valideer of er input is
    if not name or not learning_goals_str:
        st.error("Vul alsjeblieft minimaal een naam en een leerdoel in.")
    else:
        # Verwerk de input
        languages = [lang.strip() for lang in languages_str.split(',')]
        learning_goals = [goal.strip() for goal in learning_goals_str.splitlines()]

        # Maak het profiel aan
        hero = HeroProfile(name, age, country, city, occupation, languages, character, daily_routine, learning_goals, "A1", "realistisch")

        # Toon de output op de hoofdpagina
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

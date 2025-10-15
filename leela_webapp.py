import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="API Verbindingstest", page_icon="📡")
st.title("📡 API Verbindingstest")

st.info("Deze test controleert of de app succesvol kan communiceren met de OpenAI API.")

try:
    # Probeer de client aan te maken met de secret key die is opgeslagen in Streamlit
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.write("API-sleutel gevonden in Streamlit Secrets. Poging tot verbinding...")

    with st.spinner("Testbericht wordt naar OpenAI gestuurd..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Schrijf 'Hallo Wereld' in het Nederlands."}
            ]
        )

    # Als de code hier komt, is de verbinding gelukt
    st.success("✅ SUCCESS! Verbinding met OpenAI is gelukt!")
    st.write("Antwoord van de AI:")
    st.markdown(f"> {response.choices[0].message.content}")
    st.balloons()

except Exception as e:
    # Als er een fout optreedt, wordt deze hier getoond
    st.error("❌ MISLUKT! Fout bij het verbinden met de OpenAI API:")
    st.exception(e)

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Notenrechner", layout="wide")

st.title("📘 Zeugnis-Notenrechner")

# Session State initialisieren
if "faecher" not in st.session_state:
    st.session_state.faecher = [
        {"fach": "", "arbeiten": "", "muendlich": "", "verhaeltnis": "2:1"}
    ]

def neue_zeile():
    st.session_state.faecher.append(
        {"fach": "", "arbeiten": "", "muendlich": "", "verhaeltnis": "2:1"}
    )

st.subheader("Eingabe")

# Eingabezeilen
for i, fach in enumerate(st.session_state.faecher):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fach["fach"] = st.text_input(
            "Fach", value=fach["fach"], key=f"fach_{i}"
        )

    with col2:
        fach["arbeiten"] = st.text_input(
            "Arbeitsnoten (z.B. 2;3;1)",
            value=fach["arbeiten"],
            key=f"arbeiten_{i}",
        )

    with col3:
        fach["muendlich"] = st.number_input(
            "Mündliche Note",
            min_value=1.0,
            max_value=6.0,
            step=0.1,
            value=float(fach["muendlich"]) if fach["muendlich"] else 2.0,
            key=f"muendlich_{i}",
        )

    with col4:
        fach["verhaeltnis"] = st.text_input(
            "Verhältnis S:M (z.B. 2:1)",
            value=fach["verhaeltnis"],
            key=f"verhaeltnis_{i}",
        )

st.button("➕", on_click=neue_zeile)

st.divider()

def berechne_note(arbeiten, muendlich, verhaeltnis):
    try:
        schriftliche_noten = [float(n) for n in arbeiten.split(";")]
        schriftlich_avg = sum(schriftliche_noten) / len(schriftliche_noten)

        s, m = verhaeltnis.split(":")
        s = float(s)
        m = float(m)

        endnote = (schriftlich_avg * s + muendlich * m) / (s + m)
        return round(endnote, 2)
    except:
        return None

if st.button("📤 Abgeben"):
    ergebnisse = []

    for fach in st.session_state.faecher:
        if fach["fach"].strip() == "":
            continue

        note = berechne_note(
            fach["arbeiten"], fach["muendlich"], fach["verhaeltnis"]
        )

        if note is not None:
            ergebnisse.append(
                {"Fach": fach["fach"], "Note": note}
            )

    if ergebnisse:
        df = pd.DataFrame(ergebnisse)
        st.subheader("📊 Ergebnis")
        st.table(df)
    else:
        st.warning("Bitte überprüfe deine Eingaben.")

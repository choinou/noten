# Schul-Notenrechner
# Klausuren = 40 %, Mündlich = 50 %, Referate = 10 %

FAECHER = ["Mathe", "Deutsch", "Latein"]

GEWICHTE = {
    "klausuren": 0.40,
    "muendlich": 0.50,
    "referate": 0.10
}


def noten_eingeben(text):
    """
    Erwartet Noten im Format: 2, 1.5, 3
    """
    while True:
        eingabe = input(text).strip()

        if not eingabe:
            print("❌ Bitte mindestens eine Note eingeben.")
            continue

        try:
            noten = [float(n) for n in eingabe.split(",")]
            if all(1.0 <= n <= 6.0 for n in noten):
                return noten
            else:
                print("❌ Noten müssen zwischen 1.0 und 6.0 liegen.")
        except ValueError:
            print("❌ Falsches Format. Beispiel: 2,1.5,3")


def durchschnitt(noten):
    return sum(noten) / len(noten)


def fach_berechnen(fach):
    print(f"\n📘 Fach: {fach}")

    k1 = noten_eingeben("K1 Noten: ")
    k2 = noten_eingeben("K2 Noten: ")
    k3 = noten_eingeben("K3 Noten: ")

    muendlich = noten_eingeben("Mündliche Noten: ")
    referate = noten_eingeben("Referat-Noten: ")

    klausuren_avg = durchschnitt(k1 + k2 + k3)
    muendlich_avg = durchschnitt(muendlich)
    referate_avg = durchschnitt(referate)

    gesamt = (
        klausuren_avg * GEWICHTE["klausuren"]
        + muendlich_avg * GEWICHTE["muendlich"]
        + referate_avg * GEWICHTE["referate"]
    )

    return {
        "Klausuren": round(klausuren_avg, 2),
        "Mündlich": round(muendlich_avg, 2),
        "Referate": round(referate_avg, 2),
        "Gesamt": round(gesamt, 2),
    }


def main():
    print("🎓 Notenrechner\n")

    ergebnisse = {}

    for fach in FAECHER:
        ergebnisse[fach] = fach_berechnen(fach)

    print("\n📊 Ergebnisse")
    print("-" * 60)
    for fach, daten in ergebnisse.items():
        print(
            f"{fach}: "
            f"Klausuren Ø {daten['Klausuren']} | "
            f"Mündlich Ø {daten['Mündlich']} | "
            f"Referate Ø {daten['Referate']} "
            f"=> Gesamt Ø {daten['Gesamt']}"
        )


if __name__ == "__main__":
    main()

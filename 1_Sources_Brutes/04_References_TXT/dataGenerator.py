import pandas as pd
from faker import Faker
import random

# ------------------------------
# CONFIG
# ------------------------------
N = 5000

fake = Faker("fr_FR")

# --- Prénoms Maroc ---
maroc_male = [
    "Mohamed", "Ahmed", "Youssef", "Hassan", "Omar", "Ibrahim", "Karim", "Abdallah",
    "Bilal", "Mehdi", "Anas", "Yassine", "Hamza", "Rachid", "Mustapha", "Said",
    "Adil", "Hicham", "Nabil", "Khalid", "Zakaria", "Ismail", "Reda", "Salah",
    "Ayoub", "Amine", "Othmane", "Marouane", "Walid", "Sami", "Tariq", "Jamal",
    "Fouad", "Mounir", "Hakim", "Younes", "Yahya", "Moussa", "Idriss", "Badr",
    "Oussama", "Anass", "Amin", "Yacine", "Soufiane", "Imad", "Noureddine", "Driss",
    "Houssam", "Mokhtar", "Farid", "Rida", "Samir", "Aziz", "Mahdi", "Abdelali",
    "Abderrahmane", "Abdelkader", "Abdellah", "Abdessamad", "Abdelaziz", "Abdelhamid",
    "Mohammed", "Mahmoud", "Ali", "Sidi", "Mbarek", "Chakib", "Hatim", "Rayan",
    "Adam", "Ayman", "Ilyas", "Wassim", "Nasser", "Fayssal", "Haj", "Kamil",
    "Larbi", "Lotfi", "Mansour", "Naji", "Salim", "Taha", "Zouhair", "Abdou"
]

maroc_female = [
    "Fatima", "Aicha", "Khadija", "Zineb", "Sara", "Salma", "Noura", "Houda",
    "Imane", "Rania", "Asma", "Soukaina", "Meryem", "Hafsa", "Saadia", "Hayat",
    "Samira", "Latifa", "Jamila", "Nadia", "Hanane", "Kawtar", "Sanaa", "Yasmina",
    "Leila", "Naima", "Malika", "Zahra", "Bouchra", "Nabila", "Rachida", "Sofia",
    "Wafa", "Amal", "Karima", "Halima", "Mounia", "Nora", "Hanae", "Ghita",
    "Siham", "Farida", "Habiba", "Kenza", "Laila", "Mina", "Rim", "Selma",
    "Yousra", "Zahia", "Amina", "Chaimae", "Dounia", "Fadwa", "Hajar", "Ikram",
    "Ines", "Jihane", "Lina", "Manal", "Narjis", "Rokia", "Safae", "Widad",
    "Yamina", "Zara", "Aya", "Basma", "Chaymae", "Douaa", "Hiba", "Ihsane",
    "Ilham", "Khadija", "Loubna", "Marwa", "Nisrine", "Rajae", "Salsabil", "Touria",
    "Zineb", "Ahlam", "Aziza", "Boutaina", "Fatimazahra", "Hind", "Khalida", "Mariam",
    "Nezha", "Rabia", "Sabrina", "Safia", "Taoufik", "Zahra", "Zohra"
]

maroc_noms = [
    "El Fassi", "Bennani", "El Idrissi", "Lahcen", "Bourkadi", "Hattab", 
    "Alaoui", "El Amrani", "Moussaoui", "Rahmouni", "El Moutaouakil",
    "Belkhadir", "Chraibi", "Benjelloun", "El Khattabi", "Bouzekri", 
    "Lamrani", "Berrada", "Tazi", "Benkirane", "Bouhlal", "Cherkaoui",
    "Daoudi", "El Mandjra", "Fassi", "Guennoun", "Hakimi", "Jabri",
    "Kabbaj", "Lahlou", "Mernissi", "Naciri", "Ouazzani", "Qadiri",
    "Roudani", "Saadi", "Tabit", "Zerouali", "Abid", "Bouzoubaa",
    "Chaouni", "Demnati", "El Filali", "Gharbaoui", "Hassani", 
    "Iraqi", "Jorio", "Khalil", "Mouline", "Naji", "Oulad", 
    "Rifi", "Sabri", "Toumi", "Zahir", "Ait", "Bouhmadi", 
    "Chemao", "Dlimi", "El Ghalbi", "Gueddari", "Houari", 
    "Jaouhari", "Karam", "Mabrouk", "Nasser", "Ouali", 
    "Rahal", "Sahraoui", "Tourabi", "Zouhair", "Amrani",
    "Bouchentouf", "Chafik", "Doukkali", "El Hachimi", "Habti",
    "Idrissi", "Kettani", "Laraki", "Moujahid", "Nouaman",
    "Othmani", "Rais", "Sebti", "Tazi", "Ziyat", "Bahi",
    "Bouzidi", "Cheikh", "El Omari", "Hammoudi", "Jebli",
    "Kouachi", "Madani", "Nfissi", "Oufkir", "Rjai", 
    "Sefrioui", "Touil", "Zniber", "Akka", "Bouazzaoui",
    "Chraibi", "El Yazidi", "Harrak", "Joundy", "Labrini",
    "Mansouri", "Ouahbi", "Rmil", "Skalli", "Wahbi",
    "Zerhouni", "Alami", "Boudra", "Dahmani", "El Boukili",
    "Kacem", "Loukili", "Mrani", "Oulhaj", "Slaoui",
    "Touimi", "Zouak", "Bouhout", "Chrigui", "El Khamsi",
    "Khaldoune", "Maatoug", "Oujdi", "Smires", "Zaid",
    "Bouaouina", "El Fahime", "Kharroubi", "Mechbal", "Rchidi",
    "Tlemsani", "Zoubir", "Adouiri", "El Ghazaoui", "Moussa",
    "Rohi", "Touijer", "Zouita", "Amarir", "El Mrabet",
    "Moustaquin", "Saih", "Toufali", "Zouine", "Aroui",
    "El Yacoubi", "Niama", "Sakhi", "Touzani", "Zouitni",
    "Assou", "El Yousfi", "Ouassou", "Salmi", "Trimech",
    "Zoukh", "Atou", "Fennir", "Ouissaden", "Samir",
    "Wardi", "Zouria", "Azou", "Ghomri", "Oukacha",
    "Sbaai", "Yassi", "Zouro", "Bahi", "Hilal",
    "Oulad", "Sbitri", "Yousra", "Zoubir", "Baraka",
    "Jamil", "Ouled", "Sefiani", "Zahri", "Zouhir",
    "Boua", "Kamil", "Rchid", "Tahiri", "Zouine",
    "Bouj", "Larbi", "Rguibi", "Tazi", "Zoukir",
    "Bouk", "Mabrouk", "Saih", "Toumi", "Zoul",
    "Boul", "Nacer", "Slaoui", "Tourabi", "Zoumar",
    "Boun", "Ouali", "Smahi", "Touzani", "Zoumir",
    "Bour", "Radi", "Soussi", "Touzi", "Zoun",
    "Bous", "Sabi", "Tabit", "Touzy", "Zoupi",
    "Bout", "Said", "Tahri", "Touza", "Zouqi",
    "Bouz", "Salem", "Tijarti", "Touzi", "Zouri",
    "Dah", "Samir", "Tlemsani", "Touzy", "Zourk",
    "El", "Sassi", "Touahri", "Touzz", "Zous",
    "Gue", "Sbaai", "Touba", "Touz", "Zout",
    "Had", "Sbitri", "Toubi", "Touza", "Zouw",
    "Ham", "Sebti", "Toufi", "Touzi", "Zoux",
    "Har", "Sefrioui", "Tougi", "Touzy", "Zouy",
    "Has", "Slaoui", "Touhi", "Touzz", "Zouz",
    "Hass", "Smahi", "Touji", "Touz", "Zouzz"
]


# --- Afrique Ouest ---
afrique_male = ["Mamadou", "Ibrahim", "Cheikh", "Issa", "Oumar", "Souleymane", 
                "Abdoulaye", "Boubacar", "Moussa", "Amadou", "Alpha", "Modou",
                "Pape", "Serigne", "Tidiane", "Yaya", "Aliou", "Kader", "Mahamadou"]

afrique_female = ["Aminata", "Fatou", "Awa", "Mariama", "Kadija", "Bintou",
                  "Rokhaya", "Aissatou", "Maimouna", "Nafissatou", "Sokhna",
                  "Khadidiatou", "Mame", "Mbayang", "Ndeye", "Oumou", "Sira"]

afrique_noms = ["Diop", "Traoré", "Ouattara", "Gueye", "Sow", "Konaté", "Sylla",
                "Ndiaye", "Diallo", "Cissé", "Ba", "Sarr", "Fall", "Kane", "Keita",
                "Touré", "Camara", "Barry", "Savané", "Coulibaly", "Diaw"]

# --- Européens ---
europe_male = ["Lucas", "Antoine", "Nicolas", "Jean", "Miguel", "Carlos",
               "Thomas", "Pierre", "David", "Daniel", "Fernando", "Javier",
               "Paolo", "Marco", "Alexander", "Michael", "Stefan", "Patrick"]

europe_female = ["Marie", "Claire", "Anna", "Julia", "Camille", "Laura",
                 "Sophie", "Isabelle", "Elena", "Carmen", "Chiara", "Sofia",
                 "Nathalie", "Valérie", "Ingrid", "Monica", "Patricia", "Céline"]

europe_noms = ["Martin", "Bernard", "Dupont", "Garcia", "Lopez", "Rossi",
               "Dubois", "Moreau", "Simon", "Laurent", "Rodriguez", "Fernandez",
               "Müller", "Schmidt", "Silva", "Santos", "Ricci", "Conti", "Brown",
               "Jones", "Wilson", "Johansson", "Andersson"]

# --- Nationalités + proportions ---
nationalites = [
    ("Maroc", 0.85),
    ("Sénégal", 0.04),
    ("Côte d’Ivoire", 0.04),
    ("France", 0.03),
    ("Espagne", 0.02),
    ("Tunisie", 0.02)
]

# ------------------------------
# CHARGER LES FILIÈRES
# ------------------------------
filieres = pd.read_csv("Ref_Filiere_Groupe.csv", sep="\t", encoding="utf-8")

AP1 = filieres[filieres["filieres_niveau"] == "AP1"]
AP2 = filieres[filieres["filieres_niveau"] == "AP2"]
CI1 = filieres[filieres["filieres_niveau"] == "CI1"]
CI2 = filieres[filieres["filieres_niveau"] == "CI2"]
CI3 = filieres[filieres["filieres_niveau"] == "CI3"]

cycles = [AP1, AP2, CI1, CI2, CI3]

# ------------------------------
# RÉPARTITION des étudiants
# ------------------------------
base = N // 5
cycle_counts = [base + random.randint(-5, 5) for _ in range(5)]

# Ajustement total
diff = N - sum(cycle_counts)
cycle_counts[0] += diff

# ------------------------------
# FONCTIONS
# ------------------------------
def pick_nationalite():
    r = random.random()
    cum = 0
    for nat, prob in nationalites:
        cum += prob
        if r <= cum:
            return nat
    return "Maroc"

def pick_name(sexe, nationalite):
    if nationalite == "Maroc":
        return (random.choice(maroc_male if sexe == "Homme" else maroc_female),
                random.choice(maroc_noms))

    elif nationalite in ["Sénégal", "Côte d’Ivoire"]:
        return (random.choice(afrique_male if sexe == "Homme" else afrique_female),
                random.choice(afrique_noms))

    else:  # Européens
        return (random.choice(europe_male if sexe == "Homme" else europe_female),
                random.choice(europe_noms))

# ------------------------------
# GENERATION
# ------------------------------
data = []
etudiant_id = 1

for cycle_df, count in zip(cycles, cycle_counts):
    fids = cycle_df["filieres_groupe_id"].tolist()

    for _ in range(count):
        sexe = random.choice(["Homme", "Femme"])
        nat = pick_nationalite()
        prenom, nom = pick_name(sexe, nat)

        data.append({
            "etudiant_id": etudiant_id,
            "etudiant_prenom": prenom,
            "etudiant_nom": nom,
            "etudiant_sexe": sexe,
            "filieres_groupe_id": random.choice(fids)
        })

        etudiant_id += 1

df = pd.DataFrame(data)
df.to_csv("Etudiants_Population.csv", index=False)

print("✔ Fichier généré : etudiants_realistes.csv")

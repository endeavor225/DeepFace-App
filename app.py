import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image

st.set_page_config(page_title="Face Verifier", layout="centered")
st.title("🔍 Vérification Faciale avec DeepFace")

# Fonction de lecture d'image
def read_image(file):
    img = Image.open(file).convert('RGB')
    return np.array(img)

# Choix du mode de saisie de l'image cible
mode = st.radio("📷 Sélectionnez la méthode pour fournir l'image cible :", ["📸 Webcam", "📤 Uploader un fichier"])

if mode == "📸 Webcam":
    target_file = st.camera_input("📸 Prendre une photo avec la webcam (image cible)")
else:
    target_file = st.file_uploader("📤 Choisir l'image cible (personne à reconnaître)", type=["jpg", "png", "jpeg"])

# Upload des autres images à comparer
other_files = st.file_uploader("📁 Importer plusieurs images à comparer", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Traitement si tout est prêt
if target_file and other_files:
    st.image(target_file, caption="Image cible", width=200)
    target_image = read_image(target_file)

    matched = False

    for file in other_files:
        st.divider()
        st.image(file, caption=f"Comparaison avec {file.name}", width=200)
        compare_image = read_image(file)

        try:
            result = DeepFace.verify(img1_path=target_image, img2_path=compare_image, model_name = "Facenet512",  enforce_detection=False)
            if result["verified"]:
                st.success(f"✅ MATCH trouvé avec : {file.name}")
                matched = True
               
            else:
                st.warning(f"❌ Pas de correspondance avec {file.name}")
        except Exception as e:
            st.error(f"Erreur : {str(e)}")

    if not matched:
        st.info("😕 Aucun match détecté dans les images fournies.")

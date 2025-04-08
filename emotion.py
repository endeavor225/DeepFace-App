import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image

st.set_page_config(page_title="Détection d'Émotions", layout="centered")
st.title("🧠 Détection d'Émotions avec DeepFace")

# Traduction des émotions en français
emotion_fr = {
    "angry": "en colère",
    "disgust": "dégoût",
    "fear": "peur",
    "happy": "heureux(se)",
    "sad": "triste",
    "surprise": "surpris(e)",
    "neutral": "neutre"
}

# Fonction de lecture d'image
def read_image(file):
    img = Image.open(file).convert('RGB')
    return np.array(img)

# Choix de la méthode d'acquisition
mode = st.radio("📸 Choisir la méthode d'acquisition :", ["📷 Webcam", "📤 Importer une image"])

# Récupérer l'image
emotion_img = None
if mode == "📷 Webcam":
    emotion_img = st.camera_input("Prendre une photo")
else:
    emotion_img = st.file_uploader("Importer une image", type=["jpg", "jpeg", "png"])

# Analyse si une image est chargée
if emotion_img:
    st.image(emotion_img, caption="Image à analyser", width=250)
    image_array = read_image(emotion_img)

    try:
        result = DeepFace.analyze(image_array, actions=['emotion'], enforce_detection=False)
        emotion_data = result[0]
        dominant_en = emotion_data['dominant_emotion']
        dominant_fr = emotion_fr.get(dominant_en, dominant_en)

        st.subheader("😄 Émotion dominante détectée :")
        st.markdown(f"**{dominant_fr.capitalize()}**")

        st.subheader("📊 Détail des émotions détectées :")
        for emo_en, val in emotion_data["emotion"].items():
            emo_fr = emotion_fr.get(emo_en, emo_en)
            val_str = "{:.2f}".format(val).replace('.', ',')
            st.write(f"- {emo_fr.capitalize()} : {val_str} %")

    except Exception as e:
        st.error(f"Erreur lors de l'analyse : {str(e)}")

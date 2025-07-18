import streamlit as st
import random
import json
import os

# =========================
# 🔤 Список встроенных слов
# =========================
english_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
]

# ================
# 🧬 Концепты
# ================
concept_roots = {
    "time": ["tem", "chron", "zel"],
    "person": ["an", "mur", "sol"],
    "motion": ["vel", "drak", "zor"],
    "sight": ["vi", "lux", "zor"],
    "emotion": ["lem", "shu", "qar"],
    "thought": ["ment", "syn", "krel"],
    "object": ["tor", "mek", "zul"],
    "body": ["kar", "nur", "vek"],
    "communication": ["tel", "qal", "rix"],
    "nature": ["sol", "nar", "vek"],
    "abstract": ["sha", "lir", "dra"]
}

basic_map = {
    "time": "time", "person": "person", "year": "time", "day": "time",
    "thing": "object", "man": "person", "life": "abstract", "hand": "body",
    "child": "person", "eye": "sight", "woman": "person", "place": "nature",
    "work": "motion", "week": "time", "case": "abstract", "point": "abstract",
    "government": "group", "company": "group", "number": "abstract", "group": "group",
    "problem": "abstract", "fact": "abstract", "be": "abstract", "have": "abstract",
    "do": "motion", "say": "communication", "get": "motion", "make": "object",
    "go": "motion", "know": "thought", "see": "sight", "come": "motion",
    "think": "thought", "look": "sight", "want": "emotion", "give": "motion",
    "use": "motion", "find": "motion", "tell": "communication", "ask": "communication",
    "seem": "thought", "feel": "emotion", "try": "motion", "leave": "motion",
    "call": "communication"
}

# ========================
# 📖 Загрузка/создание словаря
# ========================
DICT_PATH = "alien_dict_logical.json"

if os.path.exists(DICT_PATH):
    with open(DICT_PATH, "r") as f:
        alien_dict = json.load(f)
else:
    alien_dict = {}

used_words = set(alien_dict.values())

# 🔧 Генерация инопланетных слов
def make_conceptual_word(category):
    root = random.choice(concept_roots.get(category, ["zan"]))
    suffixes = ["ek", "ur", "an", "os", "im", "ul", "ith", "ok", "ar", "em"]
    while True:
        word = root + random.choice(suffixes)
        if word not in used_words:
            used_words.add(word)
            return word

# ========================
# 🌐 Интерфейс Streamlit
# ========================
st.title("🛸 Инопланетный Переводчик")
st.markdown("Автоматически переводит английские слова в логичный выдуманный язык на основе корней.")

input_text = st.text_input("Введи английский текст:")

if input_text:
    translated = []
    for word in input_text.strip().split():
        w = word.lower().strip(",.!?")
        if w not in alien_dict and w in english_words:
            category = basic_map.get(w, random.choice(list(concept_roots.keys())))
            alien_dict[w] = make_conceptual_word(category)
            with open(DICT_PATH, "w") as f:
                json.dump(alien_dict, f, indent=2)
        translated.append(alien_dict.get(w, "[?]"))

    st.markdown("### Перевод:")
    st.markdown(" ".join(translated))

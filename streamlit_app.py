import json
import random

# Загрузим список из 10,000 слов (замени путь если у тебя есть готовый)
with open("top_10000_english_words.txt", "r") as f:
    english_words = [line.strip().lower() for line in f if line.strip()]

# Концепты и слоги
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
    "thing": "object", "man": "person", "world": "nature", "life": "abstract",
    "hand": "body", "part": "object", "child": "person", "eye": "sight",
    "woman": "person", "place": "nature", "work": "motion", "week": "time",
    "case": "abstract", "point": "abstract", "government": "group",
    "company": "group", "number": "abstract", "group": "group",
    "problem": "abstract", "fact": "abstract", "be": "abstract",
    "have": "abstract", "do": "motion", "say": "communication",
    "get": "motion", "make": "object", "go": "motion", "know": "thought",
    "see": "sight", "come": "motion", "think": "thought", "look": "sight",
    "want": "emotion", "give": "motion", "use": "motion", "find": "motion",
    "tell": "communication", "ask": "communication", "seem": "thought",
    "feel": "emotion", "try": "motion", "leave": "motion", "call": "communication"
}

def make_conceptual_word(category, used_words):
    root = random.choice(concept_roots.get(category, ["zan"]))
    suffixes = ["ek", "ur", "an", "os", "im", "ul", "ith", "ok", "ar", "em"]
    while True:
        word = root + random.choice(suffixes)
        if word not in used_words:
            used_words.add(word)
            return word

# Генерация
alien_dict = {}
used = set()

for word in english_words:
    category = basic_map.get(word, random.choice(list(concept_roots.keys())))
    alien_word = make_conceptual_word(category, used)
    alien_dict[word] = alien_word

# Сохраняем
with open("alien_dict_logical_10k.json", "w") as f:
    json.dump(alien_dict, f, indent=2)

print("✅ Словарь alien_dict_logical_10k.json готов!")

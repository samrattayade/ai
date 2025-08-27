import requests

def translate_to_hindi(word):
    url = "https://api.mymemory.translated.net/get"
    params = {"q": word, "langpair": "en|hi"}

    response = requests.get(url, params=params)
    data = response.json()

    if 'responseData' in data:
        return data['responseData']['translatedText']
    else:
        return "Translation not found."

# Run app
while True:
    word = input("\nEnter an English word (or 'q' to quit): ").strip()
    if word.lower() == 'q':
        break
    hindi_word = translate_to_hindi(word)
    print(f"🔤 {word} → 🇮🇳 {hindi_word}")

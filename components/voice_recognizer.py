import speech_recognition as sr
from sentence_transformers import SentenceTransformer, util

def recognize_and_get_best_match(word_list):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # print("speak!!!!!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        # print(f"you said {recognized_text}")
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None

    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    highest_similarity = 0
    best_match = None

    for word in word_list:
        similarity = calculate_sentence_similarity(recognized_text, word, model)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = word

    if best_match:
        return best_match
    else:
        return None

def calculate_sentence_similarity(sentence1, sentence2, model):
    embeddings1 = model.encode([sentence1], convert_to_tensor=True)
    embeddings2 = model.encode([sentence2], convert_to_tensor=True)

    similarity_score = util.cos_sim(embeddings1, embeddings2)

    return similarity_score.item()
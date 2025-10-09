# # # def get_bot_response(user_msg: str) -> str:
# # #     msg = user_msg.lower()

# # #     if "hello" in msg or "hi" in msg:
# # #         return "Hello 👋! How can I assist you with BDA services today?"
# # #     elif "application" in msg or "form" in msg:
# # #         return "You can download BDA forms from the official website or apply online."
# # #     elif "contact" in msg:
# # #         return "You can contact BDA at +91-755-xxxxxxx or visit the office at ISBT, Bhopal."
# # #     elif "what is bda" in msg or "bda" in msg:
# # #         return "BDA stands for Bhopal Development Authority, responsible for urban planning and development in Bhopal."
# # #     elif "bye" in msg:
# # #         return "Goodbye! Have a great day 😊"
# # #     else:
# # #         return "I'm still learning about BDA. Please try asking something else."


# # import csv
# # from pathlib import Path

# # # Load CSV responses once
# # RESPONSES_FILE = Path(__file__).parent / "BDA_ChatBot.csv"

# # print(f"Loading responses from: {RESPONSES_FILE.resolve()}")

# # def load_responses():
# #     responses = {}
# #     with open(RESPONSES_FILE, newline='', encoding='utf-8') as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         print(f"CSV columns: {reader.fieldnames}")
# #         for row in reader:
# #             # Convert keyword to lowercase for matching
# #             responses[row["question"].lower()] = row["answer"]
# #     return responses

# # RESPONSES = load_responses()

# # def get_bot_response(user_msg: str) -> str:
# #     msg = user_msg.lower()
# #     for question, answer in RESPONSES.items():
# #         if question in msg:
# #             return answer
# #     return "I'm still learning about BDA. Please try asking something else."


# # -----with ml concept ----

# import csv
# from pathlib import Path
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load CSV responses once
# RESPONSES_FILE = Path(__file__).parent / "BDA_ChatBot.csv"
# print(f"Loading responses from: {RESPONSES_FILE.resolve()}")

# def load_responses():
#     data = []
#     with open(RESPONSES_FILE, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         print(f"CSV columns: {reader.fieldnames}")
#         for row in reader:
#             data.append({"question": row["question"].lower(), "answer": row["answer"]})
#     return data

# RESPONSES = load_responses()

# # Prepare TF-IDF vectorizer for questions
# questions = [item["question"] for item in RESPONSES]
# vectorizer = TfidfVectorizer().fit(questions)
# question_vectors = vectorizer.transform(questions)

# def get_bot_response(user_msg: str) -> str:
#     msg = user_msg.lower()
#     if "hello" in msg or "hi" in msg:
#         return "Hello 👋! How can I assist you with BDA services today?"
#     elif "application" in msg or "form" in msg:
#         return "You can download BDA forms from the official website or apply online."
#     elif "contact" in msg:
#         return "You can contact BDA at +91-755-xxxxxxx or visit the office at ISBT, Bhopal."
#     elif "bye" in msg:
#         return "Goodbye! Have a great day 😊"

    
#     # Transform user message to vector
#     msg_vector = vectorizer.transform([msg])
#     print(f"User message vector shape: {msg_vector.shape}")
    
#     # Compute cosine similarity
#     similarities = cosine_similarity(msg_vector, question_vectors)
    
#     # Find the best matching question
#     best_index = similarities.argmax()
#     best_score = similarities[0][best_index]
    
#     # Threshold to decide if match is good enough
#     if best_score > 0.3:
#         return RESPONSES[best_index]["answer"]
    
#     return "I'm still learning about BDA. Please try asking something else."

# 08-10-25
# import csv
# from pathlib import Path
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load CSV responses once
# RESPONSES_FILE = Path(__file__).parent / "BDA_ChatBot.csv"
# print(f"Loading responses from: {RESPONSES_FILE.resolve()}")

# def load_responses():
#     data = []
#     with open(RESPONSES_FILE, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         print(f"CSV columns: {reader.fieldnames}")
#         for row in reader:
#             data.append({
#                 "question": row["question"].lower(),
#                 "answer": row["answer"],
#                 "url": row["URL"] if row["URL"] else None
#             })
#     return data

# RESPONSES = load_responses()

# # Prepare TF-IDF vectorizer for questions
# questions = [item["question"] for item in RESPONSES]
# vectorizer = TfidfVectorizer().fit(questions)
# question_vectors = vectorizer.transform(questions)

# def get_bot_response(user_msg: str) -> str:
#     msg = user_msg.lower()
#     if "hello" in msg or "hi" in msg:
#         return "Hello 👋! How can I assist you with BDA services today?"
#     elif "application" in msg or "form" in msg:
#         return "You can download BDA forms from the official website or apply online."
#     elif "contact" in msg:
#         return "You can contact BDA at +91-755-xxxxxxx or visit the office at ISBT, Bhopal."
#     elif "bye" in msg:
#         return "Goodbye! Have a great day 😊"

#     # Transform user message to vector
#     msg_vector = vectorizer.transform([msg])
#     print(f"User message vector shape: {msg_vector.shape}")
    
#     # Compute cosine similarity
#     similarities = cosine_similarity(msg_vector, question_vectors)
    
#     # Find the best matching question
#     best_index = similarities.argmax()
#     best_score = similarities[0][best_index]
    
#     # Threshold to decide if match is good enough
#     if best_score > 0.3:
#         response = RESPONSES[best_index]["answer"]
#         url = RESPONSES[best_index]["url"]
#         if url:
#             response += f' <a href="{url}" target="_blank">Click here for more details</a>'
#         return response
    
#     return "I'm still learning about BDA. Please try asking something else."

import csv
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV responses once
RESPONSES_FILE = Path(__file__).parent / "BDA_ChatBot.csv"
print(f"Loading responses from: {RESPONSES_FILE.resolve()}")

def load_responses():
    data = []
    with open(RESPONSES_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"CSV columns: {reader.fieldnames}")
        for row in reader:
            data.append({
                "question": row["question"].lower(),
                "answer": row["answer"],
                "url": row.get("URL", "").strip() or None
            })
    return data

RESPONSES = load_responses()

# Prepare TF-IDF vectorizer for questions
questions = [item["question"] for item in RESPONSES]
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

def make_links_clickable(text: str) -> str:
    """
    Detect any URL (http/https) in the text and convert it to clickable HTML.
    """
    url_pattern = r'(https?://[^\s]+)'
    return re.sub(url_pattern, r'<a href="\1" target="_blank">\1</a>', text)

def get_bot_response(user_msg: str) -> str:
    msg = user_msg.lower()
    
    # Simple keyword-based responses
    if "hello" in msg or "hi" in msg:
        return "Hello 👋! How can I assist you with BDA services today?"
    elif "application" in msg or "form" in msg:
        return "You can download BDA forms from the official website or apply online."
    elif "bye" in msg:
        return "Goodbye! Have a great day 😊"

    # TF-IDF similarity-based matching
    msg_vector = vectorizer.transform([msg])
    similarities = cosine_similarity(msg_vector, question_vectors)

    best_index = similarities.argmax()
    best_score = similarities[0][best_index]

    # Threshold for best match
    if best_score > 0.3:
        response = RESPONSES[best_index]["answer"]
        url = RESPONSES[best_index]["url"]

        # Convert any URLs in response text into clickable HTML
        response = make_links_clickable(response)

        # Add extra URL from CSV if available
        if url:
            response += f' <br><a href="{url}" target="_blank">Click here for more details</a>'
        
        return response

    return "I'm still learning about BDA. Please try asking something else."

from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.bot_logic import get_bot_response


router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    reply = get_bot_response(request.message)
    return {"reply": reply}


# 08-10-25

# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.utils.bot_logic import get_bot_response

# router = APIRouter()

# class ChatRequest(BaseModel):
#     message: str

# @router.post("/chat")
# async def chat(request: ChatRequest):
#     result = get_bot_response(request.message)
#     return {
#         "reply": result["answer"],
#         "url": result["url"]
#     }


#------------- 
# import os
# import csv
# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.utils.bot_logic import get_bot_response

# router = APIRouter()

# class ChatRequest(BaseModel):
#     message: str

# # Function to read CSV and store Q&A
# def load_qa_from_csv(file_path: str) -> dict:
#     print(f"Attempting to load CSV from: {os.path.abspath(file_path)}")
#     if not os.path.exists(file_path):
#         print(f"File not found at: {os.path.abspath(file_path)}. Current directory: {os.getcwd()}")
#         return {}
#     try:
#         qa_dict = {}
#         with open(file_path, mode='r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 question = row['question'].strip().lower()
#                 answer = row['answer'].strip()
#                 qa_dict[question] = answer
#         print(f"Successfully loaded {len(qa_dict)} Q&A pairs from {file_path}")
#         return qa_dict
#     except Exception as e:
#         print(f"Error loading CSV: {e}")
#         return {}

# # Load Q&A data on startup
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
# CSV_PATH = os.path.join(BASE_DIR, "BDA_ChatBot.csv")  # CSV in project root
# print(f"Resolved CSV path: {os.path.abspath(CSV_PATH)}")
# qa_data = load_qa_from_csv(CSV_PATH)
# print("Final Q&A data:", qa_data)

# # @router.post("/chat")
# # async def chat(query: ChatRequest):
# #     query_text = query.message.lower()
# #     response = qa_data.get(query_text, "Sorry, I couldn't find an answer for that.")
# #     return {"response": response}
# @router.post("/chat")
# async def chat(query: ChatRequest):
#     query_text = query.message.lower()
#     # Check CSV data first
#     response = qa_data.get(query_text, None)
#     # Fallback to bot_logic for greetings or default
#     if response is None:
#         response = get_bot_response(query_text)
#     return {"response": response}
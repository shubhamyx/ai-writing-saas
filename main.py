from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompts = {
    "blog": ChatPromptTemplate.from_template("""
Write a professional blog post about: {topic}
Tone: {tone}
Word count: approximately {length} words
Include: introduction, 3-5 main sections with headings, conclusion.
"""),
    "email": ChatPromptTemplate.from_template("""
Write a professional email about: {topic}
Tone: {tone}
Keep it concise and actionable.
"""),
    "social": ChatPromptTemplate.from_template("""
Write a {platform} post about: {topic}
Tone: {tone}
Make it engaging and include relevant hashtags.
"""),
    "product": ChatPromptTemplate.from_template("""
Write a compelling product description for: {topic}
Tone: {tone}
Highlight benefits, features, and call to action.
"""),
}

parser = StrOutputParser()

class GenerateRequest(BaseModel):
    content_type: str
    topic: str
    tone: str
    length: str = "500"
    platform: str = "LinkedIn"

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/generate")
def generate(request: GenerateRequest):
    prompt = prompts.get(request.content_type, prompts["blog"])
    chain = prompt | llm | parser
    
    result = chain.invoke({
        "topic": request.topic,
        "tone": request.tone,
        "length": request.length,
        "platform": request.platform
    })
    
    return {"content": result}
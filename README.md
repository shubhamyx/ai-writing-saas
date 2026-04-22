# AI Writing SaaS

AI-powered content generation platform for blogs, emails, social media, and product descriptions.

## What it does
- Generate blog posts with proper structure and headings
- Write professional emails instantly
- Create social media posts for LinkedIn, Twitter, Instagram
- Write compelling product descriptions
- Control tone and word count

## Tech Stack
- **LLM**: Groq API (llama-3.3-70b-versatile)
- **Backend**: FastAPI
- **Framework**: LangChain
- **Frontend**: Vanilla HTML/CSS/JS

## Setup

1. Clone the repo
2. Create virtual environment

    python -m venv venv
    venv\Scripts\activate

3. Install dependencies

    pip install fastapi uvicorn langchain langchain-groq python-dotenv jinja2

4. Create `.env` file

    GROQ_API_KEY=your_key_here

5. Run

    uvicorn main:app --reload

6. Open `http://localhost:8000`

## Built by
Shubham Yadav — building AI projects in public
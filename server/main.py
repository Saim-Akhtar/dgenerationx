from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import openai


app = FastAPI()

class SearchRequest(BaseModel):
    productDetail: str
    goals: str
    targetAudience: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/search")
def search(request: SearchRequest):
    productDetail = request.productDetail
    goals = request.goals
    targetAudience = request.targetAudience
    prompt = f'''
    Write a descriptive marketing compaign plan based which has the following things:\n
    Product Detail: {productDetail}\n
    Target Audience: {targetAudience}\n
    Goals: {goals}
    '''

    response = generate_response(prompt)
    print(response)

    # need to return either the JSON or pdf document here
    return {}

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Generate a response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

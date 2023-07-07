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
def search(detail, goals, target_audience):
    prompt = f"""
    You are an expert in marketing, product development and brand awareness. Based on your own knowledge of the domain
    generate an extensive marketing campaign plan that will include:
    1. Goal Setting: Establish clear objectives and goals for the marketing campaign, such as increasing brand awareness, \
        generating leads, driving sales, or promoting a new product.
    2. Target Audience Segmentation: Identify and segment the target audience into distinct groups based on \
    demographics, psychographics, or other relevant criteria. This enables personalized and targeted messaging.
    3. Digital Marketing: Utilize digital marketing strategies, including search engine optimization (SEO),\
    search engine marketing (SEM), email marketing, social media marketing, and content marketing, to increase brand visibility and drive traffic to relevant channels.
    Suggest multiple meta tags for improved SEO and similar things.
    4. Branding and Creative Elements: Develop branding elements to create a consistent and appealing brand identity.
    5. Message Development: Craft compelling and persuasive messages that communicate the unique value proposition \
    of the product or service. These messages should resonate with the target audience and differentiate the brand from competitors.
    6. Content Creation: Develop relevant and engaging content, such as blog posts, articles, \
    infographics, or social media posts, to attract and engage the target audience. This content should align with the campaign objectives and resonate with the audience's interests.
   
    The details of the product and the goals aimed to achieve by the marketing campign alongwith target audience given by the user\
        is below:
    Product Detail: {detail}\
    Goals: {goals}\
    Target Audience: {target_audience}\
        
    Tips:
    - Include each and every step of the marketing campaign.
    - Follow the description of each point and based on the data given by user generate answers.
    - Include all 6 points in the results
    - For each point try to give quote examples.

    """

    response = generate_response(prompt)
    print(response)
    response_data = {"answer": response}

    return JSONResponse(content=response_data, status_code=200)


# Set up your OpenAI API key
openai.api_key = ""


# Generate a response
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert marketing campaign adviser and generator.",
            },
            {"role": "user", "content": prompt}
            # {"role": "user", "content": "Based on the context below (which has top 5 responses) and your knowledge base, answer the following question: " + query + " according to Pakistani law."
            #     "\nAnswer as follows:" +
            #     "\nHere is the answer related to your query according to Pakistani law:" +
            #     # "\nHere is the answer from other sources:" +
            #     "\n---\n" + context}
        ],
        temperature=0.3,
    )
    response_text = f"\n{response.choices[0]['message']['content']}"
    return response_text


# search(
#     "I have a product that is related to hair growth and personal care for men",
#     "The goal for this campaign are to establish a brand image and tackle the target audience of young people",
#     "Target audience is generally people aging from 15-50",
# )
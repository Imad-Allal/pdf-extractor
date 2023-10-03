from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pdfminer.high_level import extract_text
from io import BytesIO
import requests, openai, os
import markdown
from starlette.responses import HTMLResponse


from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key")
def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header == openai.api_key:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

def extract_pdf_content(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        pdf_content = BytesIO(response.content)

        extracted_text = extract_text(pdf_content)

        return extracted_text
    
    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error extracting PDF content: {str(e)}")


def generate_course_plan(input_text: str) -> str:
    try:       
        
        messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates course plans"},
                    {"role": "user", "content": input_text},
                ]
        
        while True:
                message = input_text
                if message:
                    messages.append(
                        {"role": "user", "content": message},
                    )
                    chat = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo", messages=messages
                    )
                
                reply = chat.choices[0].message.content
                messages.append({"role": "assistant", "content": reply})

                markdown_course_plan = markdown.markdown(reply)
                return markdown_course_plan
        
    except Exception as e:
        print(f"Error generating course plan: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating course plan: {str(e)}")

@app.get("/course_plan")
async def course_plan(pdf_url: str, api_key: str = Security(get_api_key)):
    try:
        pdf_content = extract_pdf_content(pdf_url)
        course_plan_markdown = generate_course_plan(pdf_content)
        course_plan_html = markdown.markdown(course_plan_markdown)
        return HTMLResponse(content=course_plan_html, status_code=200)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating course plan: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Hello test"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

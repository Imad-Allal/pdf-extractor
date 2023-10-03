# pdf-extractor
Create a Lesson Plan suggestion API from PDF content

## Set-up
After installing FastAPI using the following command
```bash
pip install "fastapi[all]"
```
We will have to add some other packages:

### starlette
To use HTML functions
```bash
pip install starlette
```

### OpenAI
To use OpenAI functionalities
```bash
pip install openai
```

### pdfminer.six
For reading the PDF files
```bash
pip install pdfminer.six
```

### markdown
To markdown a simple text and turn in into HTML syntax
```bash
pip install markdown
```
## Available files
Two files are available: `main.py` and `main_v2.py`
The difference is that the second one uses security --athentication methods-- for the API key

## Running the files
### main.py
Create a `.env` file and init the variable `OPENAI_API_KEY` to you OpenAI API key (see `.env.example`)

After that, use the following command to run the API
```bash
uvicorn main:app --reload
```

### main_v2.py
Same instructions as `main.py` with the .env file, then run the following command
```bash
uvicorn main_v2:app --reload
```
After that, specify the header and the API key in the terminal:
```bash
curl -X GET "http://localhost:8000/course_plan?pdf_url=INSERT_PDF_URL" -H "X-API-Key: $OPENAI_API_KEY"
```
If the API key is valid, you will receive a response with the message “Access granted!”. Otherwise, an HTTP 401 Unauthorized status code will be returned.

## Endpoints
To begin with API, use the `course_plan` endpoint, specifying the PDF's url.

copy and past the following link to use the course generator:
`http://localhost:8000/course_plan?pdf_url=INSERT_PDF_URL`

Example:
`http://localhost:8000/course_plan?pdf_url=https://www.africau.edu/images/default/sample.pdf`


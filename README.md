# pdf-extractor
Create a Lesson Plan suggestion API from PDF content

#PDF LINK
curl -X GET "http://localhost:8000/course_plan?pdf_url=https://www.africau.edu/images/default/sample.pdf" -H "X-API-Key: $OPENAI_API_KEY"

curl -X GET "http://localhost:8000/protected" -H "X-API-Key: $OPENAI_API_KEY"

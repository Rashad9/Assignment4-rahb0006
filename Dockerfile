FROM python:3.11.9-slim

WORKDIR /app

ADD hangman.py /app/
COPY . .

CMD ["python" , "hangman.py"]
FROM python:3.8-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /home/gpt-3
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "/home/gpt-3/flask/run_gpt3.py"]

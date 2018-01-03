FROM python:3.5.4-alpine
WORKDIR /var/app

ADD ./ ./
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
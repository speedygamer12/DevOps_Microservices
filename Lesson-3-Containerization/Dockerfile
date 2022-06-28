From python:3.7.3-stretch

WORKDIR /app

COPY . flask_app/web.py /app/

RUN pip install --upgrade pip && /
    pip install -r requirements.txt
    
EXPOSE 80

CMD ["python", "web.py"]

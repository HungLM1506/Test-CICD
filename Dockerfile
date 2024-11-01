FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install  --no-cache-dir -r requirements.txt

COPY preprocessed_data.pkl .
CMD [ "python3", "model_serving.py" ]
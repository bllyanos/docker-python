FROM python:3-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod +x startup.sh

CMD source venv/bin/activate
CMD FLASK_APP=dashapp
CMD flask run --host=0.0.0.0
# CMD ["flask run app.py"]
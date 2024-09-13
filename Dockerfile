FROM python:3.11
RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy
CMD ["python", "app.py"]
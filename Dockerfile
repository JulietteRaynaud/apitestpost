FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . apitestpost
WORKDIR /apitestpost

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["makemigrations"]
CMD ["migrate"]
CMD ["runserver", "0.0.0.0:8000"]
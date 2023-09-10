FROM python:3.10
WORKDIR /ci_application
COPY . /ci_application
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver":"0.0.0.0:8000"]

FROM python:3.9-slim

COPY  ./FrontEnd/requirements.txt requirements.txt

RUN pip install -U pip && pip install -r requirements.txt
WORKDIR /app/FrontEnd

EXPOSE 8501

COPY  ./FrontEnd /app/FrontEnd

ENTRYPOINT ["streamlit","run"]
CMD ["/app/FrontEnd/main.py"]
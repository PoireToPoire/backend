FROM python:3.8

USER root
WORKDIR /usr/app
COPY . .

EXPOSE 8000
RUN pip install -r requirements.txt
ENTRYPOINT [ "uvicorn", "main:app" ]
CMD ["--host", "0.0.0.0", "--port", "8000"]
FROM python:3.9.18

RUN echo "This is printed during build time!"

RUN pip3 install flask

COPY ./my-app.py /app.py

ENTRYPOINT ["python3", "app.py"]

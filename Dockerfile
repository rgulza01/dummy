FROM python:3.8.9-slim-buster
#in the container, in a different place
WORKDIR /app 
COPY . . 
RUN pip3 install -r requirements.txt

ENV DATABASE_URI=${DATABASE_URI}
ARG DATABASE_URI
#RUN python3 create.py 

ENV SECRET_KEY=${SECRET_KEY}

EXPOSE 5001
ENTRYPOINT ["python", "app.py"]
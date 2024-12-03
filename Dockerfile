FROM debian

WORKDIR /app
COPY . .

RUN apt-get update
RUN apt-get install -y python3-pip python3 rustc python3-venv

ENV VIRTUAL_ENV=/home/app/venv
ENV MONGODB_URI=mongodb://mongo:27017/flask-app

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD ["python", "wsgi.py"]

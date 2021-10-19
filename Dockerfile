FROM python:3.9-alpine
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN adduser -D myuser
#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
USER myuser
WORKDIR /home/myuser
#COPY --chown=myuser:myuser requirements.txt requirements.txt
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install --user -r requirements.txt
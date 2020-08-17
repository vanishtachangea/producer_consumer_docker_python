FROM python:3.8-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /src
RUN ["chmod", "+x", "./commands.sh"]
ENTRYPOINT ["sh","./commands.sh"]

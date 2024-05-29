FROM python:3.11
WORKDIR /bot
COPY . /bot
RUN python3 -m pip install -r requirements.txt
CMD python3 main.py
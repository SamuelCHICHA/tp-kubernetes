FROM python:3.13-rc-slim
RUN pip3 install Flask
WORKDIR /app
COPY app/* /app
CMD python3 app.py

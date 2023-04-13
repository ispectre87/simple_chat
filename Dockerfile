FROM python:3.10.8-slim

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password chat_admin
RUN chown -R chat_admin /app
USER chat_admin

EXPOSE 8000/tcp

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

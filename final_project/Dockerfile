FROM python:3.10
WORKDIR /app
# Copiamos el requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]
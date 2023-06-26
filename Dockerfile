# Imagem base
FROM python:3.9-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Copia o código do aplicativo
COPY . .

# Instala as dependências do sistema operacional
RUN apt-get update \
    && apt-get install -y wget gnupg2 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Chromium e o pyppeteer
RUN pip install --no-cache-dir pyppeteer-install \
    && python -m pyppeteer-install

# Expõe a porta do aplicativo
EXPOSE 8000

# Inicia o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Usando uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install -r requirements.txt

# Expondo a porta que o Flask vai usar
EXPOSE 3000

# Define o comando para iniciar a aplicação
CMD ["python", "app.py"]
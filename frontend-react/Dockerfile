# Usando Node.js como base
FROM node:18

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências e instalar
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copiar código do frontend
COPY frontend .

# Construir a aplicação Next.js
RUN npm run build

# Expor a porta do Next.js
EXPOSE 3000

# Comando para rodar o frontend
CMD ["npm", "start"]

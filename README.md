# 🧭 Backpacker Route Finder

**Backpacker** é uma aplicação fullstack desenvolvida para ajudar mochileiros a planejarem suas rotas de viagem entre capitais europeias, utilizando o algoritmo de Dijkstra para calcular o caminho mais curto.

![Banner](https://source.unsplash.com/1600x400/?backpacking,adventure,travel)

---

## ✨ Funcionalidades

- 🌍 Interface bonita e responsiva inspirada em sites de turismo premium
- 📍 Cálculo do melhor caminho entre cidades usando o algoritmo de Dijkstra
- 🔁 Integração entre frontend (React) e backend (FastAPI)
- 🧠 UX amigável e acessível
- 🎒 Ideal para mochileiros e exploradores!

---

## 🛠️ Tecnologias Utilizadas

### 🔹 Frontend

- React + Vite
- Tailwind CSS + Bootstrap
- Axios
- Font Awesome

### 🔹 Backend

- Python 3
- FastAPI
- Uvicorn

---

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/backpacker-route-finder.git
cd backpacker-route-finder
```

---

### 2. Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # No Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload       # ou: uvicorn main:app --reload --port 8001
```

---

### 3. Frontend (React + Vite)

```bash
cd frontend-react
npm install
npm run dev
```

Acesse em: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Exemplo de uso

1. Selecione sua cidade de origem e destino.
2. Clique em **Calcular Rota**.
3. A aplicação mostrará o caminho mais curto e a distância total entre os pontos selecionados.

---

## 📁 Estrutura do Projeto

```
📦 backpacker-route-finder
├── backend
│   ├── main.py
│   ├── algoritmo.py
│   └── requirements.txt
├── frontend-react
│   ├── src
│   │   ├── components
│   │   │   └── RouteFinder.jsx
│   │   └── App.jsx
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── index.html
```

---

## 🌐 Créditos de imagem

Imagens aleatórias do [Unsplash](https://unsplash.com/) utilizando a URL dinâmica, como:

```
https://source.unsplash.com/1600x900/?mountains,adventure,travel
```

---

## 📄 Licença

Projeto com fins educacionais e open-source. Fique à vontade para clonar, estudar, adaptar e usar!

---

## 🤝 Contribuições

Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias!  
Vamos construir algo incrível juntos ✨

# 📚 bookLookUp-API

Uma API simples desenvolvida em Python utilizando Flask, que permite buscar informações sobre livros a partir de um id fornecido. Projeto de aprendizado com base para aplicações que necessitam de dados bibliográficos.

## 🚀 Funcionalidades

- Busca de livros por título.
- Retorno de informações como autor e titulo.
- Estrutura simples e de fácil compreensão.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) 3.13.3
- [Flask](https://flask.palletsprojects.com/) - Microframework para desenvolvimento web

## 📦 Instalação

Clone o repositório:

   ```bash
   git clone https://github.com/pedrohenriferreira/bookLookUp-API.git
   ```

Instale as dependências:

   ```bash
   pip install flask
   ```

## ▶️ Executando a Aplicação

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

2. Acesse a aplicação no navegador:

   ```
   http://localhost:5000/
   ```

## 📄 Endpoints

- `GET /books/<id:>`: Retorna informações sobre o livro cujo id corresponde ao parâmetro fornecido.

  **Exemplo:**

  ```
  GET /books?title=Dom%20Casmurro
  ```

  **Resposta:**

  ```json
  {
    "id": 4,
    "title": "Dom Casmurro",
    "author": "Machado de Assis"
  },
  ```

# 🎬 API de Filmes com Django REST Framework

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework como parte do meu processo de aprendizado e aprimoramento como desenvolvedor backend.

A API permite gerenciar filmes, gêneros, atores e reviews, implementando operações completas de CRUD e seguindo os princípios REST.

---

## 🚀 Funcionalidades

- ✅ Cadastro, listagem, atualização e exclusão de:
  - Movies
  - Genres
  - Actors
  - Reviews
- ✅ Relacionamentos entre entidades
- ✅ API estruturada com boas práticas REST
- 🔐 Autenticação JWT

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite
- Django Admin
- DRF Browsable API

---

## 📦 Instalação e uso local

### 1. Clone o repositório:

```bash
git clone https://github.com/leonardofgc/flix-api.git
cd flix-api
```
### 2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Gere e execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor de desenvolvimento:

```bash
python manage.py runserver
```

### 7. Acesse no navegador:

    - API Browsable: http://localhost:8000/api/

    - Django Admin: http://localhost:8000/admin/

### 🧪 Testes da API

Você pode testar os endpoints usando:
    - Postman
    - Insomnia
    - Ou diretamente pela interface web do Django REST Framework
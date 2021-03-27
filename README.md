<h1 align="center">Math's Burguer</h1>

<p align="center">Landing Page responsiva e Backend em Django para um delivery de lanches</p>

<h3>Requisitos</h3>

<li>Python 3.8</li>

<h3>Dependências</h3>

<li>Criar ambiente virtual:</li>

```console
virtualenv venv
```

<li>Instalar dependências:</li>

```console
pip install -r requirements.txt
```

<li>Iniciar banco de dados:</li>

```console
python manage.py makemigrations
```

```console
python manage.py migrate
```

<h3>Iniciar servidor:</h3>

```console
python manage.py runserver
```

<h3>Criando um super usuário:</h3>
<p>Caso queira, você pode criar um super usuário para ter acesso direto as models:</p>

```console
python manage.py createsuperuser
```

<p>No navegador: </p>

```console
127.0.0.1:8000/admin/
```

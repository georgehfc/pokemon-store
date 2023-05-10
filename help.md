# Como criar um projeto Django usando apenas o terminal

## Requisitos
- Ter o Python e o pip  instalado

## Crie uma pasta para o seu projeto e entre na mesma
```sh
mkdir meu_projeto && cd meu_projeto
```

## Crie um ambiente virtual (venv) 
```sh
python -m venv venv
```

## Ativar o ambiente virtual recem criado
```sh
source venv/bin/activate
```

## Instale dentro do venv o django na última versão:
```sh
pip install django
```

## Crie de fato o projeto Django dentro da pasta atual
```sh
django-admin startproject setup .
```
O ponto (.) no final é para indicarmos que queremos criar toda a estrutura de diretórios do Django na pasta atual, 
do contrário ele cria uma nova pasta com o nome `setup` e dentro cria outra pasta com o nome `setup`, sendo a primeira 
para usarmos para construirmos os demais aplicativos, e a segunda para as configurações do Django.

Observação: Eu particularmente gosto de criar com o nome `setup`, assim fica tudo com relação as configurações e 
customizações da inicialização da aplicação, geralmente é dado o mesmo nome do projeto a está pasta, mas não gosto 
muito dessa convenção (opinião minha), assim você pode ver como `project`, `django_project`, `myproject` ou `config`.

Criando sem o ponto (.) no final, deve ficar da seguinte forma:
```
meu-projeto/
│
├── setup/
│   │
│   ├── setup/
│   |   ├── __init__.py
│   |   ├── asgi.py
│   |   ├── settings.py
│   |   ├── urls.py
│   |   └── wsgi.py
|   | 
│   └── manage.py
│
└── venv
```
Como o ponto:
```
meu-projeto/
│
├── setup/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

## Execute o projeto
```sh
python manage.py runserver
```

## Pronto, agora já pode abrir o seu editor de código favorito e começar a utilizar o django

## Outros passos que você pode querer usar

### Criar um novo app
```sh
python manage.py startapp <nome-do-app>
```
Lembre-se de adicionar o novo app no `setup.settings.INSTALLED_APPS`

### Salvar todas suas dependências no `requirements.txt`
```sh
pip freeze > requirements.txt
```

### Adicionar um `.gitignore` com `venv`

### Como executar o projeto diretamente pelo PyCharm
- Acesse `Run/Debug Configurations`
- Clique em `Add new run configuration`
- Selecione `Python`
- Coloque um `Name` para essa configuração de execução
- No campo `Script path`, selecione o arquivo `manage.py`
- No campo `Parameters` adicione `runserver`
- Agora clique em `Apply` e depois em `Ok` e execute o projeto.

### Execute as migrations
```sh
python manage.py migrate
```
Observação: Esse comando só vai funcionar depois que configurar os dados de acesso ao banco de dados.

### Criar um super usuário para acessar o admin
```sh
python manage.py createsuperuser
```

# Exercício

## Objetivo
Criar em Python e PyQt um aplicativo simples, que tenha:

- um menu que abra uma nova janela
- campos de entrada de vários tipos (texto, combobox, checkbox)
- uma função para salvamento dos dados inseridos em um arquivo .txt
- uma função para abertura do arquivo txt e exibição do seu conteúdo.

## Estrutura de pastas e arquivos
```text
exercicio
├── src/
│   ├── build/
│   ├── main/
│   │	└── main.py
│   └── test/
├── LICENSE
├── README.md
└── requirements.txt
```
## Requisitos
- Python
- Pip
- Virtualenv

## Instalação
1. [Clonar](https://github.com/jvsouza/crudpeople.git) ou [baixar](https://github.com/jvsouza/crudPeople/archive/refs/heads/main.zip) o repositório;

2. Crie um ambiente virtual
```sh
$ virtualenv venv
```
3. Ative o ambiente virtual:
```sh
$ exercicio/venv/scripts/activate
```
4. Instale as bibliotecas dependentes do projeto:
```sh
$ pip install -r requirements.txt
```

## Executar o programa
Execute o programa apontando arquivo main.py para o python:
```sh
$ python main.py
```
## Janela
[![](src/main/resources/img/preview.png "Programa exercício")]()

## Referências
- [Python](https://www.python.org/)
- [Qt](https://doc.qt.io/qt-5.15/)
- [Git](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)
- [GitIgnore](https://docs.gitlab.com/ee/api/templates/gitignores.html)
- [Markdown](https://docs.gitlab.com/ee/user/markdown.html)
- [License](https://docs.gitlab.com/ee/user/compliance/license_compliance/)

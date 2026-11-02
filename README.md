# Plataforma Informativa Sintrajoias — MVP

MVP acadêmico desenvolvido na disciplina de **Projeto de Software**.

O sistema organiza informações públicas em categorias para facilitar o acesso de trabalhadores do setor joalheiro a benefícios, serviços, comunicados e orientações.

> Os dados incluídos nesta versão são fictícios e utilizados apenas para fins acadêmicos e de validação do protótipo.

## Tecnologias

- Python 3.12
- Flask 3.1
- SQLAlchemy 2.1
- PostgreSQL em ambiente de produção
- SQLite para execução local e testes
- Pytest
- GitHub Actions

## Funcionalidades do MVP

- Visualização de categorias ativas.
- Listagem de conteúdos ativos por categoria.
- Visualização dos detalhes de um conteúdo.
- Estado vazio quando uma categoria não possui conteúdos.
- Página amigável quando um conteúdo não está disponível.
- Interface responsiva e navegação por teclado.

## Como executar localmente

### 1. Criar ambiente virtual

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Criar dados fictícios

```powershell
python seed.py
```

### 4. Executar

```powershell
python run.py
```

Abra no navegador:

`http://127.0.0.1:5000`

## Testes automatizados

```powershell
pytest --cov=app --cov-report=term-missing
```

## Variáveis de ambiente

Copie `.env.example` para `.env` quando for utilizar PostgreSQL ou configurar uma chave secreta própria.

Nunca publique o arquivo `.env` no GitHub.

## Estrutura

```text
app/
├── static/
├── templates/
├── __init__.py
├── config.py
├── models.py
└── routes.py

tests/
├── conftest.py
└── test_routes.py

.github/workflows/ci.yml
run.py
seed.py
requirements.txt
.env.example
.gitignore
README.md
```

## CI

O workflow do GitHub Actions executa automaticamente os testes e verifica cobertura mínima de 80% em pushes e Pull Requests para a branch `main`.

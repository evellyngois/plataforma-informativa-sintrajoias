import pytest

from app import create_app
from app.models import Base, Categoria, Conteudo


@pytest.fixture()
def app(tmp_path):
    database_path = tmp_path / "test.db"

    app = create_app({
        "TESTING": True,
        "DATABASE_URL": f"sqlite:///{database_path}",
        "SECRET_KEY": "test-secret",
    })

    session = app.extensions["db_session"]

    categoria = Categoria(
        nome="Benefícios",
        descricao="Benefícios fictícios para testes.",
        ativo=True,
    )
    session.add(categoria)
    session.flush()

    session.add(Conteudo(
        titulo="Auxílio Educação",
        resumo="Conteúdo de teste.",
        texto_conteudo="Detalhes do conteúdo fictício.",
        id_categoria=categoria.id_categoria,
        ativo=True,
    ))
    session.commit()

    yield app

    session.remove()
    Base.metadata.drop_all(app.extensions["db_engine"])


@pytest.fixture()
def client(app):
    return app.test_client()

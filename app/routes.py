from flask import Blueprint, abort, current_app, render_template
from sqlalchemy import select

from .models import Categoria, Conteudo

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    session = current_app.extensions["db_session"]
    categorias = session.scalars(
        select(Categoria)
        .where(Categoria.ativo.is_(True))
        .order_by(Categoria.nome)
    ).all()
    return render_template("index.html", categorias=categorias)


@bp.get("/categorias/<int:categoria_id>")
def categoria(categoria_id):
    session = current_app.extensions["db_session"]

    categoria_encontrada = session.scalar(
        select(Categoria).where(
            Categoria.id_categoria == categoria_id,
            Categoria.ativo.is_(True),
        )
    )

    if categoria_encontrada is None:
        abort(404)

    conteudos = session.scalars(
        select(Conteudo)
        .where(
            Conteudo.id_categoria == categoria_id,
            Conteudo.ativo.is_(True),
        )
        .order_by(Conteudo.data_publicacao.desc())
    ).all()

    return render_template(
        "categoria.html",
        categoria=categoria_encontrada,
        conteudos=conteudos,
    )


@bp.get("/conteudos/<int:conteudo_id>")
def conteudo(conteudo_id):
    session = current_app.extensions["db_session"]

    conteudo_encontrado = session.scalar(
        select(Conteudo).where(
            Conteudo.id_conteudo == conteudo_id,
            Conteudo.ativo.is_(True),
        )
    )

    if conteudo_encontrado is None or not conteudo_encontrado.categoria.ativo:
        abort(404)

    return render_template("conteudo.html", conteudo=conteudo_encontrado)


@bp.app_errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404

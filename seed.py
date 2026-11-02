from datetime import datetime, timezone

from sqlalchemy import select

from app import create_app
from app.models import Categoria, Conteudo

app = create_app()

with app.app_context():
    session = app.extensions["db_session"]

    if session.scalar(select(Categoria).limit(1)) is not None:
        print("O banco já possui dados. Nenhuma alteração foi realizada.")
        raise SystemExit(0)

    beneficios = Categoria(
        nome="Benefícios",
        descricao="Informações públicas sobre benefícios e apoios ao trabalhador.",
    )
    servicos = Categoria(
        nome="Serviços",
        descricao="Conheça os serviços e canais de atendimento disponíveis.",
    )
    comunicados = Categoria(
        nome="Comunicados",
        descricao="Avisos e informações importantes do Sintrajoias.",
    )
    orientacoes = Categoria(
        nome="Orientações",
        descricao="Orientações gerais para trabalhadores do setor joalheiro.",
    )

    session.add_all([beneficios, servicos, comunicados, orientacoes])
    session.flush()

    session.add_all([
        Conteudo(
            titulo="Auxílio Educação",
            resumo="Saiba como solicitar apoio educacional para cursos e capacitação.",
            texto_conteudo=(
                "Conteúdo fictício utilizado exclusivamente para demonstração acadêmica. "
                "Em uma versão real, esta página apresentaria informações públicas validadas pelo Sintrajoias."
            ),
            data_publicacao=datetime(2026, 10, 20, tzinfo=timezone.utc),
            id_categoria=beneficios.id_categoria,
        ),
        Conteudo(
            titulo="Convênio Saúde",
            resumo="Consulte informações gerais sobre atendimento e benefícios de saúde.",
            texto_conteudo=(
                "Conteúdo fictício utilizado exclusivamente para validação do protótipo."
            ),
            data_publicacao=datetime(2026, 10, 15, tzinfo=timezone.utc),
            id_categoria=beneficios.id_categoria,
        ),
        Conteudo(
            titulo="Vale-Transporte",
            resumo="Informações gerais sobre orientação relacionada ao vale-transporte.",
            texto_conteudo=(
                "Conteúdo fictício utilizado exclusivamente para validação do protótipo."
            ),
            data_publicacao=datetime(2026, 10, 10, tzinfo=timezone.utc),
            id_categoria=beneficios.id_categoria,
        ),
    ])

    session.commit()
    print("Dados fictícios cadastrados com sucesso.")

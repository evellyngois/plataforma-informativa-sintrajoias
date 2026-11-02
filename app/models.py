from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    descricao: Mapped[str | None] = mapped_column(String(255), nullable=True)
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    conteudos: Mapped[list["Conteudo"]] = relationship(
        back_populates="categoria",
        cascade="all, delete-orphan",
    )


class Conteudo(Base):
    __tablename__ = "conteudos"

    id_conteudo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(160), nullable=False)
    resumo: Mapped[str | None] = mapped_column(String(300), nullable=True)
    texto_conteudo: Mapped[str] = mapped_column(Text, nullable=False)
    data_publicacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    id_categoria: Mapped[int] = mapped_column(
        ForeignKey("categorias.id_categoria"), nullable=False, index=True
    )

    categoria: Mapped[Categoria] = relationship(back_populates="conteudos")

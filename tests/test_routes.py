def test_pagina_inicial_exibe_categoria(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert "Benefícios" in resposta.get_data(as_text=True)


def test_categoria_exibe_conteudo_ativo(client):
    resposta = client.get("/categorias/1")

    assert resposta.status_code == 200
    assert "Auxílio Educação" in resposta.get_data(as_text=True)


def test_conteudo_exibe_detalhes(client):
    resposta = client.get("/conteudos/1")

    assert resposta.status_code == 200
    pagina = resposta.get_data(as_text=True)
    assert "Auxílio Educação" in pagina
    assert "Detalhes do conteúdo fictício." in pagina


def test_categoria_inexistente_retorna_404(client):
    resposta = client.get("/categorias/999")

    assert resposta.status_code == 404
    assert "Conteúdo não disponível" in resposta.get_data(as_text=True)

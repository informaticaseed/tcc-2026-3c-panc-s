"""Fixo temporário"""

PANCS = {
    "ora-pro-nobis": {
        "nome_popular": "Ora-pro-nóbis",
        "nome_cientifico": "Pereskia aculeata",
        "descricao": (
            "Planta trepadeira muito rica em proteína, usada principalmente "
            "em Minas Gerais em refogados e recheios de tortas e pastéis."
        ),
        "beneficios": "Alto teor de proteína, ferro e cálcio.",
        "modo_uso": "Folhas cozidas em refogados, sopas, omeletes e recheios.",
        "imagem": "ora-pro-nobis.jpg",
    },
    "taioba": {
        "nome_popular": "Taioba",
        "nome_cientifico": "Xanthosoma sagittifolium",
        "descricao": (
            "Planta de folhas grandes parecidas com as do inhame, muito "
            "usada na culinária mineira e capixaba."
        ),
        "beneficios": "Rica em vitamina A, ferro e fibras.",
        "modo_uso": "Folhas sempre bem cozidas (nunca cruas) em refogados e recheios.",
        "imagem": "taioba.jpg",
    },
    "capuchinha": {
        "nome_popular": "Capuchinha",
        "nome_cientifico": "Tropaeolum majus",
        "descricao": (
            "Planta ornamental comestível, com flores e folhas de sabor "
            "picante parecido com agrião."
        ),
        "beneficios": "Fonte de vitamina C e compostos antimicrobianos.",
        "modo_uso": "Flores e folhas cruas em saladas, como decoração comestível.",
        "imagem": "capuchinha.jpg",
    },
    "bertalha": {
        "nome_popular": "Bertalha",
        "nome_cientifico": "Basella alba",
        "descricao": (
            "Trepadeira de folhas carnudas, também conhecida como espinafre-"
            "indiano, fácil de cultivar em quintais."
        ),
        "beneficios": "Rica em vitaminas A e C, cálcio e ferro.",
        "modo_uso": "Folhas cozidas em refogados, sopas e caldos.",
        "imagem": "bertalha.jpg",
    },
    "serralha": {
        "nome_popular": "Serralha",
        "nome_cientifico": "Sonchus oleraceus",
        "descricao": (
            "Erva espontânea comum em quintais e terrenos baldios, muito "
            "usada na culinária nordestina."
        ),
        "beneficios": "Fonte de vitaminas A e C e minerais.",
        "modo_uso": "Folhas jovens cruas em saladas ou cozidas em refogados.",
        "imagem": "serralha.jpg",
    },
    "vinagreira": {
        "nome_popular": "Vinagreira",
        "nome_cientifico": "Hibiscus sabdariffa",
        "descricao": (
            "Também chamada de caruru-azedo, típica da culinária do "
            "Maranhão, com sabor levemente ácido."
        ),
        "beneficios": "Rica em vitamina C e antioxidantes.",
        "modo_uso": "Folhas cozidas em arroz e refogados; cálices usados em chás.",
        "imagem": "vinagreira.jpg",
    },
}


def listar_pancs():
    """Retorna a lista de PANCs (id + dados) ordenada por nome popular."""
    itens = [{"id": chave, **dados} for chave, dados in PANCS.items()]
    return sorted(itens, key=lambda p: p["nome_popular"])


def buscar_panc(panc_id):
    """Retorna os dados de uma PANC pelo id, ou None se não existir."""
    dados = PANCS.get(panc_id)
    if dados is None:
        return None
    return {"id": panc_id, **dados}

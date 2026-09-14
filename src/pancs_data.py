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
        "credito_imagem": "Ricardosdag/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Pereskia_aculeata",
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
        "credito_imagem": "Angrense/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Xanthosoma_sagittifolium",
        "precisa_preparo": True,
        "aviso_preparo": (
            "Nunca coma a taioba crua: ela tem oxalato de cálcio, que irrita "
            "a boca e a garganta. Precisa ser sempre bem cozida antes de comer."
        ),
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
        "credito_imagem": "J-Luc/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Tropaeolum_majus",
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
        "credito_imagem": "Shizhao/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Basella_alba",
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
        "credito_imagem": "Wildfeuer/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Sonchus_oleraceus",
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
        "credito_imagem": "Salil Kumar Mukherjee/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Hibiscus_sabdariffa",
    },
    "babosa": {
        "nome_popular": "Babosa",
        "nome_cientifico": "Aloe vera",
        "descricao": (
            "Planta suculenta de folhas grossas cheias de um gel "
            "transparente, muito conhecida por uso medicinal e cosmético, "
            "mas também usada na alimentação."
        ),
        "beneficios": "Hidratante, auxilia a digestão e tem ação anti-inflamatória.",
        "modo_uso": "Gel usado em sucos, geleias e sobremesas.",
        "imagem": "babosa.jpg",
        "credito_imagem": "MidgleyDJ/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Aloe_vera",
        "precisa_preparo": True,
        "aviso_preparo": (
            "Logo abaixo da casca da babosa existe uma seiva amarela "
            "(aloína) que é laxante forte e não deve ser consumida. Retire "
            "a casca e lave bem o gel transparente antes de usar."
        ),
    },
    "pitaya": {
        "nome_popular": "Pitaya",
        "nome_cientifico": "Hylocereus undatus",
        "descricao": (
            "Cacto trepador de origem tropical, conhecido pelo fruto "
            "exótico de polpa branca ou vermelha com sementes pretas "
            "comestíveis, também chamado de fruta-do-dragão."
        ),
        "beneficios": "Rica em vitamina C, antioxidantes e fibras.",
        "modo_uso": "Fruto consumido in natura, cortado ao meio e comido com colher, ou em sucos e saladas de frutas.",
        "imagem": "pitaya.jpg",
        "credito_imagem": "Webysther Nunes/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Pitaia",
    },
    "mandacaru": {
        "nome_popular": "Mandacaru",
        "nome_cientifico": "Cereus jamacaru",
        "descricao": (
            "Cacto colunar típico da caatinga nordestina, resistente à "
            "seca. Seus frutos e cladódios (partes carnudas do caule) "
            "podem ser consumidos."
        ),
        "beneficios": "Fonte de fibras e água; ajuda na alimentação em períodos de seca.",
        "modo_uso": "Fruto consumido in natura; os cladódios (a \"palma\") são cozidos em refogados.",
        "imagem": "mandacaru.jpg",
        "credito_imagem": "Hervé Lefebvre/Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Mandacaru",
        "precisa_preparo": True,
        "aviso_preparo": (
            "O mandacaru tem espinhos grandes por todo o corpo. É preciso "
            "remover todos os espinhos com cuidado antes de manusear ou "
            "preparar qualquer parte da planta."
        ),
    },
    "menta": {
        "nome_popular": "Menta",
        "nome_cientifico": "Mentha × piperita",
        "descricao": (
            "Erva aromática de folhas verdes brilhantes e sabor "
            "refrescante mentolado, muito usada como tempero, chá e em "
            "receitas doces."
        ),
        "beneficios": "Auxilia a digestão e tem ação calmante e refrescante.",
        "modo_uso": "Folhas frescas usadas em chás, sucos, saladas e como tempero.",
        "imagem": "menta.jpg",
        "credito_imagem": "Wikipedia",
        "fonte_imagem": "https://pt.wikipedia.org/wiki/Hortel%C3%A3-pimenta",
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

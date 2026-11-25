biblioteca = {
    "Jane Eyre": {
        "autores": [("Charlotte Brontë", 1816, "Britânica")],
        "paginas": 659,
        "ano_publicacao": 1847,
        "generos": ["Ficção Vitoriana", "Romance de Formação (Bildungsroman)", "Histórico"],
        "avaliacao": 4.6,
        "disponivel": True,
        "emprestado_para": None,
    },
    "Python Illustrated": {
        "autores": [
            ("Zia van Putten", 2023, "Holandesa"),
            ("Maaike van Putten", 1991, "Holandesa"),
            ("Imke van Putten", 1997, "Holandesa"),
        ],
        "paginas": 432,
        "ano_publicacao": 2026,
        "generos": ["Informativo", "Educação"],
        "avaliacao": 5,
        "disponivel": False,
        "emprestado_para": "Jacob",
    },
    "Se os gatos desaparecessem do mundo": {
        "autores": [("Genki Kawamura", None, None)],
        "paginas": 144,
        "ano_publicacao": 2012,
        "generos": ["Ficção Literária", "Realismo Mágico", "Ficção Filosófica"],
        "avaliacao": 4.2,
        "disponivel": False,
        "emprestado_para": "Chai",
    },
}

print(list(biblioteca))
print("Romance" in biblioteca["Python Illustrated"]["generos"])
print(biblioteca["Jane Eyre"]["autores"][0][2])

gatos = biblioteca["Se os gatos desaparecessem do mundo"]
gatos["disponivel"] = True
gatos["emprestado_para"] = None

python = biblioteca["Python Illustrated"]
if python["disponivel"]:
    print("Python Illustrated está disponível")
else:
    print(f"Python Illustrated foi emprestado para {python['emprestado_para']}")

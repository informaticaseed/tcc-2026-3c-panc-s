# TCC 2026 — PANC'S 
**LTP3 + QP3 · CEMIC 2026 · Prof. Rafael Martins Alves**

---



## 👥 Integrantes

| Nome completo | GitHub | Turma |
|--------------|--------|-------|
| (Ana Carolina Carvalho Rodrigues) | anacarolrodrigues08-hue | 3C |

**Tema:** (Desenvolvimento de um site informativo sobre Plantas Alimentícias Não Convencionais (PANC’s).)
**Tecnologia:** Python + Flask + SQLite

---

## 🎯 O que o sistema faz

(O sistema consiste em um site informativo desenvolvido para divulgar conhecimento sobre as Plantas Alimentícias Não Convencionais (PANC’s). O objetivo é facilitar o acesso da população a informações confiáveis sobre identificação, benefícios e formas de utilização dessas plantas na alimentação do dia a dia.
O site busca promover educação alimentar e conscientização sobre alternativas sustentáveis e nutritivas presentes na biodiversidade brasileira.)

---

## 🔄 Como o grupo trabalha toda semana

1. **Segunda** — cada integrante abre Issues da semana (use o template "Tarefa Semanal")
2. **Durante a semana** — trabalham e fazem commits
3. **Sexta** — o grupo abre 1 Pull Request linkando as Issues concluídas
4. **Push** — métricas de participação aparecem automaticamente no Actions

---

## 📁 Estrutura do projeto

```
pancs_site/
│
├── app.py              # Arquivo principal do servidor Flask e rotas
├── pancs_data.py       # Arquivo com os dados das PANCs (aquele dicionário)
├── requirements.txt    # Dependências do projeto (Flask, pytest, etc.)
├── vercel.json         # Configuração de deploy para a Vercel
│
├── static/             # Pasta para arquivos que o navegador baixa direto
│   ├── css/            # Arquivos de estilização (.css)
│   └── imagens/        # Fotos e ilustrações das plantas
│
└── templates/          # Páginas HTML que o Flask renderiza
    ├── index.html      # Página inicial (Lista de plantas)
    └── detalhe.html    # Página com os detalhes de cada planta
```

---

## ⚡ Comandos rápidos

**Requisito:** Python 3.9 ou superior.

```bash
# Clonar o repositório
git clone <URL>
cd tcc-2026-3c-panc-s

# Criar e ativar o ambiente virtual (venv)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
source .venv/Scripts/activate
source .venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Rodar o projeto
python src/app.py
# Site disponível em http://127.0.0.1:5000

# Rodar os testes
pytest tests/ -v
```






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
tcc-2026-3c-panc-s/
│
├── requirements.txt        # Dependências do projeto (Flask, pytest, etc.)
├── .env.example             # Modelo do arquivo .env (copie e preencha)
│
└── src/
    ├── app.py               # Arquivo principal do servidor Flask e rotas
    ├── models.py            # Tabelas do banco: Usuario, Topico, Comentario
    ├── pancs_data.py        # Dados das PANCs (dicionário fixo)
    │
    ├── static/
    │   └── css/style.css    # Estilização (.css)
    │
    └── templates/           # Páginas HTML que o Flask renderiza
        ├── base.html            # Layout comum (menu, rodapé)
        ├── index.html           # Página inicial (lista de plantas)
        ├── detalhe.html         # Detalhes de cada planta
        ├── login.html
        ├── cadastro.html
        └── forum/
            ├── lista.html       # Lista de tópicos do fórum
            ├── novo_topico.html
            └── topico.html      # Tópico + comentários
```

---

## 🌱 Funcionalidades

- **Catálogo de PANCs** — lista e página de detalhe de cada planta (não exige login)
- **Cadastro e login de usuários** — senha guardada com hash, nunca em texto puro
- **Fórum** — qualquer pessoa pode ler os tópicos; criar tópico e comentar exige login

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

# Criar o arquivo .env (copie o modelo e preencha o SECRET_KEY)
cp .env.example .env

# Rodar o projeto
python src/app.py
# Site disponível em http://127.0.0.1:5000

# Rodar os testes
pytest tests/ -v
```

O banco de dados (`panc.db`, SQLite) é criado automaticamente na primeira vez que o site roda.

---

## Ver online

O site (https://anacarol.pythonanywhere.com) fica hospedado gratuitamente no **PythonAnywhere**, que usa o mesmo SQLite do desenvolvimento.

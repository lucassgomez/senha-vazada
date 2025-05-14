# 🔐 Verificador de Senhas Vazadas com Python

Este projeto verifica se senhas de usuários foram comprometidas em vazamentos de dados públicos, utilizando a API do [Have I Been Pwned](https://haveibeenpwned.com/Passwords).

## 💡 Como funciona

O programa:
1. Lê um arquivo `usuarios.csv` com colunas `usuario` e `senha`.
2. Converte cada senha para hash SHA-1.
3. Envia os 5 primeiros caracteres do hash para a API (privacidade preservada).
4. Compara localmente o restante do hash com os resultados da API.
5. Informa se a senha foi vazada e quantas vezes.

---

## 🗂 Estrutura do Projeto

senha-vazada/
│
├── verificador-senhas/           # Pasta contendo os arquivos principais do projeto
│   ├── verificador.py            # Código principal que realiza a verificação de senhas
│   ├── usuarios.csv             # Arquivo CSV com as senhas e e-mails dos usuários
│   └── README.md                # Este arquivo README
│
└── .git/                         # Arquivos de configuração do Git

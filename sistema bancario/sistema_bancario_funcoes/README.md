# Sistema Bancário com Funções (Python)

Desafio: refatorar o sistema bancário usando **funções** para depósito, saque e extrato.
Inclui **CLI interativo**, **boas práticas**, **testes unitários** e **README** com passo a passo para
criar o repositório no GitHub.

## Requisitos atendidos
- Operações: **depósito**, **saque**, **extrato**;
- **Funções** dedicadas para cada operação com validações;
- Limites: até **3 saques por dia** e **R$ 500,00** por saque;
- Bloqueio de valores inválidos (negativos/zero) e saques sem saldo;
- Registro de movimentações no **extrato** com data/hora;
- Interface de menu simples (CLI), fácil de testar;
- **Testes unitários** básicos (`pytest`).

## Como executar
```bash
# Requer Python 3.9+
cd src
python cli.py
```

## Estrutura
```
sistema_bancario_funcoes/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ src/
│  ├─ bank.py
│  └─ cli.py
└─ tests/
   └─ test_bank.py
```

## Passo a passo: criar repositório no GitHub (via navegador)
1. Acesse **github.com** → **New repository** → Nome: `sistema-bancario-funcoes` → Create.
2. No seu PC, abra o terminal dentro da pasta `sistema_bancario_funcoes`.
3. Rode:
   ```bash
   git init
   git add .
   git commit -m "feat: sistema bancário com funcoes, cli e testes"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/sistema-bancario-funcoes.git
   git push -u origin main
   ```
4. Atualize a página do repositório no GitHub e confira os arquivos.

> Se preferir **GitHub Desktop**: `File > Add local repository` e depois `Publish repository`.

## Passo a passo: criar repositório pelo Git (linha de comando)
```bash
# Dentro de sistema_bancario_funcoes
git init
git add .
git commit -m "feat: sistema bancario com funcoes"
git branch -M main
# Substitua SEU_USUARIO
git remote add origin https://github.com/SEU_USUARIO/sistema-bancario-funcoes.git
git push -u origin main
```

## Dicas
- Edite os limites em `cli.py` (constantes `MAX_SAQUES` e `LIMITE_SAQUE`).
- Rode os testes (se tiver `pytest`): `pytest -q`.
- Adapte este projeto ao enunciado da sua plataforma (DIO, etc.).

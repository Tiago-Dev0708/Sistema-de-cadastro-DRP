# Sistema-de-cadastro-DRP

O sistema consiste em cadastrar clientes e pedidos, fazendo uso de um menu interativo via cli com o usuário, além de uma documentação via swagger e README.md


## 🚀 Configuração do Ambiente

### Pré-requisitos

1. Python 3.13+
2. Docker e Docker Compose

### Instalação

1. **Clone o repositório**:

```bash
git clone <repository-url>
cd Sistema-de-cadastro-DRP
```

2. **Configure as variáveis de ambiente**:

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. **Crie um ambiente virtual e instale as dependências(Usando o venv no exemplo)**:

```bash
Criando um ambiente virtual: python3 -m venv venv

Ativando o ambiente no linux: source venv/bin/activate
Ativando o ambiente no Windows: ./venv/Scripts/activate

Instale as dependências com: pip install -r requirements.txt
```
5. **Execute o banco conteinerizado(obrigatório para o funcionamento da aplicação) e use as variaveis de ambiente para conexão com o banco e para vizualizar o mesmo pelo pgadmin**:

```bash
docker compose up -d postgres pgadmin
```
O pgadmin estará disponível em `http://localhost:5050`

5. **Execute a aplicação localmente**:

```bash
uvicorn api.main:app --reload
```

6. **Execute a aplicação conteinerizada**:

```bash
docker compose up -d --build api
```

A aplicação estará disponível em `http://localhost:8000`







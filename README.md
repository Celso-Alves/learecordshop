## Lea Record Shop

Projeto de um e-commerce utilizando Flask/Postgresql/Redis/Docker

## Introdução
Esse projeto foi criado com o intuido de mostrar a criação de APIs Restful em linguagem Python utilizando o framework Flask.

## Descrição do Projeto
O projeto se baseia na criação de uma pequena loja fictícia de discos Lea Record Shop que deseja vender
seu catalogo na internet através de um e-commerce simples.
Uma das premissas do projeto é garantir que não haja perda de desempenho devido a campanhas de marketing promocionais,ou seja,
em determinados momentos pode haver um alto nível de tráfico e é necessário que a aplicação mantenha um bom desempenho.

## Tecnologias utilizadas

### 🌶️ Flask 
Flask é um microframework para web escrito em Python. Ele faz uso da flexbilidade do Python para prover modelos de desenvolvimento web, com ele é possível escrever APIs escalaveis integradas com diversos bancos de dados e serviços de mensageria.Flask também tem uma excelente documentação e uma comunidade ativa.

### 🐘 Postgresql
PostgreSQL é um banco de dados relacional orientado a objetos (ORDBMS) baseado no pacote
INGRES (INteractive Graphics REtrieval System), que foi desenvolvido na University of California, Berkeley. 
O projeto POSTGRES (Post Ingres) foi iniciado em 1985 a verão 1 foi lançada para um pequeno número de usuários em 1989.
Agora, com mais de 20 anos de de desenvolvimento Postgresql se consolidou como um banco de dados agil e flexivel

### 🟥 Redis
O Redis é um armazenamento de estrutura de dados de chave-valor de código aberto e na memória. O Redis oferece um conjunto de estruturas versáteis de dados na memória que permite a fácil criação de várias aplicações personalizadas. Os principais casos de uso do Redis incluem cache, gerenciamento de sessões, PUB/SUB e classificações.
Por conta da sua velocidade e facilidade de uso, o Redis é uma escolha em alta demanda para aplicações web e móveis, como também de jogos, tecnologia de anúncios e IoT, que exigem o melhor desempenho do mercado. 

## Dependências 
Para esse projeto é necessário Python 3.9 ou superior e o gerenciador de pacotes PIP.


## Docker

Comando para iniciar

    docker-compose up -d --build

Conteudo do docker-compose.yml

    version: '3.1'
    
    services:
        web:
            build: .
            command: python run.py
            ports:
                - 5000:5000
            environment:
                - FLASK_APP=run.py
            env_file:
                - env.list
        db:
            image: postgres:13-alpine
            restart: always
            volumes:
                - postgres_data:/var/lib/postgresql/data/
            environment:
                - POSTGRES_USER=lea_shop
                - POSTGRES_PASSWORD=lea_shop2022
                - POSTGRES_DB=learecordshop_db
        redis:
            image: redis
            container_name: redis-container
            ports:
                - "6379:6379"
    volumes:
      postgres_data:


Após os containers serem iniciados, o seguinte endereço da API ficará disponivel [http://localhost:5000] ***


#### API
Abaixo estão uma lista dos endpoints com seus parametros, é necessário que a aplicação esteja rodando para que os endpoints funcionem.

### DISCOS  - Operações de Create, Read, Update, and Delete (CRUD)
    

#### READ 
|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/discos`| GET | Retorna listagem de disco(s)| /api/discos/\<ID\> Identificação única do disco|

Exemplo de saída
    
        {
        "3": {
        "nme_disco": "We are Reactive",
        "artista": "Hohpe",
        "estilo": "Indie",
        "ano_lancto": 2022,
        "quantidade": 500
        }
    }
#### CREATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/discos`| POST | Inclui um novo discos | Vide Body abaixo|

Exemplo do Body

        {
         "nme_disco": 'Time of the Oath', 
         "artista": "Helloween",
         "estilo": "Metal",
        "ano_lancto": 1996,
         "quantidade": 100
        }
    

#### READ - SEARCH

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/discos?`| GET | Pesquisa por query| /api/discos?\<campo\>=\<valor\>&\<campo\>=\<valor\>|

Exemplo:

    http://localhost:5000/api/discos?artista=Helloween

Saida:

    {
    "3": {
        "nme_disco": "Time of the Oath",
        "artista": "Helloween",
        "estilo": "Metal",
        "ano_lancto": 1996,
        "quantidade": 9450
         }
    }

#### UPDATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/discos`| PATCH | Altera um ou mais campos informados| /api/discos/\<ID\>|

 Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Sucesso         |
|404               |Not Found|Disco nao localizado pelo ID informado|

#### DELETE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/discos`| DELETE | Apaga o disco atráves do ID informado| /api/discos/\<ID\>|

 Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Sucesso         |
|404               |Not Found|Disco nao localizado pelo ID informado|


------------------------------------------------------------------------
### CLIENTES  - Operações de Read, Update, and Delete 
    

#### READ 
|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/clientes`| GET | Retorna listagem de clientes(s)| /api/clientes/\<ID\> Identificação única do disco|

Exemplo de saída
    
    {
        "1": {
        "nme_cliente": "joao",
        "email": "joao@joao.com",
        "telefone": "1199999999",
        "dt_nasc": "1981-04-24T00:00:00",
        "ativo": false,
        "nr_documento": "1234567890-123"
        }
    }

#### CREATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/clientes`| POST | Inclui um novo clientes | Vide Body abaixo|

Exemplo do Body

        {
        "nme_cliente": "jose",
        "email": "jose@jose.com",
        "telefone": "1199999999",
        "dt_nasc": "1981-04-24T00:00:00",
        "ativo": false,
        "nr_documento": "1234567890-123"
        }

#### UPDATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/clientes`| PATCH | Altera um ou mais campos informados| /api/clientes/\<ID\>|

 Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Sucesso         |
|404               |Not Found|cliente nao localizado pelo ID informado|

#### DELETE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/clientes`| DELETE | **'INATIVA'** o cliente atráves do ID informado| /api/clientes/\<ID\>|

 Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Cliente inativado com sucesso         |
|404               |Not Found|Cliente nao localizado pelo ID informado|

--------------------------------------------------------------------

### PEDIDOS  - Operações de Create, Read, Update, and Delete 
    

#### READ 
|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/pedidos`| GET | Retorna listagem de pedidos(s)| /api/pedidos/\<ID\> Identificação única do pedido|

Exemplo de saída
    
    {
    "1": {
        "id_disco": 3,
        "quantidade": 10,
        "id_cliente": 1,
        "dt_pedido": "2022-03-01T10:54:32",
        "nme_disco": "Time of the Oath",
        "nme_cliente": "jose"
    }

#### CREATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/pedidos`| POST | Inclui um novo Pedido | Vide Body abaixo|

Exemplo do Body

        {
        "nme_cliente": "jose",
        "email": "jose@jose.com",
        "telefone": "1199999999",
        "dt_nasc": "1981-04-24T00:00:00",
        "ativo": false,
        "nr_documento": "1234567890-123"
        }

Na postagem de um pedido, é necessário saber se há estoque disponivel para o mesmo. No caso, quando não houver estoque daquele produto,
a aplicação retorna uma mensagem e inclui o produto numa lista de espera, dessa forma o forma o cliente é avisado por e-mail quando a loja
repor o estoque

Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Pedido incluido com sucesso         |
|412               | Precondition Failed| `Vide Abaixo`|
|404               |Not Found|Disco nao localizado pelo ID informado|

#### Mensagens de erro Código 412
1. Erro Cliente nao localizado pelo ID informado ou não ativo
2. Infelismente esse disco acabou :( , mas não se preocupe, vamos incluir seu nome na lista de espera,assim que estiver disponivel te informamos por e-mail


#### UPDATE

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/pedidos`| PATCH | Altera um ou mais campos informados| /api/pedidos/\<ID\>|

 Codigos de retorno HTTP Status
 
|Código de Retorno |Status| Definição |
|------------------|------|-----------|
|400               |OK    |Sucesso         |
|404               |Not Found|pedido nao localizado pelo ID informado|

#### READ - SEARCH

|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|`http://localhost:5000/api/pedidos?`| GET | Pesquisa por query| /api/pedidos?\<campo\>=\<valor\>&\<campo\>=\<valor\>|

Exemplo:

    http://localhost:5000/api/pedidos?nme_cliente=jose&dt_ini=28/02/2022&dt_fim=03/03/2022

Saida:

```
   {
   "1": {
        "id_disco": 3,
        "quantidade": 10,
        "id_cliente": 1,
        "dt_pedido": "2022-03-01T10:54:32",
        "nme_disco": "Time of the Oath",
        "nme_cliente": "jose"
        }
    }
```

### Instalação
Instalação dos frameworks necessários

    pip install -r requirements.txt
    
### TDD - Testes integração
Testes são um dos mais fortes pilares de qualquer software antes, durante e depois do desenvolvimento.Especialmente nos caso de microservicos web onde a aplicação
vai lidar com um grande volume de tráfego
    
   python app_tests.py -v


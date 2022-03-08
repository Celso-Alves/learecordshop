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


### API
Abaixo estão uma lista dos endpoints com seus parametros, é necessário que a aplicação esteja rodando para que os endpoints funcionem.

#### Clientes
    
|Endpoint | Método | Descrição|Paramêtros|
|---------|--------|----------|-------|
|http://localhost:5000/api/clientes/| GET | Retorna listagem de cliente(s)| /api/clientes/\<ID\> Identificação única do Cliente|

Exemplo de saída
    
        {
        "3": {
            "nme_disco": "Time of the Oath",
            "artista": "Helloween",
            "estilo": "Metal",
            "ano_lancto": 1996,
            "quantidade": 9450
        }
    }





### Instalação
Instalação dos frameworks necessários

    pip install -r requirements.txt
    
### TDD - Testes integração
Testes são um dos mais fortes pilares de qualquer software antes, durante e depois do desenvolvimento.Especialmente nos caso de microservicos web onde a aplicação
vai lidar com um grande volume de tráfego
    
    python app_tests.py -v

### Configuração




Os dados são persistidos em um container com Postgresql. Também foi utilizando Redis para fazer cache.
Este projeto foi escrito usando o Visual Studio Code 1.65

<h2>Run locally with docker</h2>

> Status do Projeto: Concluido :heavy_check_mark:
## Linguagens e libs utilizadas :books:

- [React PDF](https://react-pdf.org/): versão xx.xxx 

### Participante: 
|name|email|present|receiveCertificate|course|
| -------- | -------- | -------- |-------- | -------- |
|Chaiana Hermes|chaiana_hermes@yahoo.com.br|true|false|Bootcamp React|

    sudo apt update
    sudo apt install snapd

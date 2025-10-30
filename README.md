# 🚀 API de Cupons
Uma API REST simples, construída com Python e Flask, para consultar e filtrar uma lista de cupons de desconto.

## 📖 Sobre o Projeto
Este projeto expõe um conjunto de endpoints GET para interagir com uma coleção de dados de cupons (mantida em memória). 
O objetivo principal é fornecer uma maneira rápida e estruturada de filtrar cupons por empresa e/ou categoria.

### Principais Recursos
- Listar todos os cupons disponíveis.
- Listar todas as empresas e categorias únicas.
- Filtrar cupons por empresa.
- Filtrar cupons por categoria.
- Filtrar cupons por uma combinação de empresa e categoria.
- Respostas de erro em JSON (404) quando nenhum resultado é encontrado.

## 🛠️ Começando
Siga estas instruções para obter uma cópia local do projeto e executá-la.

### Pré-requisitos
Você precisará ter o Python 3.8+ e o pip (gerenciador de pacotes do Python) instalados em sua máquina.

### Instalação
Clone o repositório para sua máquina local:

```sh
git clone https://github.com/damatomos/flask-api-cupom.git
cd flask-api-cupom
```

(Recomendado) Crie e ative um ambiente virtual (virtualenv) para isolar as dependências do projeto:
```sh
# Windows
python -m venv venv
.\venv\Scripts\activate
```
```sh
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Instale a única dependência do projeto, o Flask:

```sh
pip install Flask
```

## 🏃‍♀️ Como Executar
Com o ambiente virtual ativado e o Flask instalado, execute o seguinte comando no seu terminal:

```sh
python app.py
```
O servidor será iniciado em modo de debug, o que significa que ele reiniciará automaticamente a cada alteração no código.

Você verá uma saída similar a esta:

 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!

A API agora está acessível em http://127.0.0.1:5000.

## 📚 Guia da API (Endpoints)
Aqui estão todos os endpoints disponíveis na API.

### Endpoint Raiz (Descoberta)
> GET /

Descrição: Retorna uma mensagem de boas-vindas e um mapa de todas as rotas disponíveis na API.

Exemplo de Resposta:

```JSON

{
  "mensagem": "Bem-vindo à API de Cupons!",
  "rotas": {
    "/cupons": "Retorna todos os cupons",
    "/cupons/categoria/list": "Retorna a lista de categorias encontradas",
    "/cupons/categoria/<nome_categoria>": "Retorna cupons de uma categoria"
  }
}
```

### Endpoints de Cupons
> GET /cupons

Descrição: Retorna a lista completa de todos os cupons.

Exemplo de Resposta:

```JSON

[
  {"id": 1, "empresa": "Amazon", "categoria": "Eletrônicos", "codigo": "AMZ10", "desconto": "10%"},
  {"id": 2, "empresa": "Netflix", "categoria": "Streaming", "codigo": "NET20", "desconto": "20%"}
]
```

### Endpoints de Categoria
> GET /cupons/categoria/list

Descrição: Retorna uma lista de todas as categorias únicas disponíveis.

Exemplo de Resposta:

```JSON

["Eletrônicos", "Streaming", "Roupas", "Livros"]
```

>  GET /cupons/categoria/<nome_categoria>

Descrição: Retorna todos os cupons que correspondem à categoria especificada (case-insensitive).

Exemplo de URL: http://127.0.0.1:5000/cupons/categoria/eletronicos

Exemplo de Resposta:

```JSON

[
  {"id": 1, "empresa": "Amazon", "categoria": "Eletrônicos", "codigo": "AMZ10", "desconto": "10%"},
  {"id": 3, "empresa": "Submarino", "categoria": "Eletrônicos", "codigo": "SUB15", "desconto": "15%"}
]
```

Resposta de Erro (404):

```JSON

{"erro": "Nenhum cupom encontrado para a categoria 'games'"}
```

### Endpoints de Empresa
> GET /cupons/empresa/list

Descrição: Retorna uma lista de todas as empresas únicas disponíveis.

Exemplo de Resposta:

```JSON

["Amazon", "Netflix", "Submarino", "Nike"]
```

> GET /cupons/empresa/<nome_empresa>

Descrição: Retorna todos os cupons que correspondem à empresa especificada (case-insensitive).

Exemplo de URL: http://127.0.0.1:5000/cupons/empresa/amazon

Exemplo de Resposta:

```JSON

[
  {"id": 1, "empresa": "Amazon", "categoria": "Eletrônicos", "codigo": "AMZ10", "desconto": "10%"},
  {"id": 5, "empresa": "Amazon", "categoria": "Livros", "codigo": "BOOK5", "desconto": "5%"}
]
```

Endpoints Combinados
> GET /cupons/empresa/<nome_empresa>/categoria/list

Descrição: Retorna uma lista de categorias únicas para uma empresa específica.

Exemplo de URL: http://127.0.0.1:5000/cupons/empresa/amazon/categoria/list

Exemplo de Resposta:

```JSON

["Eletrônicos", "Livros"]
```

> GET /cupons/empresa/<nome_empresa>/categoria/<nome_categoria>

Descrição: Retorna os cupons que correspondem tanto à empresa quanto à categoria especificadas.

Exemplo de URL: http://127.0.0.1:5000/cupons/empresa/amazon/categoria/livros

Exemplo de Resposta:

```JSON

[
  {"id": 5, "empresa": "Amazon", "categoria": "Livros", "codigo": "BOOK5", "desconto": "5%"}
]
```

## 🤝 Como Contribuir
Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. 
Quaisquer contribuições que você fizer serão muito bem-vindas.

1. Faça um Fork do projeto

2. Crie sua Feature Branch (git checkout -b feature/NovaFeature)

3. Faça o Commit de suas mudanças (git commit -m 'Adicionando NovaFeature')

4. Faça o Push para a Branch (git push origin feature/NovaFeature)

5. Abra um Pull Request

### 📄 Licença
Distribuído sob a Licença MIT. 
Veja o arquivo LICENSE.md para mais informações.

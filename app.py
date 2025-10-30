import os
from flask import Flask, request, jsonify

cupons = [
    {"id": 1, "empresa": "Amazon", "categoria": "Eletrônicos", "codigo": "AMZ10", "desconto": "10%"},
    {"id": 2, "empresa": "Netflix", "categoria": "Streaming", "codigo": "NET20", "desconto": "20%"},
    {"id": 3, "empresa": "Submarino", "categoria": "Eletrônicos", "codigo": "SUB15", "desconto": "15%"},
    {"id": 4, "empresa": "Nike", "categoria": "Roupas", "codigo": "NIK25", "desconto": "25%"},
    {"id": 5, "empresa": "Amazon", "categoria": "Livros", "codigo": "BOOK5", "desconto": "5%"},
]

def bootstrap() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'development'),
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def home():
        return jsonify({
            "mensagem": "Bem-vindo à API de Cupons!",
            "rotas": {
                "/cupons": "Retorna todos os cupons",
                "/cupons/categoria/list": "Retorna a lista de categorias encontradas",
                "/cupons/categoria/<nome_categoria>": "Retorna cupons de uma categoria",
                "/cupons/empresa/list": "Retorna a lista de empresas encontradas",
                "/cupons/empresa/<nome_empresa>": "Retorna cupons de uma empresa",
                "/cupons/empresa/<nome_empresa>/categoria/list": "Retorna categorias de uma empresa",
                "/cupons/empresa/<nome_empresa>/categoria/<nome_categoria>": "Retorna cupons de uma empresa em uma categoria",
            }
        })

    @app.route("/cupons", methods=["GET"])
    def get_cupons():
        return jsonify(cupons)
    
    @app.route("/cupons/categoria/list", methods=["GET"])
    def get_categorias():
        categorias = list(set(c["categoria"] for c in cupons))
        return jsonify(categorias)

    @app.route("/cupons/categoria/<string:categoria>", methods=["GET"])
    def get_cupons_por_categoria(categoria):
        resultado = [c for c in cupons if c["categoria"].lower() == categoria.lower()]
        if not resultado:
            return jsonify({"erro": f"Nenhum cupom encontrado para a categoria '{categoria}'"}), 404
        return jsonify(resultado)
    
    @app.route("/cupons/empresa/list", methods=["GET"])
    def get_empresas():
        empresas = list(set(c["empresa"] for c in cupons))
        return jsonify(empresas)

    @app.route("/cupons/empresa/<string:empresa>", methods=["GET"])
    def get_cupons_por_empresa(empresa):
        resultado = [c for c in cupons if c["empresa"].lower() == empresa.lower()]
        if not resultado:
            return jsonify({"erro": f"Nenhum cupom encontrado para a empresa '{empresa}'"}), 404
        return jsonify(resultado)
    
    @app.route("/cupons/empresa/<string:empresa>/categoria/list", methods=["GET"])
    def get_categorias_por_empresa(empresa):
        categorias = list(set(c["categoria"] for c in cupons if c["empresa"].lower() == empresa.lower()))
        if not categorias:
            return jsonify({"erro": f"Nenhuma categoria encontrada para a empresa '{empresa}'"}), 404
        return jsonify(categorias)

    @app.route("/cupons/empresa/<string:empresa>/categoria/<string:categoria>", methods=["GET"])
    def get_cupons_por_empresa_e_categoria(empresa, categoria):
        resultado = [c for c in cupons if c["empresa"].lower() == empresa.lower() and c["categoria"].lower() == categoria.lower()]
        if not resultado:
            return jsonify({"erro": f"Nenhum cupom encontrado para a empresa '{empresa}' na categoria '{categoria}'"}), 404
        return jsonify(resultado)

    return app


app = bootstrap()

if __name__ == '__main__':
    app.run(debug=True)
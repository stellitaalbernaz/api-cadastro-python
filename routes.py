from flask import jsonify, request
from database import conectar, criar_tabela

criar_tabela()

def configurar_rotas(app):
    @app.route("/")
    def home():
        return jsonify({"mensagem": "API funcionando!"})
    
    @app.route("/usuarios", methods=["POST"])
    def criar_usuario():
        dados = request.json
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", 
            (dados["nome"], dados["email"])
        )
        conn.commit()
        conn.close()
        return jsonify(dados), 201
    @app.route("/usuarios", methods=["GET"])
    def listar_usuarios():
        conn = connectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        lista = [
            {"id": u[0], "nome": u[1], "email": u[2]}
            for u in usuarios
        ]
        return jsonify(lista)
    @app.route("/usuarios/<int:id>", methods=["PUT"])
    def atualizar_usuario(id):
        dados = request.json
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome=?, email=? WHERE id=?", (dados["nome"], dados["email"], id)
        )
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário atualizado"})
    
    @app.route("/usuarios/<int:id", methods=["DELETE"])
    def deletar_usuario(id)
       conn = conectar()
       cursor = conn.cursor()
       cursor.execute("DELETE FROM usuarios WHERE id=?", (id))
       conn.commit()
       conn.close()
       return jsonify({"mensagem": "Usuário removido"})
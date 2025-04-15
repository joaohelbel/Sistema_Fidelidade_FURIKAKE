from flask import Flask, request, jsonify
from blockchain import Blockchain
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

blockchain = Blockchain()


@app.route('/comprar', methods=['POST'])
def registrar_compra():
    dados = request.get_json()
    if not dados or 'cpf' not in dados or 'valor' not in dados:
        return jsonify({'erro': 'Dados inválidos'}), 400

    bloco = blockchain.adicionar_bloco(dados)
    return jsonify({
        'mensagem': 'Compra registrada!',
        'index': bloco.index,
        'hash': bloco.hash,
        'dados': bloco.dados
    }), 201

@app.route('/cadeia', methods=['GET'])
def ver_cadeia():
    cadeia = [{
        'index': b.index,
        'timestamp': b.timestamp,
        'dados': b.dados,
        'hash': b.hash,
        'previous_hash': b.previous_hash
    } for b in blockchain.chain]
    return jsonify(cadeia), 200

@app.route('/validar', methods=['GET'])
def validar():
    valido = blockchain.validar()
    return jsonify({'valido': valido}), 200

def saldo_cliente(self, cpf):
    return {
        'cpf': cpf,
        'carimbos': self.carimbos_por_cliente.get(cpf, 0),
        'pratos': sum(
            1 for b in self.chain
            if isinstance(b.dados, dict) and b.dados.get('cpf') == cpf and b.dados.get('pratos_ganhos') > 0
        )
    }


if __name__ == '__main__':
    app.run(debug=True)

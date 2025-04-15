from flask import Flask, request, jsonify
from blockchain import Blockchain
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

blockchain = Blockchain()


@app.route('/nota', methods=['POST'])
def registrar_por_nota():
    dados = request.get_json()
    if not dados or 'cpf' not in dados or 'nome' not in dados or 'chave' not in dados:
        return jsonify({'erro': 'Dados inválidos'}), 400

    chave = dados['chave']
    
    # Simulação de "leitura da nota fiscal"
    valor_simulado = simular_leitura_nota(chave)

    compra = {
        'nome': dados['nome'],
        'cpf': dados['cpf'],
        'valor': valor_simulado
    }

    bloco = blockchain.adicionar_bloco(compra)

    return jsonify({
        'mensagem': 'Compra registrada via nota!',
        'valor_lido': valor_simulado,
        'index': bloco.index,
        'dados': bloco.dados
    }), 201

def simular_leitura_nota(chave):
    # Simulação com base nos últimos dígitos da chave
    try:
        digito = int(chave[-1])
        return 35 + (digito * 2)  # Ex: último dígito 3 → R$41
    except:
        return 30.0  # Valor mínimo

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

@app.route('/saldo/<cpf>', methods=['GET'])
def saldo(cpf):
    resultado = blockchain.saldo_cliente(cpf)
    return jsonify(resultado), 200



if __name__ == '__main__':
    app.run(debug=True)

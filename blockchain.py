import hashlib
import json
from time import time

class Bloco:
    def __init__(self, index, timestamp, dados, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.dados = dados
        self.previous_hash = previous_hash
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        conteudo = f'{self.index}{self.timestamp}{json.dumps(self.dados)}{self.previous_hash}'
        return hashlib.sha256(conteudo.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.criar_bloco_genesis()]
        self.carimbos_por_cliente = {}

    def criar_bloco_genesis(self):
        return Bloco(0, time(), "Bloco Gênesis", "0")

    def get_ultimo_bloco(self):
        return self.chain[-1]

    def adicionar_bloco(self, compra):
        cliente = compra['cliente']
        valor = float(compra['valor'])

        carimbos_atuais = self.carimbos_por_cliente.get(cliente, 0)
        carimbos_ganhos = 1 if valor > 39.9 else 0
        carimbos_totais = carimbos_atuais + carimbos_ganhos

        pratos_ganhos = carimbos_totais // 10
        carimbos_restantes = carimbos_totais % 10

        self.carimbos_por_cliente[cliente] = carimbos_restantes

        dados_bloco = {
            'cliente': cliente,
            'valor': valor,
            'carimbo_gerado': bool(carimbos_ganhos),
            'carimbos_atuais': carimbos_restantes,
            'pratos_ganhos': pratos_ganhos
        }

        ultimo = self.get_ultimo_bloco()
        novo = Bloco(
            index=ultimo.index + 1,
            timestamp=time(),
            dados=dados_bloco,
            previous_hash=ultimo.hash
        )
        self.chain.append(novo)
        return novo

    def validar(self):
        for i in range(1, len(self.chain)):
            atual = self.chain[i]
            anterior = self.chain[i - 1]
            if atual.hash != atual.calcular_hash():
                return False
            if atual.previous_hash != anterior.hash:
                return False
        return True

    def saldo_cliente(self, nome):
        return {
            'cliente': nome,
            'carimbos': self.carimbos_por_cliente.get(nome, 0),
            'pratos': sum(1 for b in self.chain if isinstance(b.dados, dict) and b.dados.get('cliente') == nome and b.dados.get('pratos_ganhos') > 0)
        }

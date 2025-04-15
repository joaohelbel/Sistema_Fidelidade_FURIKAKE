
# 🥢 Furikake Fidelidade – Sistema de Carimbos com Blockchain

Este é um sistema de fidelidade que simula o acúmulo de **carimbos** a cada compra realizada, utilizando **tecnologia blockchain** para registrar os dados de forma segura e transparente. O front-end foi inspirado na identidade visual da Furikake Daily Food 🍱.

---

## ✨ Funcionalidades

✅ Registro de compras via nota fiscal (simulado com chave)  
✅ Acúmulo de carimbos a cada compra acima de R$39,90  
✅ A cada 10 carimbos, o cliente ganha 1 prato  
✅ Consulta de carimbos e pratos pelo CPF  
✅ Cartela visual de carimbos em estilo "loyalty card"  
✅ Blockchain com hash, índice, timestamp e integridade entre blocos

---

## 🖼️ Interface

A interface inclui:
- Formulário para envio da nota fiscal
- Visualização da quantidade de carimbos
- Sistema de validação da integridade da blockchain
- Cartela gráfica com SVG ou ícones

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/fidelidade-furikake.git
cd fidelidade-furikake
```

### 2. Instale as dependências

```bash
pip install flask flask-cors
```

### 3. Execute o back-end

```bash
python app.py
```

Ele irá rodar em `http://localhost:5000`

### 4. Rode o front-end

Abra o arquivo `index.html` que está dentro da pasta `frontend/` usando Live Server (recomendado) ou clique duplo.

---

## 📦 Estrutura do Projeto

```
.
├── app.py
├── blockchain.py
├── requirements.txt
└── frontend/
    ├── index.html
    ├── style.css
    ├── script.js
    └── icone-carimbo.svg (opcional)
```

---

## 🔐 Sobre o Blockchain

Cada compra é registrada como um bloco com:
- Hash único baseado nos dados + hash anterior
- Timestamp
- Nome, CPF, valor, carimbos e pratos
- Ligação com o bloco anterior via `previous_hash`

---

## 🔧 Melhorias Futuras

- Leitura real de QR Code da nota fiscal (NFC-e)
- OCR com PyTesseract para ler valores de notas em imagem
- Painel de administração com ranking de clientes fiéis
- Login com CNPJ para lojistas acompanharem as premiações

---

## 💼 Feito por

**João Pedro**  
Sistema de Fidelidade baseado em Blockchain  
ESPM – Ciência de Dados para Negócios  

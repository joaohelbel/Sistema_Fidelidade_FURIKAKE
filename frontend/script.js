
function registrarNota() {
  const nome = document.getElementById('nome').value;
  const cpf = document.getElementById('cpf').value;
  const chave = document.getElementById('chave').value;

  if (!nome || !cpf || !chave) {
    alert("Preencha todos os campos.");
    return;
  }

  fetch("http://localhost:5000/nota", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nome, cpf, chave })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("respostaConsulta").style.display = "none";
    const res = document.getElementById("resultado");
    res.style.display = "block";
    res.innerText = `Compra de R$${data.valor_lido.toFixed(2)} registrada!\nCarimbos: ${data.dados.carimbos_atuais} / 10\nPratos: ${data.dados.pratos_ganhos}`;
    atualizarCartela(data.dados.carimbos_atuais);
  })
  .catch(error => {
    alert("Erro ao conectar com o servidor.");
    console.error(error);
  });
}

function atualizarCartela(carimbos) {
  const cartela = document.getElementById("cartela");
  cartela.innerHTML = "";
  for (let i = 0; i < 10; i++) {
    const c = document.createElement("div");
    c.className = "carimbo" + (i < carimbos ? " preenchido" : "");

    if (i < carimbos) {
      const img = document.createElement("img");
      img.src = "yaki.svg"; // caminho relativo
      img.alt = "Carimbo";
      img.style.width = "64px";
      img.style.height = "64px";
      c.appendChild(img);
    }

    cartela.appendChild(c);
  }
}

function consultarCarimbos() {
  const cpf = document.getElementById("cpf").value;

  if (!cpf) {
    alert("Digite um CPF para consultar.");
    return;
  }

  fetch(`http://localhost:5000/saldo/${cpf}`)
    .then(res => {
      if (!res.ok) {
        console.error("Status HTTP:", res.status);
        throw new Error("Resposta não OK");
      }
      return res.json();
    })
    .then(data => {
      document.getElementById("resultado").style.display = "none";
      const div = document.getElementById("respostaConsulta");
      div.style.display = "block";
      div.innerText = `CPF: ${data.cpf}\nCarimbos: ${data.carimbos}/10\nPratos: ${data.pratos}`;
      atualizarCartela(data.carimbos);
    })
    .catch(err => {
      console.error("Erro detalhado:", err);
      alert("Erro ao consultar carimbos.");
    });
}



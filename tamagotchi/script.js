var fome = 100;
var higiene = 100;
var sono = 100;
var diversao = 100;
var social = 100;
var idade = 0;

function Loop(time = 2) {
  var total = fome + higiene + sono + diversao + social;

  fome = fome - parseInt(time) * 1;
  higiene = higiene - parseInt(time) * 0.25;
  sono = sono - parseInt(time) * 1;
  diversao = diversao - parseInt(time) * 0.25;
  social = social - parseInt(time) * 0.3;
  idade = idade + parseInt(time) * 0.5;

  document.getElementById("fome").innerHTML = fome.toFixed(1) + "%";
  document.getElementById("higiene").innerHTML = higiene.toFixed(1) + "%";
  document.getElementById("sono").innerHTML = sono.toFixed(1) + "%";
  document.getElementById("diversao").innerHTML = diversao.toFixed(1) + "%";
  document.getElementById("social").innerHTML = social.toFixed(1) + "%";
  document.getElementById("idade").innerHTML = idade;

  if (
    fome <= 0 ||
    higiene <= 0 ||
    sono <= 0 ||
    diversao <= 0 ||
    social <= 0 ||
    idade >= 80
  ) {
    fome = 0;
    higiene = 0;
    sono = 0;
    diversao = 0;
    social = 0;
    idade = 0;
    document.getElementById("pet").src = "img/preto.jpg";
    document.getElementById("message").innerHTML = "Seu pet morreu";
  } else if (total > 400) {
    document.getElementById("pet").src = "img/azul.jpg";
  } else if (total > 300) {
    document.getElementById("pet").src = "img/amarelo.jpg";
  } else if (total > 200) {
    document.getElementById("pet").src = "img/vermelho.jpg";
  }
}

function Comer() {
  fome += 4;
}

function Banho() {
  higiene += 4;
}

function Dormir() {
  sono += 3;
}

function Brincar() {
  diversao += 2;
}

function Conversar() {
  social += 2;
}

function Start() {
  var temporizador = setInterval(Loop, 2000);
}

Start();

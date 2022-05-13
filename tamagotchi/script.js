var fome = 100;
var higiene = 100;
var sono = 100;
var diversao = 100;
var social = 100;
var idade = 0;

function Loop(time = 2) {
  fome = fome - parseInt(time) * 0.5;
  higiene = higiene - parseInt(time) * 0.25;
  sono = sono - parseInt(time) * 1;
  diversao = diversao - parseInt(time) * 0.25;
  social = social - parseInt(time) * 0.3;
  idade = idade + parseInt(time) * 0.5;

  document.getElementById("fome").innerHTML = fome + "%";
  document.getElementById("higiene").innerHTML = higiene.toFixed(1) + "%";
  document.getElementById("sono").innerHTML = sono.toFixed(1) + "%";
  document.getElementById("diversao").innerHTML = diversao.toFixed(1) + "%";
  document.getElementById("social").innerHTML = social.toFixed(1) + "%";
  document.getElementById("idade").innerHTML = idade;

  if (idade >= 5) {
    document.getElementById("pet").src = "img/rodrigo.png";
  } else if (idade >= 15) {
    document.getElementById("pet").src = "./img/oldrigo.jpeg";
  }

  if (
    fome == 0 ||
    higiene == 0 ||
    sono == 0 ||
    diversao == 0 ||
    social == 0 ||
    idade >= 80
  ) {
    alert("SEU BONEQUINHO MORREU.");
    document.location.reload(true);
  }
}

function Comer() {
  fome = fome + 10;
}

function Banho() {
  higiene = higiene + 10;
}

function Dormir() {
  sono = sono + 10;
}

function Brincar() {
  diversao = diversao + 5;
}

function Conversar() {
  social = social + 5;
}

function Start() {
  var temporizador = setInterval(Loop, 2000);
}

Start();

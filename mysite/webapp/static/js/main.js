
function select(elem) {
  if (elem.src === `http://${location.host}/static/img/free.png`) {
    elem.src = `http://${location.host}/static/img/selected.png`;
    input = document.getElementById('seat-input-box');
    if (input.value.length == 0) {
      input.value += elem.id;
    }
    else {
      input.value += `,${elem.id}`;
    }
  }
  else if (elem.src === `http://${location.host}/static/img/selected.png`)  {
    elem.src = `http://${location.host}/static/img/free.png`
    input.value = input.value.replace(`,${elem.id}`, "");
    input.value = input.value.replace(`${elem.id},`, "");
    input.value = input.value.replace(`${elem.id}`, "");
}}
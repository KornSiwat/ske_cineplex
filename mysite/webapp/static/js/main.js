
function select(elem) {
  if (elem.src === `http://${location.host}/static/img/free.png`) {
    elem.src = `http://${location.host}/static/img/selected.png`;
    let input = $('#seat-input-box');
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

function choose_time(elem) {
  let all_showtime = $(".showtime-button");
  for (let i = 0; i < all_showtime.length; i++) {
    all_showtime[i].className = 'showtime-button';
  }
  elem.className = "showtime-button chosen";
  showtime_form = $('#showtime-field');
  showtime_form.value = elem.id;
  let id = $('.booking-name')[0].id
  $.ajax({
    url: `/update/${id}/${elem.id}`,
    method: 'GET',
    data: {},
    success: function(data){
      $('#gonna-update').html(data);
    }, error: function(error){
      console.log(error)
      console.log("error")
    }
  })
  }

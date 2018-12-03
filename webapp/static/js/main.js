
const select = function(elem) {
  let input = $('#seat-input-box');
  if (elem.src === `http://${location.host}/static/img/free.png`) {
    elem.src = `http://${location.host}/static/img/selected.png`;
    // alert(input[0]);
    if (input[0].value.length == 0) {
      input[0].value += elem.id;
    }
    else {
      input[0].value += `,${elem.id}`;
    }
  }
  else if (elem.src === `http://${location.host}/static/img/selected.png`)  {
    elem.src = `http://${location.host}/static/img/free.png`
    input[0].value = input[0].value.replace(`,${elem.id}`, "");
    input[0].value = input[0].value.replace(`${elem.id},`, "");
    input[0].value = input[0].value.replace(`${elem.id}`, "");
}}

const choose_time = function(elem) {
  let all_showtime = $(".showtime-button");
  for (let i = 0; i < all_showtime.length; i++) {
    all_showtime[i].className = 'showtime-button';
  }
  elem.className = "showtime-button chosen";
  showtime_form = $('#showtime-field');
  showtime_form[0].value = elem.id;
  console.log(showtime_form[0].value )
  let id = $('.booking-name')[0].id;
  $.ajax({
    url: `/update/${id}/${elem.id}`,
    method: 'GET',
    data: {},
    success: function(data){
      $('#gonna-update').html(data);
    }, error: function(error){
      console.log(error);
      console.log("error");
    }
  })
  }


const add_card = function() {
  $('.list')[0].innerHTML += ("<div class='empty_card' ></div>");
}

const check_card = function() {
  let winWidth = (window.innerWidth - (0.1* window.innerWidth))
  for (let i = 0; i < 5; i++){
    $( ".empty_card" ).remove();
  }
  for (let i = 0; i < 5; i++){
    card = $('.card').length;
    if ((card % Math.floor(winWidth / 230)) > 0) {
      $('.list')[0].innerHTML += ("<div class='empty_card card' ></div>");
    }
  }
}
setTimeout(check_card, 50);

window.onresize = function() {
  check_card();
};


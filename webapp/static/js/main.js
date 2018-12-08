$( document ).ready(function() {

  $('.seat-icon-aval').click(function(){
    let elem = $(this);
    let movie_field = $('#movie-field');
    let movie_name = $('.booking-movie-name');
    movie_field[0].value = movie_name[0].id
    let date_field = $('#date-field');
    let today = $('.date');
    date_field[0].value = today[0].id
    let input = $('#seat-input-box');
    if (elem[0].src === `http://${location.host}/static/img/free.png`) {
      elem[0].src = `http://${location.host}/static/img/selected.png`;
      if (input[0].value.length == 0) {
        input[0].value += elem[0].id;
      }
      else {
        input[0].value += `,${elem[0].id}`;
      }
    }
    else if (elem[0].src === `http://${location.host}/static/img/selected.png`)  {
      elem[0].src = `http://${location.host}/static/img/free.png`
      input[0].value = input[0].value.replace(`,${elem[0].id}`, "");
      input[0].value = input[0].value.replace(`${elem[0].id},`, "");
      input[0].value = input[0].value.replace(`${elem[0].id}`, "");
  }});
});


const choose_time = function(elem) {
  let all_showtime = $(".showtime-button");
  for (let i = 0; i < all_showtime.length; i++) {
    all_showtime[i].className = 'showtime-button';
  }
  elem.className = "showtime-button chosen";
  showtime_form = $('#showtime-field');
  showtime_form[0].value = elem.id;
  let id = $('.booking-name')[0].id;
  $.ajax({
    url: `/update_seat/${id}/${elem.id}`,
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

const update_history = function() {
  let name = $('#history-name');
  let tel = $('#history-tel');
  $.ajax({
    url: `/update_history/${name[0].value}/${tel[0].value}`,
    method: 'GET',
    data: {},
    success: function(data){
      $('#history-update').html(data);
    }, error: function(error){
      console.log('error')
    }
  })
}

const check_card = function() {
  let card = $('.card');
  let winWidth = (window.innerWidth - (0.1* window.innerWidth));
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
setTimeout(check_card, 0);

window.onresize = function() {
  check_card();
};
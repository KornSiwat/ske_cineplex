$(window).ready( () => {
    let first_button = $('.chosen');
    console.log(first_button[0].id)
    showtime_form = $('#showtime-field');
    showtime_form[0].value = first_button[0].id;
    let id = $('.booking-name')[0].id;
    $.ajax({
      url: `/update_seat/${id}/${first_button[0].id}`,
      method: 'GET',
      data: {},
      success: (data) => {
        $('#gonna-update').html(data);
      }, error: (error) => {
        console.log(error);
        console.log("error");
      }
  });
});

const choose_time = (elem) => {
  let input = $('#seat-input-box');
  input[0].value = '';
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
    success: (data) => {
      $('#gonna-update').html(data);
    }, error: (error) => {
      console.log(error);
      console.log("error");
    }
  })
};

const select = (elem) => {
  let movie_field = $('#movie-field');
  let movie_name = $('.booking-movie-name');
  movie_field[0].value = movie_name[0].id
  let date_field = $('#date-field');
  let today = $('.date');
  date_field[0].value = today[0].id
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
}};

const update_history = () => {
  let name = $('#history-name');
  let tel = $('#history-tel');
  $.ajax({
    url: `/update_history/${name[0].value}/${tel[0].value}`,
    method: 'GET',
    data: {},
    success: (data) => {
      $('#history-update').html(data);
    }, error: (error) => {
      console.log('error');
    }
  })
};

const check_card = () => {
  let card = $('.card');
  let winWidth = (window.innerWidth - (0.1* window.innerWidth));
  if (winWidth > 765) {
    let card_width = 230;
  }
  else {
    let card_width = 170;
  }
  card = $('.card').length;
  $( ".empty_card" ).remove();
  card = $('.card').length;
  for (let i = 0; i < 5; i++){
    card = $('.card').length;
    if ((card % Math.floor(winWidth / card_width)) > 0) {
      $('.list')[0].innerHTML += ("<div class='empty_card card' ></div>");
    }
  }
}
setTimeout(check_card, 0);

window.onresize = () => {
  setTimeout(check_card, 100);
};
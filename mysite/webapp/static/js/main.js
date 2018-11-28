var emptyCells, i;

$('.list.with-empty-cells').each(function() {
  emptyCells = [];
  for (i = 0; i < $(this).find('.empty-theater_card').length; i++) {
    emptyCells.push($('<ul>', {
      class: 'empty-theater_card'
    }));
  }
  $(this).append(emptyCells);
});
//Script updates the text of the header element to red when user clicks on
//he tag DIV#red_header

$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});

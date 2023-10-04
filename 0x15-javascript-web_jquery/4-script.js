// JavaScript script that toggles the class of the <header> element

$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});

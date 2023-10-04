// JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr

$(function () {
  $.ajax({
    type: 'Get',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});

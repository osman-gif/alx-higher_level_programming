/* global $ */

$(function () {
  const $hello = $('DIV#hello');

  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'get',
    success: function (result) {
      $hello.text(result.hello);
    }
  });
});

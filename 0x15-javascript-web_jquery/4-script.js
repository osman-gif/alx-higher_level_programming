/* global $ */
function toggel () {
  $(document).ready(function () {
    const header = $('header.green');
    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else {
      header.removeClass('green');
      header.addClass('red');
    }
  });
}

$('#toggle_header').click(toggel);

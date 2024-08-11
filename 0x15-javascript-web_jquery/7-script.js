/* global $ */
const $name = $('DIV#character');
$.ajax({
  type: 'get',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (data) {
    $name.text(data.name);
  }
});

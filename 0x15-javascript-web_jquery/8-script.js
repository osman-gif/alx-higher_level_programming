/* global $ */
const $titels = $('UL#list_movies');
$.ajax({
  type: 'get',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (result) {
    $.each(result.results, function (i, data) {
      $titels.append('<li>' + data.title + '</li>');
      console.log(data.title);
    });
  }
});

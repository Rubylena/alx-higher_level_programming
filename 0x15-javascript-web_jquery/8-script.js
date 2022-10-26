// $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
//     $('ul#list_movies').append(...data.results.map(data => `<li>${data.title}<li>`))
// });
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
  });
});
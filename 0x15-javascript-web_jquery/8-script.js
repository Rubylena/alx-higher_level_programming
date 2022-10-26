$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
    $('ul#list_movies').append(...data.results.map(data => `<li>${data.title}<li>`))
});
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
            $("#list_movies").html(data.results.forEach(titulo => {
                $('ul#list_movies').append('<li>'+titulo.title+'</li>');
            }));
});

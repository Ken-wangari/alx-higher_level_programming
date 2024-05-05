$.get('https://swapi.co/api/films/?format=json', function(data) {
  const movieList = data.results.map(movie => `<li>${movie.title}</li>`).join('');
  $('#list_movies').append(movieList);
});


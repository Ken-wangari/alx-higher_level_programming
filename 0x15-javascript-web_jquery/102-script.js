$(function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  
  $('#btn_translate').on('click', function() {
    $.get(url + $.param({ lang: $('#language_code').val() }), function(data) {
      $('#hello').html(data.hello);
    });
  });
});


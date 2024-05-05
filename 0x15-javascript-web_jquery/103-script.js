$(document).ready(function() {
  $('#btn_translate').click(translate);
  $('#language_code').focus(function() {
    $(this).keydown(function(event) {
      if (event.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('#language_code').val() }), function(data) {
    $('#hello').html(data.hello);
  });
}


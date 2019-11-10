
// Global

var $form;
var $phrase;
var $button;
var $field;
var $wrapper;
var $translated;
var english;
var wookie;

// Animate print text
var showText = function ($target, message, index, interval, callback) {
  if (index < message.length) {
    $target.append(message[index++]);
    setTimeout(function () { showText($target, message, index, interval, callback); }, interval);
  } else {
    // Recurssion done
    callback();
  }
}

function checkInput() {
  if(english == '' && wookie != '') {
    clearTranslation()
  }
}


function clearTranslation(event) {
  $translated.text('');
  $field.removeClass('sleeping');
  $button.removeAttr('disabled');
}

function wakeUp(event) {
  $field.removeClass('sleeping');
  $button.removeAttr('disabled');
}
function goToSleep() {
  $button.attr('disabled');
  $field.addClass('sleeping');
  $phrase.val("");
  $phrase.attr('placeholder','');
  $wrapper.children().fadeOut('slow');
}
function toggleRoar() {
  $field.toggleClass('roaring');
  $field.removeClass('sleeping');
}

function translationComplete() {
  $field.removeClass('roaring');
  $phrase.attr('disabled');
  // clearTranslation();
}

// Ajax response function
function showTranslation(response) {

  $phrase.attr('placeholder', english);
  $phrase.attr('disabled');
  english = '';
  $phrase.val('');

  $span = $('<span>');
  $p = $('<p>').append($span);

  $wrapper.prepend($p);

  $wrapper.fadeIn(200).delay(500).queue(function(next) {
    toggleRoar();
    $phrase.attr('disabled')
    // $('#translated').text('');
    showText($span, response, 0, 150, translationComplete);
    next();
  });
}

function attemptTranslate(event) {
  event.preventDefault();

  english = $phrase.val();

  if(english === '') {
    goToSleep();
    return;
  }

  analytics.track('Translated');
  var url = $form.attr('action');
  var ajaxConfig = {
    method: 'POST',
    data: JSON.stringify({'english': english}),
    contentType : 'application/json'
  }

  // Send ajax request!
  $.ajax(url, ajaxConfig).then(showTranslation);
}


// ----- Doc Ready ------

$(function() {

  // Elements
  $form = $('#form');
  $translated = $('#translated');
  $field = $('#field');
  $button = $('#translate');
  $phrase = $('#phrase');
  $wrapper = $('#wrapper');
  url = $('#backendUrl').val();


  // Listeners
  $phrase.focus(wakeUp);
  $phrase.on('input', checkInput)
  $form.submit(attemptTranslate);

  // Initial state
  goToSleep();
});
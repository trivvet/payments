function initAddForm() {
  $('option').click(function(event) {
    var option = $(this);
    $('div.provider').show();
    $('#add_counter').removeAttr('disabled');
    $('#inputArrears').removeAttr('disabled');
    $('p.provider').hide();
    $('a.provider_site').hide();
    switch($(this).val()) {
	  case 'water':
	  case 'sewerage':
	    $('.water').show();
	    $('#inputProvider').val('Хмельницькводоканал');
	    $('#inputSiteProvider').val('water.km.ua');
	    break;
	  case 'electricity':
	    $('.electricity').show();
	    $('#inputProvider').val('Хмельницькобленерго');
	    $('#inputSiteProvider').val('oblenergo.km.ua/portal/');
	    break;
	  case 'gas':
		$('.gas').show();
		$('#inputProvider').val('Хмельницькгаз');
		$('#inputSiteProvider').val('km.104.ua/ua/');
		break;
      case 'waste':
        $('.waste').show()
        $('#inputProvider').val('Спецкомунтранс');
        $('#inputSiteProvider').val('skt.km.ua/');
        $('#add_counter').attr('disabled', 'true');
        break;
	  default:
	    $('div.provider').hide();
        $('#inputArrears').attr('disabled', 'true');
	    break;
	};
  });
  $('#add_counter').click(function(event) {
    var button = $(this);
    if ($('div.counter1').attr('hidden')) {
      $('div.counter1').removeAttr('hidden');
    } else if ($('div.counter2').attr('hidden')) {
      $('div.counter2').removeAttr('hidden');
      $('#delete_counter_1').attr('disabled', 'true'); 
    } else if ($('div.counter3').attr('hidden')) {
      $('div.counter3').removeAttr('hidden');
      $('#delete_counter_2').attr('disabled', 'true');
    } else if ($('div.counter4').attr('hidden')) {
      $('div.counter4').removeAttr('hidden');
      $('#delete_counter_3').attr('disabled', 'true'); 
      button.hide();
    };
  });
  $('#delete_counter_1').click(function(event) {
    $('div.counter1').attr('hidden', 'true');
  });
  $('#delete_counter_2').click(function(event) {
    $('div.counter2').attr('hidden', 'true');
    $('#delete_counter_1').removeAttr('disabled');
  });
  $('#delete_counter_3').click(function(event) {
    $('div.counter3').attr('hidden', 'true');
    $('#delete_counter_2').removeAttr('disabled');
  });
  $('#delete_counter_4').click(function(event) {
    $('div.counter4').attr('hidden', 'true');
    $('#delete_counter_3').removeAttr('disabled');
    $('#add_counter').show(); 
  });
}

function initEditForm() {
  $('input.counter_value').keyup(function(event) {
    if($(this).val() > $('#counter_before1').text()) {
      $('#arrears').text(Number(($(this).val()-$('#counter_before1').text()) * 0.45) + 
      Number($('#inputArrears').val()));
    };
  });
}

$(document).ready(function() {
  initAddForm();
  initEditForm();
})

function initAddForm() {
  $('option').click(function(event) {
    var option = $(this);
    $('div.provider').show();
    $('div.tariff').show();
    $('#add_counter').removeAttr('disabled');
    $('#inputArrears').removeAttr('disabled');
    $('p.provider').hide();
    $('p.tariff').hide();
    $('a.provider_site').hide();
    switch($(this).val()) { 
	  case 'water':
		$('.water').show();
	    $('#inputProvider').val('Хмельницькводоканал');
	    $('#inputSiteProvider').val('water.km.ua');
	    $('#inputTariff').val('4.25');
	    break;
	  case 'sewerage':
	    $('.sewerage').show();
	    $('#inputProvider').val('Хмельницькводоканал');
	    $('#inputSiteProvider').val('water.km.ua');
	    $('#inputTariff').val('4.13');
	    break;
	  case 'electricity':
	    $('.electricity').show();
	    $('#inputProvider').val('Хмельницькобленерго');
	    $('#inputSiteProvider').val('oblenergo.km.ua/portal/');
	    $('#inputTariff').val('0.456');
	    break;
	  case 'gas':
		$('.gas').show();
		$('#inputProvider').val('Хмельницькгаз');
		$('#inputSiteProvider').val('km.104.ua/ua/');
		$('#inputTariff').val('7.188');
		break;
      case 'waste':
        $('.waste').show()
        $('#inputProvider').val('Спецкомунтранс');
        $('#inputSiteProvider').val('skt.km.ua/');
        $('#add_counter').attr('disabled', 'true');
        $('#inputTariff').val('8.60');
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
    var current = $('#inputArrears').val();
    var account = parseFloat(current - Number(($(this).val()-$('#counter_before1').text()) 
      * 0.45)).toFixed(2);
    if($(this).val() > Number($('#counter_before1').text())) {
      $('#arrears').text(account + ' грн');
      if(account > 0) {
	    $('#arrears').css('color', 'green');
	  } else if (account < 0) {
	    $('#arrears').css('color', 'red');
	  } else if (current == 0) {
        $('#arrears').css('color', 'black');
      };
    } else if ($(this).val() == Number($('#counter_before1').text())) {
      $('#arrears').text(parseFloat(Number($('#inputArrears').val())).toFixed(2) + ' грн');
      if(account > 0) {
	    $('#arrears').css('color', 'green');
	  } else if (account < 0) {
	    $('#arrears').css('color', 'red');
	  } else if (current == 0) {
        $('#arrears').css('color', 'black');
      };
    };
  });
  $('input.counter_value').click(function(event) {
    var current = $('#inputArrears').val();
    var account = parseFloat(current - Number(($(this).val()-$('#counter_before1').text()) 
      * 0.45)).toFixed(2);
    if($(this).val() > Number($('#counter_before1').text())) {
      $('#arrears').text(account + ' грн');
      if(account > 0) {
	    $('#arrears').css('color', 'green');
	  } else if (account < 0) {
	    $('#arrears').css('color', 'red');
	  } else if (current == 0) {
        $('#arrears').css('color', 'black');
      };
    } else if ($(this).val() == Number($('#counter_before1').text())) {
      $('#arrears').text(parseFloat(Number($('#inputArrears').val())).toFixed(2) + ' грн');
      if(account > 0) {
	    $('#arrears').css('color', 'green');
	  } else if (account < 0) {
	    $('#arrears').css('color', 'red');
	  } else if (current == 0) {
        $('#arrears').css('color', 'black');
      };
    };
  });
}

$(document).ready(function() {
  initAddForm();
  initEditForm();
})

function initAddForm() {
  $('option').click(function(event) {
    var option = $(this);
    $('div.provider').removeAttr('hidden');
    $('p.provider').attr('hidden', 'true');
    $('a.provider_site').attr('hidden', 'true');
    switch($(this).val()) {
	  case 'water':
	  case 'sewerage':
	    $('.water').removeAttr('hidden');
	    $('#inputProvider').val('Хмельницькводоканал');
	    $('#inputSiteProvider').val('water.km.ua');
	    break;
	  case 'electricity':
	    $('.electricity').removeAttr('hidden');
	    $('#inputProvider').val('Хмельницькобленерго');
	    $('#inputSiteProvider').val('oblenergo.km.ua/portal/');
	    break;
	  case 'gas':
		$('.gas').removeAttr('hidden');
		$('#inputProvider').val('Хмельницькгаз');
		$('#inputSiteProvider').val('km.104.ua/ua/');
		break;
      case 'waste':
        $('.waste').removeAttr('hidden');
        $('#inputProvider').val('Спецкомунтранс');
        $('#inputSiteProvider').val('skt.km.ua/');
        break;
	  default:
	    $('div.provider').attr('hidden', 'true');
	    break;
	};
  });
}

$(document).ready(function() {
  initAddForm();
})

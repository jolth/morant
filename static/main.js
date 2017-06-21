$(document).ready( function() {
    //var _validFileExtensions = [".jpg", ".jpeg"];
    var reg = /\.(jpg|jpeg)/g;

    $.validate({
        modules : 'file'
    });

    $(document).on('change', '.btn-file :file', function() {
	    var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
            /*if (input[0].type == 'file') {
                if (!label.match(reg)) {
                    alert("No es un jpg/jpeg");
                    return; 
                }
            } else {
                return;
            }*/
		input.trigger('fileselect', [label]);
    });

    //Set file name
	$('.btn-file :file').on('fileselect', function(event, label) {
        var input = $(this).parents('.input-group').find(':text'),
		    log = label;
		    
		if( input.length ) {
		    input.val(log);
		} else {
		    if( log ) alert(log);
		}
	    
	});

    function isFormValid() {
        return $('#imgInp1').val() != "" && $('#imgInp2').val() != "" && $('#imgInp3').val() != "";
    }

    function toggleEnableContinue() {
        $('#btn_send').prop('disabled', !isFormValid());
    }

    $('#imgInp1, #imgInp2, #imgInp3').change(toggleEnableContinue);

});

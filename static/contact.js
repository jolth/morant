$(document).ready(function () {

    function isFormValid() {
        return $('#inputName').val() != '' && $('#inputEmail').val() != '' && $('#inputMessage').val() != '';
    }

    function toggleEnableContinue() {
        $('#btn_send').prop('disabled', !isFormValid());
    }

    $('#inputName, #inputEmail, #inputMessage').keyup(toggleEnableContinue);

    $('#form_contact').submit(function(event) {
        event.preventDefault();
        $(this).hide();

        var name = $('#inputName').val();
        var email = $('#inputEmail').val();
        var message = $('#inputMessage').val();

        $.post('/contact',
            {
                name: name,
                email: email,
                message: message
            },
            function(data, status){
                $('#message').html("<p>"+ data +"</p>").show();
            });
    });

});

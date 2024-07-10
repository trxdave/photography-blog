$(document).ready(function() {
    $('#email-signup-btn').click(function() {
        $('#email-signup').show();
        $('#social-signup').hide();
    });

    $('#social-signup-btn').click(function() {
        $('#email-signup').hide();
        $('#social-signup').show();
    });
});
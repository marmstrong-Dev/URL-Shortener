function regValidation() {
    if (document.getElementById('auth_message').innerHTML == 'New User') {
        pass1 = document.getElementById('password').value;
        pass2 = document.getElementById('cpassword').value;

        if (pass1.length < 1 || pass2.length < 1)
        { $('#errorMsg').show(); return false; }
        else if (pass1 != pass2)
        { $('#errorMsg').show(); return false; }
        else
        { return true; }
    }
    else
    { return true; }
}

$(document).ready(function(){
  	$('#errorMsg').hide();
 });
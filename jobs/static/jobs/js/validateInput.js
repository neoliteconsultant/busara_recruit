function validatePassword(formName) {
	 if (document.forms[formName]["password"].value !== 
		document.forms[formName]["confirm_password"].value) {
		alert("The passwords don't match.");
		document.forms[formName]["confirmPassword"].focus();
		return false;
	}
}

/* SHOW LOGIN MODAL WHEN SIGN IN CLICKED */
var login_modal = document.getElementById("login-modal");
var login_btn = document.getElementById("login-btn");

login_btn.onclick = function() {
    login_modal.style.display = "block";
}


/* MAIN LOGIN TO EMAIL LOGIN */
var login_email_modal = document.getElementById("login-email-modal");
var login_email_btn = document.getElementById("login-email-btn");

login_email_btn.onclick = function() {
    login_email_modal.style.display = "block";
    login_modal.style.display="none"
}


/* SHOW SIGN UP MODAL WHEN SIGN UP CLICKED */
var signup_modal = document.getElementById("signup-modal");
var signup_btn = document.getElementById("signup-btn");

signup_btn.onclick = function() {
    signup_modal.style.display = "block";
    login_email_modal.style.display = "none";
    login_modal.style.display="none"
}

/* SIGN UP TO EMAIL SIGN UP */
var signup_email_modal = document.getElementById("signup-email-modal");
var signup_email_btn = document.getElementById("signup-email-btn");

signup_email_btn.onclick = function() {
    signup_email_modal.style.display = "block";
    signup_modal.style.display = "none";
    login_email_modal.style.display = "none";
    login_modal.style.display="none"
}


/* CLOSE MODALS */
var close0 = document.getElementsByClassName("close")[0];
var close1 = document.getElementsByClassName("close")[1];
var close2 = document.getElementsByClassName("close")[2];
var close3 = document.getElementsByClassName("close")[3];

close0.onclick = function() {
    login_modal.style.display = "none";
    login_email_modal.style.display = "none";
    signup_modal.style.display = "none";
    signup_email_modal.style.display = "none";
}

close1.onclick = function() {
    login_modal.style.display = "none";
    login_email_modal.style.display = "none";
    signup_modal.style.display = "none";
    signup_email_modal.style.display = "none";
}

close2.onclick = function() {
    login_modal.style.display = "none";
    login_email_modal.style.display = "none";
    signup_modal.style.display = "none";
    signup_email_modal.style.display = "none";
}

close3.onclick = function() {
    login_modal.style.display = "none";
    login_email_modal.style.display = "none";
    signup_modal.style.display = "none";
    signup_email_modal.style.display = "none";
}

/* CLOSE MODALS WHEN WINDOW IS CLICKED */
window.onclick = function(event) {
    if (event.target == login_modal) {
        login_email_modal.style.display = "none";
        login_modal.style.display = "none";
        signup_modal.style.display = "none";
        signup_email_modal.style.display = "none";
    }
    if (event.target == login_email_modal) {
        login_email_modal.style.display = "none";
        login_modal.style.display = "none";
        signup_modal.style.display = "none";
        signup_email_modal.style.display = "none";
    }
    if (event.target == signup_modal) {
        login_email_modal.style.display = "none";
        login_modal.style.display = "none";
        signup_modal.style.display = "none";
        signup_email_modal.style.display = "none";
    }

    if (event.target == signup_email_modal) {
        login_email_modal.style.display = "none";
        login_modal.style.display = "none";
        signup_modal.style.display = "none";
        signup_email_modal.style.display = "none";
    }
}


/* BACK MODALS */
var back0 = document.getElementsByClassName("back")[0];
var back1 = document.getElementsByClassName("back")[1];

back0.onclick = function() {
    login_email_modal.style.display = "none";
    login_modal.style.display = "block";
}

back1.onclick = function() {
    signup_email_modal.style.display = "none";
    signup_modal.style.display = "block";
}
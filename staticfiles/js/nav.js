let mainNav = document.getElementById('mySidenav');
let navBarToggle = document.getElementById('js-navbar-toggle');
let closeBtn = document.getElementById('closebtn')

navBarToggle.addEventListener('click', function() {
    mainNav.classList.toggle('active', true);
});

closeBtn.addEventListener('click', function() {
    mainNav.classList.toggle('active', false);
});

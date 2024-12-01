// Show the confirm password field when the user starts typing in the first password field
document.addEventListener('DOMContentLoaded', function () {
    const password1 = document.getElementById('password1');
    const password2Container = document.getElementById('password2-container');

    if (password1) {
        password1.addEventListener('input', function () {
            if (password1.value.length > 0) {
                password2Container.style.display = 'block';
            } else {
                password2Container.style.display = 'none';
            }
        });
    }
});

// Show the confirm password field when the user starts typing in the first password field
document.addEventListener('DOMContentLoaded', function () {
    const password1 = document.getElementById('password1');
    const password2Container = document.getElementById('password2-container');

    // Show confirm password field if the first password field is already filled
    if (password1 && password1.value.length > 0) {
        password2Container.style.display = 'block';
    }

    if (password1) {
        password1.addEventListener('input', function () {
            if (password1.value.length > 0) {
                password2Container.style.display = 'block';
            } else {
                password2Container.style.display = 'none';
            }
        });
    }
});

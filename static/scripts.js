// script.js

document.addEventListener('DOMContentLoaded', function () {

    // Example of handling form submission for login
    const loginForm = document.querySelector('form[action="/login"]');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission

            const username = document.querySelector('#username').value;
            const password = document.querySelector('#password').value;

            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({
                    username: username,
                    password: password
                })
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/options';
                } else {
                    return response.text().then(text => {
                        showError(text);
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showError('An error occurred. Please try again.');
            });
        });
    }

    // Function to show error messages
    function showError(message) {
        let errorDiv = document.querySelector('.error');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error';
            document.querySelector('.container').prepend(errorDiv);
        }
        errorDiv.textContent = message;
    }

    // Example of handling form submission for appointment booking
    const appointmentForm = document.querySelector('form[action="/book"]');
    if (appointmentForm) {
        appointmentForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(appointmentForm);

            fetch('/book', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showSuccess(data.message);
                } else {
                    showError('Failed to book appointment.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showError('An error occurred. Please try again.');
            });
        });
    }

    // Function to show success messages
    function showSuccess(message) {
        let successDiv = document.querySelector('.success');
        if (!successDiv) {
            successDiv = document.createElement('div');
            successDiv.className = 'success';
            document.querySelector('.container').prepend(successDiv);
        }
        successDiv.textContent = message;
    }
});

const togglePassword = document.getElementById('togglePassword');
const passwordField = document.querySelector('input[type="password"]');

togglePassword.addEventListener('click', function () {
    
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    
    this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>'; 
});
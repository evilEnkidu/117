document.addEventListener('DOMContentLoaded', () => {
      const menuToggle = document.querySelector('.menu-toggle');
      const navLinks = document.querySelector('.nav-links');

      menuToggle.addEventListener('click', () => {
          // Toggle menu
          navLinks.classList.toggle('active');
          menuToggle.classList.toggle('active');
      });

      // Close mobile menu when a link is clicked
      document.querySelectorAll('.nav-links a').forEach(link => {
          link.addEventListener('click', () => {
              navLinks.classList.remove('active');
              menuToggle.classList.remove('active');
          });
      });
  });
// DOM Elements
const navbar = document.querySelector('.navbar');
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const navLinksItems = document.querySelectorAll('.nav-links a');
const sections = document.querySelectorAll('section');

// Mobile menu toggle
if (hamburger) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
    document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
  });
}

// Close mobile menu when clicking on a link
navLinksItems.forEach(link => {
  link.addEventListener('click', () => {
    if (navLinks.classList.contains('active')) {
      hamburger.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
    navbar.style.background = 'rgba(255, 255, 255, 0.98)';
    navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
  } else {
    navbar.classList.remove('scrolled');
    navbar.style.background = 'rgba(255, 255, 255, 0.95)';
    navbar.style.boxShadow = 'none';
  }
  
  // Update active section in navigation
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (window.scrollY >= sectionTop - 300) {
      current = section.getAttribute('id');
    }
  });

  navLinksItems.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href').slice(1) === current) {
      link.classList.add('active');
    }
  });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;
    
    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      window.scrollTo({
        top: targetElement.offsetTop - 80,
        behavior: 'smooth'
      });
    }
  });
});

// Animation on scroll
const animateOnScroll = () => {
  const elements = document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right, .timeline-item');
  
  elements.forEach(element => {
    const elementTop = element.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;
    
    if (elementTop < windowHeight - 100) {
      element.classList.add('animate');
    }
  });
};

// Initial setup when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Add scrolled class if page is not at top
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
    navbar.style.background = 'rgba(255, 255, 255, 0.98)';
  }
  
  // Add animation classes to elements with delay
  document.querySelectorAll('section, .timeline-item').forEach((element, index) => {
    element.classList.add('fade-in');
    element.style.animationDelay = `${index * 0.1}s`;
  });
  
  // Initial animation check
  animateOnScroll();
});

// Add loading animation
window.addEventListener('load', () => {
  document.body.classList.add('loaded');
});

// Event listeners for scroll and resize
window.addEventListener('scroll', animateOnScroll);
window.addEventListener('resize', animateOnScroll);
});

// Add animation on scroll
const animateOnScroll = () => {
  const elements = document.querySelectorAll('.skill-category, .project-card');
  
  elements.forEach(element => {
    const elementPosition = element.getBoundingClientRect().top;
    const screenPosition = window.innerHeight / 1.3;
    
    if (elementPosition < screenPosition) {
      element.style.opacity = '1';
      element.style.transform = 'translateY(0)';
    }
  });
};

// Set initial state for animation
document.addEventListener('DOMContentLoaded', () => {
  // Animate skills and projects on page load
  document.querySelectorAll('.skill-category, .project-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });
  
  // Initial check for elements in viewport
  animateOnScroll();
  
  // Set current year in footer
  document.querySelector('footer p:first-child').textContent = `© ${new Date().getFullYear()} Sanjana Gupta. All rights reserved.`;
});

// Check for elements in viewport on scroll
window.addEventListener('scroll', animateOnScroll);

// Form submission handling (example - you'll need to replace with your actual form handling)
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Add your form submission logic here
    alert('Thank you for your message! I will get back to you soon.');
    contactForm.reset();
  });
}

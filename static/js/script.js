document.addEventListener("DOMContentLoaded", function() {
  const elements = document.querySelectorAll('.fade-in-element');

  const handleScroll = () => {
    elements.forEach(element => {
      const rect = element.getBoundingClientRect();
      if (rect.top <= window.innerHeight && rect.bottom >= 0) {
        element.classList.add('visible');
      }
    });
  };

  window.addEventListener('scroll', handleScroll);
  handleScroll();
});

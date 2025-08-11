document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('homeButton');
  if (button) {
    button.addEventListener('click', () => {
      window.open('https://withseok.tistory.com/606', '_blank');
    });
  }
});

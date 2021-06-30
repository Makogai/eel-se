document.getElementById("snake").addEventListener(
    "click",
    () => {
      eel.snake();
    },
    false
  );
document.getElementById("pdfconvertor").addEventListener(
    "click",
    () => {
      eel.pdf();
    },
    false
  );
document.getElementById("image").addEventListener(
    "click",
    () => {
      eel.image();
    },
    false
  );
  
  
  tippy('#snake_hs', {
    content: 'Leaderboard',
    placement: 'top',
  });
  
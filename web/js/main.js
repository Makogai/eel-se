
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
  
  
  tippy('#snake_hs', {
    content: 'Leaderboard',
    placement: 'top',
  });
  
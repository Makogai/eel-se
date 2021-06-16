document.getElementById("snake").addEventListener(
    "click",
    () => {
      eel.snake();
    },
    false
  );
  
  
  tippy('#snake_hs', {
    content: 'Leaderboard',
    placement: 'top',
  });
  
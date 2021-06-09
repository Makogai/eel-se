document.getElementById("get_data").addEventListener(
  "click",
  () => {
    let link = document.querySelector("#username").value;
    let loader = $(".loader");
    loader.removeClass("invisivle");
    eel.get_shortened_url(link);
  },
  false
);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

eel.expose(shorten_link);
function shorten_link(data) {
    let loader = $(".loader");

  let result = $(".result");

  result.text(data.tinyurl);

  loader.addClass("invisivle");
}





  var input = document.getElementById("username");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("get_data").click();
  }
});
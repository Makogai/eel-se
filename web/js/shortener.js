document.getElementById("get_data").addEventListener(
  "click",
  () => {
    let link = document.querySelector("#link").value;
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

  let tinyurl = $("#tinyurl");
  let dagd = $("#dagd");
  let osdb = $("#osdb");
  let adfly = $("#adfly");

  tinyurl.val(data['tinyurl'])
  dagd.val(data['dagd'])
  osdb.val(data['osdb'])
  adfly.val(data['adfly'])

  loader.addClass("invisivle");
}





  var input = document.getElementById("link");

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
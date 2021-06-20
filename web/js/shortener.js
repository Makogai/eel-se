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


function kFormatter(num, digits = 2) {
  const lookup = [
    { value: 1, symbol: "" },
    { value: 1e3, symbol: "k" },
    { value: 1e6, symbol: "M" },
    { value: 1e9, symbol: "G" },
    { value: 1e12, symbol: "T" },
    { value: 1e15, symbol: "P" },
    { value: 1e18, symbol: "E" },
  ];
  const rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
  var item = lookup
    .slice()
    .reverse()
    .find(function (item) {
      return num >= item.value;
    });
  return (num / item.value).toFixed(digits).replace(rx, "$1") + item.symbol;
}


tippy('.check', {
    content: 'Verified',
    placement: 'right',
  });
tippy('.lock', {
    content: 'Private account',
    placement: 'right',
  });

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
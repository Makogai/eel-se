document.getElementById("get_data").addEventListener(
  "click",
  () => {
    let username = document.querySelector("#username").value;
    let loader = $(".loader");
    loader.removeClass("invisivle");
    eel.get_profile(username);
  },
  false
);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

eel.expose(instagram_show);
function instagram_show(data) {
    let loader = $(".loader");

  let img = $(".thumbnail");
  let username = $(".username");
  let full_name = $(".full_name");
  let followers = $(".followers");
  let following = $(".following");
  let bio = $(".bio");

  let is_verified = data.is_verified;

  $(".check")
    .removeClass(is_verified ? "hidden" : "")
    .addClass(is_verified ? "" : "hidden");

  console.log(data.profile_pic);
  username.text(data.username);
  full_name.text(data.full_name);
  bio.text(data.bio);
  followers.text(kFormatter(data.followers));
  following.text(kFormatter(data.following));

  img.attr("src", "data:image/png;base64, " + data.profile_pic);
  loader.addClass("invisivle");
}

const getBase64FromUrl = async (url) => {
  const data = await fetch(url, { mode: "no-cors" });
  const blob = await data.blob();
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.readAsDataURL(blob);
    reader.onloadend = () => {
      const base64data = reader.result;
      resolve(base64data);
    };
  });
};

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
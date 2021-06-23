document.getElementById("encrypt_as").addEventListener(
  "click",
  () => {
    let text = document.querySelector("#text_as").value;
    console.log(text);
    let loader = $(".loader");
    loader.removeClass("invisible");
    eel.encrypt_as(text);
  },
  false
);


eel.expose(encrypt_as_js);
function encrypt_as_js(data) {
  let loader = $(".loader");

  let result = $("#result_as");

  result.val(data)

  loader.addClass("invisivle");
}


document.getElementById("decrypt_as").addEventListener(
  "click",
  () => {
    let text = document.querySelector("#text_as").value;
    console.log(text);
    let loader = $(".loader");
    loader.removeClass("invisible");
    eel.decrypt_as(text);
  },
  false
);


eel.expose(decrypt_as_js);
function decrypt_as_js(data) {
  let loader = $(".loader");

  let result = $("#result_as");

  result.val(data)

  loader.addClass("invisivle");
}

// ALPHA MIXER
document.getElementById("encrypt_am").addEventListener(
  "click",
  () => {
    let text = document.querySelector("#text_am").value;
    let secret = document.querySelector("#secret_am").value;
    console.log(text);
    let loader = $(".loader");
    loader.removeClass("invisible");
    eel.encrypt_am(text,secret);
  },
  false
);


eel.expose(encrypt_am_js);
function encrypt_am_js(data) {
  let loader = $(".loader");

  let result = $("#result_am");

  result.val(data)

  loader.addClass("invisivle");
}
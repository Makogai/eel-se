$(document).ready(function(){
    let loader = $(".loader");
    loader.removeClass("invisivle");
    eel.snake_hs();
})

eel.expose(snake_fill_hs);
function snake_fill_hs(data) {
    let loader = $(".loader");

    let result = $(".fillable");

    for(let key in data){
        // console.log(data[key]['name']);
        score = '<li><mark>'+data[key]['name']+'</mark><small>'+data[key]['score']+'</small></li>';
        result.append(score);
    }

  loader.addClass("invisivle");
}
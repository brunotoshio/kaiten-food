totalFood = 0
$(document).ready(function() {
  // Start food trail

  setInterval(function() {
    if (totalFood >= 12) return;
    $.get('/put', function(resp) {
      data = $.parseJSON(resp);
      html = buildFood(data);
      $('.marquee .container').append(html);
      totalFood++;
    })
  }, 2000)


})

function addToBill(name, price) {

}

function buildFood(data) {
  html = "<div class='food'><img src='/static/foods/" + data.pic + "' />";
  html = html + "<div class='name'>" + data.name + "</div><div class='price'>" + data.price;
  html = html + "</div></div>";
  return html
}
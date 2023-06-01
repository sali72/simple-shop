
$(document).ready(function(){


$.ajax({
  url: "http://127.0.0.1:5000/v1/shop/products",
  type: "GET",
  dataType: "json",
  // data: {"action": "loadall", "id": id},
}).done(function (data) {
  console.log(data);
  let products = data
  let range = products.length-1
  let cloned = null
  for (let i = 0; i <= range; i++){
      cloned = $(".row:first-of-type").clone(true, true).appendTo(".table");
      $("td", cloned).text(products[i].name);
  };
  $(".row:first-of-type").remove();
  // var out = '<table>';
  // $.each(data, function (index) {
  //   out += '<tr><td>' + data[index].name + ': ' + data[index].count + '</td></tr>';
  // });
  // out += '</table>';
  // $(".list").html(out);
}).fail(function (error) {
  console.log("Error:");
  console.log(error);
});
});

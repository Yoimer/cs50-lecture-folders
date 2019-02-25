
document.addEventListener("DOMContentLoaded", () => {

  let buttons = document.querySelectorAll('.btn-secondary');
  buttons.forEach(button => {
    button.onclick = function() {

      let srsf = this.previousSibling.value;

      let request = new XMLHttpRequest;
      let data = new FormData();
      data.append("dish", this.dataset.dish);
      data.append("type", this.dataset.type);
      data.append("size", this.dataset.size);
      data.append("price", this.dataset.price);

      request.open('POST', '/added');
      request.setRequestHeader('X-CSRFToken', csrf);
      request.send(data);

      request.onload = () => {
        let data = JSON.parse(request.responseText);
        document.querySelector('#cart').src = "/static/orders/img/Shopping-Cart-icon-active.png";
      }
    }
  });
});

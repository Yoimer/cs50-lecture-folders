// THIS IS FOR CREATING A NEW DISPLAY NAME
document.addEventListener('DOMContentLoaded', () => {

  if (document.querySelector('#formDisplay')){

    document.querySelector('#formDisplay').onsubmit = () => {
      // Create a new AJAX request
      let request = new XMLHttpRequest();

      // Asign value to submit
      let name = document.querySelector('#name').value;
      let data = new FormData();
      data.append('name', name);

      // Open the the already created request and send
      request.open('POST', '/name');

      request.send(data)
      // Response
      request.onload = () => {
        let data = JSON.parse(request.responseText);
        if (data.success){
          document.querySelector('#form').style.display = 'none';
          let h = document.createElement('h3');
          h.innerHTML = 'Welcome ' + data.name + '!';
          document.querySelector('#user-data').dataset.username = data.name;
          document.querySelector('#DisplayName').append(h);
          document.querySelector('#channelContainer').style.display = '';
        }else{
          document.querySelector('#DisplayName').innerHTML = 'Humm!, Unfortunately there was an error.. Please try again';
        }
      }
      return false;
    }
  }
});

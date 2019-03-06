function AJAXRequest(address, crsf, dataToSend){
  let request = new XMLHttpRequest;
  let data = new FormData();

  if (dataToSend === undefined) {

  }else{
    for (let key in dataToSend){
      data.append(key, dataToSend[key])
    }
  }

  request.open('POST', address);
  request.setRequestHeader('X-CSRFToken', crsf);
  request.send(data);

  return new Promise(function(resolve, reject) {
    request.onload = () => {
      var data = JSON.parse(request.responseText);
      resolve(data);
    }
  });
};

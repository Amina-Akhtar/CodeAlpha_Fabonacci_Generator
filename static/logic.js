function generateFibonacci() {
  const fibType = document.getElementById('fibType').value;
  const numberInput = document.getElementById('numberInput').value;
  const resultDiv = document.getElementById('result');

  if (numberInput <= 0) {
    resultDiv.innerHTML = 'You have entered an invalid number.';
    return;
  }

  const formData = new FormData();
  formData.append('fibType', fibType);
  formData.append('numberInput', numberInput);

  fetch('/generate', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    resultDiv.innerHTML = data.result;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

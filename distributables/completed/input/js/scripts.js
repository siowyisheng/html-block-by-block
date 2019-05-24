function myFunction() {
  console.log('clicked the H1')
}

function setDiv() {
  let value = document.getElementById('input').value
  console.log(value)
  document.getElementById('container').innerHTML = value
}

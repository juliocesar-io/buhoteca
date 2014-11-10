

var options = {
  valueNames: [ 'titulo', 'born' ]
};

var userList = new List('users', options);


function show(shown, hidden) {

  document.getElementById(shown).style.display='block';
  document.getElementById(hidden).style.display='none';
  return false;
  
}
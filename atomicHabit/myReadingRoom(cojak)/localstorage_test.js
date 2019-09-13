// 초보자를 위한 바닐라 자바스크립트
// https://github.com/nomadcoders/js-basics/blob/master/todo.js

const toDoForm  = document.querySelector('.toDoForm'),
      toDoInput = toDoForm.querySelector('input'),
      toDoList  = document.querySelector('.toDoList');
const TODOS_LS = 'toDos';
const toDos = [];


function saveToDos() {
  localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}


function paintToDo(text) {
  const li = document.createElement('li');
  const span = document.createElement('span');
  const delBtn = document.createElement('button');
  const newId = toDos.length + 1;
  
  span.innerText = text;
  delBtn.innerText = 'DEL';

  li.appendChild(delBtn);
  li.appendChild(span);
  toDoList.appendChild(li);
  li.id = newId;

  const toDoObj = {
    id: newId,
    text: text
  };
  toDos.push(toDoObj);
  saveToDos();
}


function handleSubmit(event) {
  event.preventDefault();
  const currentValue = toDoInput.value;
  paintToDo(currentValue);
  toDoInput.value = '';
}


function loadToDos() {
  const loadedToDos = localStorage.getItem(TODOS_LS);
  if(loadedToDos !== null) {
    const parsedToDos  = JSON.parse(loadedToDos);
    console.log(parsedToDos);
  }
}


function init() {
  loadToDos();
  toDoForm.addEventListener('submit', handleSubmit);
}

init();

function submitOK() {
  if(bookName.value !== ''){
    if(confirm('정말 작성하시겠습니까?') === flase){
      event.preventDefault();
    }
  } else {
    alert('required book name ');
  }
}

bookNoteSubmitBtn.addEventListener('click', submitOK);
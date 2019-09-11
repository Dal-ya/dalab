window.onload = function() {
  const bookNoteSubmitBtn = document.getElementById('book_note_submit_btn');
  const bookName = document.getElementById('book_name');

  function submitOK() {
    if(bookName.value !== ''){
      if(confirm('정말 작성하시겠습니까?') === flase){
        event.preventDefault();
      }
    } else {
      alert('book name required');
    }
  }
  
  bookNoteSubmitBtn.addEventListener('click', submitOK);
};



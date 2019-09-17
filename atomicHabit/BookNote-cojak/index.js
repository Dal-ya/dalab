const bookForm = document.querySelector('.book_form');
const bookList = document.querySelector('.book_list');

const BOOK_NOTE_STORAGE = 'bookNoteStorage';
let bookNoteStorageArr = [];


function setBookNote() {
  localStorage.setItem(BOOK_NOTE_STORAGE, JSON.stringify(bookNoteStorageArr));
}


function writeBookNote(event) {
  const bookName = document.getElementById('book_name');
  const bookStatus = document.getElementById('book_status');
  const bookMemo = document.getElementById('book_memo');
  const bookDate = document.getElementById('book_date');
  const bookStatusOptionsIndex = bookStatus.options.selectedIndex;
  const bookStatusText = bookStatus.options[bookStatusOptionsIndex].text;
  
  if(bookName.value !== ''){
    if(confirm('정말 작성하시겠습니까?') === false){
      event.preventDefault();
    } else {
      const bookNoteValueObj = {
        id: bookNoteStorageArr.length + 1,
        bookNameValue: bookName.value,
        bookStatusTextValue: bookStatusText,
        bookMemoValue: bookMemo.value,
        bookDateValue: bookDate.value
      }
      bookNoteStorageArr.push(bookNoteValueObj);
      setBookNote(); 
    }
  } 
}


function viewBookNote() {
  const spanID = document.createElement('span');
  const spanBookName = document.createElement('span');
  const spanBookStatus = document.createElement('span');
  const spanBookMemo = document.createElement('span');
  const spanBookDate = document.createElement('span');
  
  let []

  spanID.className = 'cell col1';
  spanID.innerText = 'test';
  document.body.appendChild(spanID);
}


function getBookNote() {
  const getBookNote = localStorage.getItem(BOOK_NOTE_STORAGE);
  if(getBookNote !== null) {
    const parseGetBookNote  = JSON.parse(getBookNote);
    bookNoteStorageArr = parseGetBookNote;
  }
}


function init() {
  getBookNote();
  bookForm.addEventListener('submit', writeBookNote);
  viewBookNote();
}


init();







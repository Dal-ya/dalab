const bookForm = document.querySelector('.book_form');
const bookList = document.querySelector('.book_list');

const BOOK_NOTE_LIST_STORAGE = 'bookNoteListStorage';
let bookNoteListStorageArr = [];


function setBookNoteList() {
  localStorage.setItem(BOOK_NOTE_LIST_STORAGE, JSON.stringify(bookNoteListStorageArr));
}



function handleSubmit(event) {
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
      //event.preventDefault();
      const bookNoteValueObj = {
        id: bookNoteListStorageArr.length + 1,
        bookNameValue: bookName.value,
        bookStatusTextValue: bookStatusText,
        bookMemoValue: bookMemo.value,
        bookDateValue: bookDate.value
      }
      bookNoteListStorageArr.push(bookNoteValueObj);
      setBookNoteList(); 
    }
  } 
}


function viewList() {
  
}


function getBookNoteList() {
  const getBookNoteList = localStorage.getItem(BOOK_NOTE_LIST_STORAGE);
  if(getBookNoteList !== null) {
    const parseGetBookNoteList  = JSON.parse(getBookNoteList);
    bookNoteListStorageArr = parseGetBookNoteList;
  }
}


function init() {
  getBookNoteList();
  bookForm.addEventListener('submit', handleSubmit);
}


init();







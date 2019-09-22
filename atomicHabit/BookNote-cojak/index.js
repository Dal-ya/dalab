const bookForm = document.querySelector('.book_form');
const bookList = document.querySelector('.book_list');

const BOOK_NOTE_STORAGE = 'bookNoteStorage';
let bookNoteStorageArr = [];


function setBookNote() {
  localStorage.setItem(BOOK_NOTE_STORAGE, JSON.stringify(bookNoteStorageArr));
}


function getBookNote() {
  const getBookNote = localStorage.getItem(BOOK_NOTE_STORAGE);
  if(getBookNote !== null) {
    const parseGetBookNote  = JSON.parse(getBookNote);
    bookNoteStorageArr = parseGetBookNote;
  }
}


function writeBookNote(event) {
  const bookName = document.getElementById('book_name');
  const bookStatus = document.getElementById('book_status');
  const bookMemo = document.getElementById('book_memo');
  const bookDate = document.getElementById('book_date');
  
  // bookStatus 의 value가 아닌 text 가져오기.
  const bookStatusOptionsIndex = bookStatus.options.selectedIndex;
  const bookStatusText = bookStatus.options[bookStatusOptionsIndex].text;
  
  if(bookName.value !== ''){
    if(confirm('정말 작성하시겠습니까?') === false){
      event.preventDefault();
    } else {
      const bookNoteValueObj = {
        id: bookNoteStorageArr.length + 1,
        bookNameValue: bookName.value,
        bookStatusValue: bookStatusText,
        bookMemoValue: bookMemo.value,
        bookDateValue: bookDate.value
      }
      bookNoteStorageArr.push(bookNoteValueObj);
      setBookNote(); 
    }
  } 
}


function viewBookNote() {
  console.log(bookNoteStorageArr);
  
  bookNoteStorageArr.forEach(list => {
    const divRow = document.createElement('div');
    const spanID = document.createElement('span');
    const spanBookName = document.createElement('span');
    const spanBookStatus = document.createElement('span');
    const spanBookMemo = document.createElement('span');
    const spanBookDate = document.createElement('span');
    const delBtn = document.createElement('button');
    const updateBtn = document.createElement('button');

    divRow.className = 'row';
    spanID.className = 'cell col1';
    spanBookName.className = 'cell col2';
    spanBookStatus.className = 'cell col3';
    spanBookMemo.className = 'cell col4';
    spanBookDate.className = 'cell col5';

    divRow.id = list.id;

    spanID.innerText = list.id;
    spanBookName.innerText = list.bookNameValue;
    spanBookStatus.innerText = list.bookStatusValue;
    spanBookMemo.innerText = list.bookMemoValue;
    spanBookDate.innerText = list.bookDateValue;
    delBtn.innerText = '삭제';
    updateBtn.innerText = '수정'

    bookList.appendChild(divRow);
    divRow.appendChild(spanID);
    divRow.appendChild(spanBookName);
    divRow.appendChild(spanBookStatus);
    divRow.appendChild(spanBookMemo);
    divRow.appendChild(spanBookDate);
    divRow.appendChild(delBtn);
    divRow.appendChild(updateBtn);    

    delBtn.addEventListener('click', deleteList);
    updateBtn.addEventListener('click', updateBookNote);
  });
}


function updateBookNote() {
  location.href = '#open';
  const btn = event.target;
  const div = btn.parentNode;
  const divID = div.id;
  

  const updateCloseBtn = document.getElementById('update_close_btn');
  updateCloseBtn.addEventListener('click', () => location.href = '#close');

  // bookNoteStorageArr.forEach(obj => {
  //   if(obj.id === 2){
  //         bookNoteStorageArr[1].bookNameValue = 'hello';
  //     bookNoteStorageArr[1].bookStatusValue = '읽는중';
  //     }
  // });
  // setBookNote();
}


function deleteList(event) {
  if(confirm('정말 삭제하시겠습니까?') === false) {
    event.preventDefault();
  } else {
    const btn = event.target;
    const div = btn.parentNode;
    bookList.removeChild(div);
    const filterBookNote =  bookNoteStorageArr.filter(list => {
      return list.id !== parseInt(div.id);
    });
    bookNoteStorageArr = filterBookNote;
    setBookNote();
  }
}


function init() {
  getBookNote();
  viewBookNote();
  bookForm.addEventListener('submit', writeBookNote);
}


init();

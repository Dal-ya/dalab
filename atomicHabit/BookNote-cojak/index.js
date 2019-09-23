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
  const bookStatusText = bookStatus.options[bookStatusOptionsIndex].textContent;
  
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


function updateBookNote(event) {
  location.href = '#open';

  const btn = event.target;
  const div = btn.parentNode;

  const updateBookForm = document.querySelector('.update_book_form');
  const updateCloseBtn = document.getElementById('update_close_btn');
  const upBookID = document.getElementById('update_book_id');
  const upBookName = document.getElementById('update_book_name');
  const upBookStatus = document.getElementById('update_book_status');
  const upBookMemo = document.getElementById('update_book_memo');
  const upBookDate = document.getElementById('update_book_date');

  const statusObj = {
    완독: 'completion',
    읽는중: 'reding',
    다시읽기: 'rereading',
    대기: 'standby',
    발췌독: 'picking',
    훑어보기: 'skimming' 
  };

  let statusValue = '';
  for(let prop in statusObj) {
    if(prop === div.childNodes[2].textContent) {
      statusValue = statusObj[prop];
    }
  }

  upBookID.value = div.id;
  upBookName.value = div.childNodes[1].textContent;
  upBookStatus.value = statusValue;
  upBookMemo.value = div.childNodes[3].textContent;
  upBookDate.value = div.childNodes[4].textContent;

  updateCloseBtn.addEventListener('click', () => location.href = '#close');

  updateBookForm.addEventListener('submit', (event)=>{
    if(confirm('정말 수정하시겠습니까?') === false) {
      event.preventDefault();
    } else {
      const upBookStatusOptionsIndex = upBookStatus.options.selectedIndex;
      const upBookStatusText = upBookStatus.options[upBookStatusOptionsIndex].textContent;

      bookNoteStorageArr.forEach(list => {
        if(list.id === parseInt(div.id)) {
          list.bookNameValue = upBookName.value;
          list.bookStatusValue = upBookStatusText;
          list.booMemoValue = upBookMemo.value;
          list.bookDateValue = upBookDate.value;
        }
      });
      setBookNote();
      location.href = '#close';
    }
  });
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

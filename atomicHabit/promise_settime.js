// https://www.youtube.com/watch?v=CA5EDD4Hjz4

function setTimeoutPromise(sec) {
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve(new Date().toISOString());
    }, sec * 1000);
  });
}

setTimeoutPromise(1)
  .then((result)=>{
    console.log(1, result);
    return setTimeoutPromise(1);
  })
  .then((result)=>{
    console.log(2, result);
    return setTimeoutPromise(1);
  })
  .then((result)=>{
    console.log(3, result);
    return 'promise~@.@';
  })
  .then((result)=>{
    console.log(result);
  });

/*
1 '2019-09-08T15:26:41.036Z'
2 '2019-09-08T15:26:42.047Z'
3 '2019-09-08T15:26:43.053Z'
promise~@.@
*/





console.log('start', new Date().getSeconds());

setTimeout(function() {
  console.log('3sec', new Date().getSeconds());
}, 3000);

setTimeout(function() {
  console.log('1sec', new Date().getSeconds());
}, 1000);

setTimeout(function() {
  console.log('2sec', new Date().getSeconds());
}, 2000);

console.log('end', new Date().getSeconds());

/* 
ex)
start 4
end 4
1sec 5
2sec 6
3sec 7
*/




console.log('start', new Date().getSeconds());

setTimeout(function() {
  console.log('1sec', new Date().getSeconds());
  setTimeout(function() {
    console.log('2sec', new Date().getSeconds());
    setTimeout(function() {
      console.log('3sec', new Date().getSeconds());
    }, 3000);    
  }, 2000);
}, 1000);

console.log('end', new Date().getSeconds());
/*  
ex)
start 14
end 14
1sec 15
2sec 17
3sec 20
*/
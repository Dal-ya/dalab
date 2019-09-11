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


// callback 으로도 동기 가능.
setTimeout(function() {
  console.log('first', new Date().getSeconds());
  setTimeout(function() {
    console.log('second', new Date().getSeconds());
    setTimeout(function() {
      console.log('third', new Date().getSeconds());
    }, 3000);    
  }, 1000);
}, 1000);
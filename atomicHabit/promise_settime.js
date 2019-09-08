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
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
// https://www.zerocho.com/category/JavaScript/post/5acafb05f24445001b8d796d

const arr = [10, 20, 30, 40, 50];

// forEach
const newArr = [];
const resultForEach = arr.forEach(n => {
  return newArr.push(n*10);
});

console.log(newArr); // [ 100, 200, 300, 400, 500 ]


// reduce
const reduceResultOne = arr.reduce(function(acc, cur, idx) {
	console.log(`acc: ${acc}, cur: ${cur}, idx: ${idx}`);
	return acc + cur;
}, 0);

console.log(reduceResultOne);
/* 
acc: 0, cur: 10, idx: 0
acc: 10, cur: 20, idx: 1
acc: 30, cur: 30, idx: 2
acc: 60, cur: 40, idx: 3
acc: 100, cur: 50, idx: 4
150
*/


const reduceResultTwo = arr.reduce((acc, cur, idx) => {
   acc.push(cur * 2);
   return acc;
}, []);

console.log(reduceResultTwo);
// [ 20, 40, 60, 80, 100 ]

// acc.push > [...acc, newElement]
let newElement = 0;
const arr2 = arr.reduce((acc, cur) => {
  newElement = cur * 2;
  return [...acc, newElement];
}, []);

console.log(arr2); 
// [ 20, 40, 60, 80, 100 ]


const resultReduceRight = arr.reduceRight((acc, cur, idx) => {
	console.log(`acc: ${acc}, cur: ${cur}, idx: ${idx}`);
	return acc + cur;
}, 0);

console.log(resultReduceRight);
/*
acc: 0, cur: 50, idx: 4
acc: 50, cur: 40, idx: 3
acc: 90, cur: 30, idx: 2
acc: 120, cur: 20, idx: 1
acc: 140, cur: 10, idx: 0
150
*/


const reducer = (acc, cur) => acc - cur;
const reducerResult = arr.reduce(reducer);

console.log(reducerResult);
// -130


const findMax = arr.reduce((acc, cur) => {
	if (cur > acc) {
		acc = cur;
	}
	return acc;
});

console.log('findMax: ', findMax);
// findMax:  50



// map
const mapResultOne = arr.map(function(element) {
	return element;
});

console.log(mapResultOne); // [ 10, 20, 30, 40, 50 ]
console.log(mapResultOne === arr);  // false


const mapResultTwo = arr.map(element => {
	return element * 2;
});

console.log(mapResultTwo);
// [ 20, 40, 60, 80, 100 ]



//filter
const filterResult = arr.filter(element => {
	return element > 20;
});

console.log(filterResult)
// [ 30, 40, 50 ]

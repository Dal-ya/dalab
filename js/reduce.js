// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
// https://www.zerocho.com/category/JavaScript/post/5acafb05f24445001b8d796d

const arr = [10, 20, 30, 40, 50];


// reduce
const reduceResultOne = arr.reduce(function(acc, cur, idx) {
	console.log(`acc: ${acc}, cur: ${cur}, idx: ${idx}`);
	return acc + cur;
}, 0);

console.log(reduceResultOne);


const reduceResultTwo = arr.reduce((acc, cur, idx) => {
   acc.push(cur * 2);
   return acc;
}, []);

console.log(reduceResultTwo);


const resultReduceRight = arr.reduceRight((acc, cur, idx) => {
	console.log(`acc: ${acc}, cur: ${cur}, idx: ${idx}`);
	return acc + cur;
}, 0);

console.log(resultReduceRight);


const reducer = (acc, cur) => acc - cur;
const reducerResult = arr.reduce(reducer);

console.log(reducerResult);


const findMax = arr.reduce((acc, cur) => {
	if (cur > acc) {
		acc = cur;
	}
	return acc;
});

console.log('findMax: ', findMax);


// map
const mapResultOne = arr.map(function(element) {
	return element;
});

console.log(mapResultOne);
console.log(mapResultOne === arr);  // false


const mapResultTwo = arr.map(element => {
	return element * 2;
});

console.log(mapResultTwo);


//filter
const filterResult = arr.filter(element => {
	return element > 20;
});

console.log(filterResult)

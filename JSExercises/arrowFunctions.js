//arrow Functions examples

//arrow funtions styles using map function

const names = ["Sumit", "Munish", "Manik"];

//arrow function style 1 - with paranthesis around argument name
const fullNames1 = names.map(name => {
  let x;
  name === "Munish" ? (x = `${name} Gupta`) : (x = `${name} Mahajan`);
  return x;
});

//arrow function style 2 - without paranthesis around argument name
const fullNames2 = names.map(name => {
  let x;
  name === "Munish" ? (x = `${name} Gupta`) : (x = `${name} Mahajan`);
  return x;
});

//arrow function style 3 - implicit return
const fullNames3 = names.map(name => `${name} Mahajan`);

//arrow function style 4 - with no arguments
const fullNames4 = names.map(() => `Mahajan`);

console.log(fullNames1);
console.log(fullNames2);
console.log(fullNames3);
console.log(fullNames4);

//Filter function example
const ages = [43, 23, 29, 18, 19, 49, 35];
let old = ages.filter(age => age > 20);
console.log(old);

//reduce function examples
const sample = [43, 23, 29, 18, 19, 49, 35];
let totalage = sample.reduce((sum, Element) => sum + Element);
console.log(totalage);

let dummyString = "magic";

function reverseString(dummyString) {
  let arr = dummyString.split("");
  arr.reverse();
  return arr.join("");
}
console.log(reverseString(dummyString));

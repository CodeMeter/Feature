var student = {
  name: "David Rayy",
  class: "VI",
  rollno: 12
};

function ObjectKeys(obj) {
  if (obj) {
    let arr = Object.keys(obj);
    arr.includes("exp") ? arr : arr.push("exp");
    return arr;
  }
}
const amendedArray = ObjectKeys(student);
console.log(amendedArray);

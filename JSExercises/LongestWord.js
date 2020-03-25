let dummyString = "magic is phenomanal work";

function longestWord(dummyString) {
  //console.log(dummyString);
  dummyString.trim();
  //console.log(dummyString);
  dummyString.replace(/[^a-zA-Zsd]/g, "");
  //console.log(dummyString);

  let arr = dummyString.split(" ");
  //console.log(arr);
  arr.sort(function(a, b) {
    console.log(a);
    console.log(b);
    console.log(arr);
    return b.length - a.length;
  });
  console.log(arr);
  return arr.shift();
  return dummyString;
}

console.log(longestWord(dummyString));

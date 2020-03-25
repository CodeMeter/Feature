/*
 * Programming Quiz: Umbrella (7-1)
 */

var umbrella = {
  color: "pink",
  isOpen: true,
  open: function() {
    if (umbrella.isOpen === true) {
      return "The umbrella is already opened!";
    } else {
      umbrella.isOpen = true;
      return "Julia opens the umbrella!";
    }
  },
  isClosed: function() {
    if (umbrella.isOpen === false) {
      return "The umbrella is already closed!";
    } else {
      umbrella.isOpen = false;
      return "Julia closed the umbrella!";
    }
  }
  // your code goes here
};

console.log(umbrella.isClosed());
console.log(umbrella.isOpen);

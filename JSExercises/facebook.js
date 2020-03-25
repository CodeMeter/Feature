var facebookProfile = {
  name: "Sumit Mahajan",
  friends: 500,
  messages: ["Hi,whatsup", "Birthday Night Celebrations", "Great News"],
  addFriend: function() {
    facebookProfile.friends++;
  },
  removeFriend: function() {
    facebookProfile.friends--;
  },
  postMessage: function(message) {
    message ? facebookProfile.messages.push(message) : console.log("hi");
  },
  deleteMessage: function(message) {
    if (message) {
      var index = facebookProfile.messages.indexOf(message);
      if (index !== -1) {
        console.log(index);
        facebookProfile.messages.splice(index, 1);
      }
    }
  }
};

facebookProfile.addFriend();
console.log(facebookProfile.friends);
facebookProfile.removeFriend();
console.log(facebookProfile.friends);
facebookProfile.postMessage("");
console.log(facebookProfile.messages);
facebookProfile.deleteMessage("Great News");
console.log(facebookProfile.messages);

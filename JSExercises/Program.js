function calculateVideoTime(element, videoDesc) {
  return Array.from(document.getElementsByTagName(element))
    .filter(newlist => newlist.innerText === videoDesc)
    .map(item => item.dataset.time.split(":"))
    .map(timecode => parseInt(timecode[0] * 60) + parseInt(timecode[1]))
    .reduce((a, b) => a + b);
}

const reduxTime = calculateVideoTime("li", "Redux Videos");
const flexTime = calculateVideoTime("li", "Flex Videos");

console.log(`redux time of videos are ${reduxTime}`);
console.log(`flex time of videos are ${flexTime}`);

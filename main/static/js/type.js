async function typeSentence(sentence, eleRef, delay = 200) {
  const letters = sentence.split("");
  let i = 0;
  while (i < letters.length) {
    await waitForMs(delay);
    $(eleRef).append(letters[i]);
    i++;
  }
  return;
}

function waitForMs(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function deleteSentence(eleRef) {
  const sentence = $(eleRef).html();
  const letters = sentence.split("");
  let i = 0;
  while (letters.length > 0) {
    await waitForMs(100);
    letters.pop();
    $(eleRef).html(letters.join(""));
  }
}

const carouselText = [" Reliability' ", " Integrity' ", " Punctuality' "];

async function carousel(carouselList, eleRef) {
  var i = 0;
  while (true) {
    await typeSentence(carouselList[i], eleRef);
    await waitForMs(500);
    await deleteSentence(eleRef);
    await waitForMs(100);
    i++;
    if (i >= carouselList.length) {
      i = 0;
    }
  }
}

carousel(carouselText, "#sentence");

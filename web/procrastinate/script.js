let phrases = [
    { text: 'send a funny gif to a friend', image: 'https://code.s3.yandex.net/web-code/procrastinate/1.gif' },
    { text: 'look up airfare discounts', image: 'https://code.s3.yandex.net/web-code/procrastinate/2.png' },
    { text: 'figure out what rappers are singing about', image: 'https://code.s3.yandex.net/web-code/procrastinate/3.png' },
    { text: 'learn something new on TED', image: 'https://code.s3.yandex.net/web-code/procrastinate/4.png' },
    { text: 'arrange books on a shelf by color', image: 'https://code.s3.yandex.net/web-code/procrastinate/5.png' },
    { text: 'read about San Francisco wages', image: 'https://code.s3.yandex.net/web-code/procrastinate/6.png' },
    { text: 'to read the news and be horrified at the comments', image: 'https://code.s3.yandex.net/web-code/procrastinate/7.png' },
    { text: 'get into a stream of sad songs and remember all the mistakes of my youth', image: 'https://code.s3.yandex.net/web-code/procrastinate/8.png' },
    { text: 'watch the trailer of the show and the first season along the way', image: 'https://code.s3.yandex.net/web-code/procrastinate/9.png' },
    { text: 'check the unread in Telegram channels', image: 'https://code.s3.yandex.net/web-code/procrastinate/10.png' }
];

function getRandomElement(arr) {
    let randIndex = Math.floor(Math.random() * arr.length);
    return arr[randIndex];
}

let button = document.querySelector('.button');
let phrase = document.querySelector('.phrase');
let advice = document.querySelector('.advice');
let image = document.querySelector('.image');

button.addEventListener('click', function () {
  let randomElement = getRandomElement(phrases);
  smoothly(phrase, 'textContent', randomElement.text);
  smoothly(image, 'src', randomElement.image);

  if (randomElement.text.length > 40) {
    advice.style.fontSize = '33px';
  } else {
    advice.style.fontSize = '42px';
  }
});

for (let i = 0; i < 3; i = i + 1) {
    smoothly(phrase, 'textContent', phrases[i].text)
    smoothly(image, 'src', phrases[i].image)
  }
var arrayOfQuotes = [
    {
        "author":"Jim Rohn",
        "quote":"Beware of what you become in pursuit of what you want."
    },
    {
        "author":"Epictetus",
        "quote":"It's not what happen to you, but how you react to it that matters."
    }
]

function randomSelector(arrayLength) {
    return Math.floor(Math.random() * arrayLength);
}

function generateQuote() {
    var randomNUmber = randomSelector(arrayOfQuotes.length);

    document.getElementById("quoteOutput").innerHTML = '"' + arrayOfQuotes[randomNUmber].quote + '"';

    document.getElementById("authorOutput").innerHTML = "- " + arrayOfQuotes[randomNUmber].author;
}
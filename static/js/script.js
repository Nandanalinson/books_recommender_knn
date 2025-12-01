function getRecommendations() {
    const bookName = document.getElementById("userBook").value;
    const list = document.getElementById("results");

    // 🔹 Show "Searching..." immediately
    list.innerHTML = "<li>Searching...</li>";

    fetch("/get_similar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({book_name: bookName})
    })
    .then(res => res.json())
    .then(data => {

        list.innerHTML = "";

        if (data.error) {
            list.innerHTML = "<li>No book found.</li>";
            return;
        }

        if (data.recommendations.length === 0) {
            list.innerHTML = "<li>No similar books.</li>";
            return;
        }

        data.recommendations.forEach(book => {
            const item = document.createElement("li");
            item.textContent = `${book.title} by ${book.author}`;
            list.appendChild(item);
        });

    })
    .catch(err => {
        list.innerHTML = "<li>Error connecting to server.</li>";
    });
}

function getRecommendations() {
    const bookName = document.getElementById("userBook").value;
    console.log("Book:", bookName);

    fetch("/get_similar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ book_name: bookName })
    })
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("results");
        list.innerHTML = "";

        if (data.error) {
            list.innerHTML = "<li>No book found.</li>";
            return;
        }

        data.recommendations.forEach(book => {
            const item = document.createElement("li");
            item.textContent = `${book["Book-Title"]} by ${book["Book-Author"]}`;
            list.appendChild(item);
        });
    })
    .catch(err => {
        console.log("ERR:", err);
        document.getElementById("results").innerHTML = "<li>Error connecting to server.</li>";
    });
}

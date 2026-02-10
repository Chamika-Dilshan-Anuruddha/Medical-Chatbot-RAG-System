function sendData() {

    let userQuery = document.getElementById("query").value; 
    let MessageBodyElement = document.getElementById("message-body");

    MessageBodyElement.innerHTML += `<p class="user-query" id="user-query-text">${userQuery}</p>`;


    fetch("http://127.0.0.1:8000/get_results" , {
        method: "POST",
        body: JSON.stringify({
            query:userQuery
        }),
        headers: {
            "Content-type":"application/json; charset=UTF-8"
        }
    })
    .then((response) => response.json())
    .then((data)=> {
         MessageBodyElement.innerHTML += `<p id="user-results-text">${marked.parse(data["results"])}</p>`;
    })
}
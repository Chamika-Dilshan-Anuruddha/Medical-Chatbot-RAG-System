function sendData() {

    let userQueryElement = document.getElementById("query"); 
    let MessageBodyElement = document.getElementById("message-body");
    let userQuery = userQueryElement.value
    userQueryElement.value = "";

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


function clearChat(){
    let MessageBodyElement = document.getElementById("message-body");
    let userQuery = document.getElementById("query");
    MessageBodyElement.innerHTML = "";
    userQuery.value = "";
}
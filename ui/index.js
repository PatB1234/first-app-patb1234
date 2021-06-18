
function getTodos() {
    var todos = document.getElementById('todos');
    axios.get('/todo')
        .then(function (response) {
            console.log(response);
            todos.innerHTML = response.data.map(e => {
                return `<li><input type="checkbox" ${e.status ? "checked" : ""}>${e.item}</li>`
            }).join("\n");

        })
        .catch(function (error) {
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}
function addItem(event) {
    if (event.keyCode == 13) {
        axios.post('/todo', { 'item': newTodo.value })
            .then(function (response) {
                newTodo.value = "";
            })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
                // always executed
            });
        getTodos();
    }
}
function getMessage(){
    var requeteAjax = new XMLHttpRequest();
    requeteAjax.open("GET" , "chat_api.php") ;
    requeteAjax.onload = function(){
        var resultat =  JSON.parse(requeteAjax.responseText) ;
        var html = resultat.map(function(message){
        return `
        <div class="outgoing_msg">
        <div class="sent_msg">
            <p>${message.message}</p>
            <span class="time_date">${message.create_at} | Today</span> 
        </div>
        </div>
            `
        }).join('');
        var messages = document.getElementById('message_field'); 
        messages.innerHTML = html; 
    }
    requeteAjax.send() ;
}

function postMessage(e){
    e.preventDefault();

    var author = document.querySelector('#user') ;
    var content = document.querySelector('#message') ;

    var data = new FormData();
    data.append('author', author.value);
    data.append('message', content.value);

    var requeteAjax = new XMLHttpRequest();
    requeteAjax.open("POST", 'chat_api.php?task=write');
    requeteAjax.onload = function(){
        message.value = '';
        content.focus() ;
        getMessage();
    }
    requeteAjax.send(data);
}
document.querySelector('form').addEventListener('submit', postMessage);
var interval = window.setInterval(getMessage, 1000) ;

getMessage(); 




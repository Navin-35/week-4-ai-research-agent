const chatBox = document.getElementById("chat-box");

async function sendMessage(){

    const input=document.getElementById("message");

    const message=input.value.trim();

    if(message==="") return;

    chatBox.innerHTML+=`
    <div class="user">

    <b>You</b><br>

    ${message}

    </div>
    `;

    input.value="";

    chatBox.scrollTop=chatBox.scrollHeight;

    chatBox.innerHTML+=`
    <div id="loading" class="bot">

    Researching...

    </div>
    `;

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            message

        })

    });

    const data=await response.json();

    document.getElementById("loading").remove();

    chatBox.innerHTML+=`
    <div class="bot">

    <b>Research Agent</b><br>

    ${data.answer}

    </div>
    `;

    chatBox.scrollTop=chatBox.scrollHeight;

}


async function clearChat(){

    await fetch("/clear",{

        method:"POST"

    });

    chatBox.innerHTML="";

}


document.getElementById("message")
.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});
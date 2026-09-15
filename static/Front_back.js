//User Register//
document.addEventListener('DOMContentLoaded', ()=> {
    const loginBtn = document.getElementById("RegisterBtn")
    if(loginBtn){
        console.log("found")
        loginBtn.addEventListener('click' , () =>{
            Is_Equal();
            RegisterUser();
        })
    }
    else{
        console.error("Could not find button")
    }
})
equal_Register = false
document.getElementById('RegisterBtn').addEventListener('click' , () =>{
    Is_Equal();
    RegisterUser();
});
function Is_Equal(){
    if(document.getElementById("Password1").value == document.getElementById("Password2").value){
        equal_Register = true
    } else{
        console.error("Passwords Arent the same")
    }
};
async function RegisterUser(){
    const username  = document.getElementById("UserName-register").value;
    const password = document.getElementById("Password1").value;
    if(!username || !password){
        console.error("No Inputs");
    }
    else if (equal_Register){
        url = "http://127.0.0.1:8000";
        const response = await fetch(url + "/api/user-action" , {method: 'POST', headers:{'Contest-Type': 'application.json'}, bpdy: JSON.stringify({action: 'register' , UserName: username, Password: password})});
        const result = await response.json();
        if (result["Sucess"]){
            alert("yay");
        }
        else{
            alert("nay");
        }

    }
    else{
        console.error("Could not Register User");
    }
};

//User Login//

document.addEventListener('DOMContentLoaded', ()=> {
    const loginBtn = document.getElementById("Login")
    if(loginBtn){
        console.log("found")
        loginBtn.addEventListener('click' , login)
    }
    else{
        console.error("Could not find button")
    }
})
async function login(event){
    if (event) event.preventDefault();
    console.log("button pressed");
    const username = document.getElementById("UserName").value;
    const password = document.getElementById("Password").value;
    if (!username || !password){
        console.error("No Input")
    }
    url = "http://127.0.0.1:8000";
    const response = await fetch(url + "/api/user-action" , {method: 'POST', headers:{'Content-Type': 'application/json'}, body: JSON.stringify({action: 'login' , UserName: username , Password: password})});
    const result = await response.json();
    if(result["Sucess"]){
        window.location.replace(url + "/Account.html");
    }
    else{
        alert("nay");
    }
};
//Index(Home) Page//

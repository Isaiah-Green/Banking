
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
        console.error("Could not find button");
    }
})
equal_Register = false;
function Is_Equal(){
    if(document.getElementById("Password1").value == document.getElementById("Password2").value){
        equal_Register = true;
    } else{
        console.error("Passwords Arent the same");
    }
};
async function RegisterUser(event){
    if (event) event.preventDefault();
    const username  = document.getElementById("UserName-register").value;
    const password = document.getElementById("Password1").value;
    if(!username || !password){
        console.error("No Inputs");
        return;
    }
    if (equal_Register){
        url = "http://127.0.0.1:8000";
        const response = await fetch(url + "/api/user-action" , {method: 'POST', headers:{'Content-Type': 'application/json'}, body: JSON.stringify({action: 'register' , UserName: username, Password: password})});
        const result = await response.json();
        if(result["Sucess"]){
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

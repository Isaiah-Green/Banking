//User Register//
/*
document.getElementById('RegisterBtn').addEventListener('click' , Is_Equal);
function Is_Equal(){
    if(document.getElementById("Password1").value == document.getElementById("Password2").value){
        return true
    } else{
        return false
    }
}
    */
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
    console.log(result);
    if(result["Sucess"]){
        alert("Yay");
    }
    else{
        alert("nay");
    }
};
//Index(Home) Page//

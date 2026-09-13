//User Register//
document.getElementById('RegisterBtn').addEventListener('click' , Is_Equal);
function Is_Equal(){
    if(document.getElementById("Password1").value == document.getElementById("Password2").value){
        return true
    } else{
        return false
    }
}
//User Login//
document.getElementById("Login").addEventListener('click' , login);
function login(){
    
}
//Index(Home) Page//

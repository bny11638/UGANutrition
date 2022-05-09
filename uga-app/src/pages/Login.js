import React from "react";
import "../styles/welcome.css"
import { Link } from "react-router-dom";
import BounceTitle from "./components/BounceTitle";
import { useState } from "react";
import { useLocation } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { useDispatch } from 'react-redux'
import { login } from '../redux-slices/UserSlice';



function Login() {
    // react-redux functions
    const dispatch = useDispatch();
    // react-router functions
    const location = useLocation();
    const navigate = useNavigate();
    // react state function
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [falseLogin, setFalseLogin] = useState(false);
    // onClick functions
    const loginButton = () => {
        // api fetch logic.
        fetch(process.env.REACT_APP_BACKEND_URL + "/login", {method: 'POST', headers: { 'Content-Type': 'application/json'}, body: JSON.stringify({name: email, password: password})})
        .then((res) => res.json())
        .then( (result) => {
            if (result.pid !== -1) { 
                dispatch(login({pid: result.pid, email: result.name, password: result.password}));
                navigate("/dashboard");
            } else { 
                setFalseLogin(true);
            }
        })
    }


    const switchText = location.pathname === "/register" ? "Click here to login" : "Click here to register";
    const switchURL = location.pathname === "/register" ? "/login" : "/register";
    return (
    <div style={{
      justifyContent: 'center',
      display: 'flex',
      margin: 'auto',
      marginTop: '75px'
    }}>
        <div style={{
            marginTop: '165px',
            marginLeft: '40px'
        }}>
            <BounceTitle/>
        </div>
        <div class="verticalForm" style={{marginLeft: '85px'}}>
            <h1 class="vFormLabel"> Lets get back to business. </h1>
            {falseLogin && <p>Email and Password combination not found please try again.</p>}
            <h1 class="vFormHead">Email</h1>
            <input type="text" class="textInput" value ={email} onChange={(event) => setEmail(event.target.value)}/>
            <h1 class="vFormHead">Password</h1>
            <input type="text" class="textInput" value ={password} onChange={(event) => setPassword(event.target.value)}/>
            <div style={{marginTop: '35px'}}>
                <div class="bg1">
                    <button type="button" id="butt2" onClick={ () => {navigate("/")}}>Back</button>
                </div>
                <div class="fg">
                    <button type="button" id="butt2" onClick={loginButton}>{location.pathname === "/register" ? "Register" : "Login"}</button>
                </div>
            </div>
            <Link to={switchURL} style={{textAlign: 'center', marginTop: '15px', marginRight: '25px', color: "white", fontFamily: 'Marvel'}}>{switchText}</Link>
        </div>
    </div>);
}
export default Login;
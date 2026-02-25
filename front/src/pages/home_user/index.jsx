import { use, useEffect } from "react";
import axios from "axios";

export default function HomeUser(){

    const token = localStorage.getItem('token')
    const listar = async ()=>{
        const response = await axios.get('Http://localhost:8000/api/usuarios/')
        console.log("listar usuarios: ", response.data);

    }

    useEffect(()=>{listar()}, [])
    return(
        <div>
            <p> Essa é a página HOME USER </p>
            <div style={{width: "100%"}}> Token: {token} </div>
        </div>
    )
}
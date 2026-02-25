import React, { useEffect, useState } from "react"
import axios from "axios"
 
export default function HomeUser() {
    const [user, setUser] = useState([])
    const [search, setSearch] = useState("")
 
    const token = localStorage.getItem('token')
 
    const listar = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` }
            })
            setUser(response.data)
        } catch (error) {
            console.log(error);
        }
    }
 
    useEffect(() => { listar() }, [])
 
    const usuariosFiltrados = user.filter((u) =>
        u.nome.toLowerCase().includes(search.toLowerCase())
    )
 
    return (
        <div>
            <h2>Lista de Usuários</h2>
 
            <input
                type="text"
                placeholder="Pesquisar usuário..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                style={{
                    marginBottom: "15px",
                    padding: "8px",
                    width: "250px"
                }}
            />
 
            <table border="1" cellPadding="6" style={{ width: "100%" }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {usuariosFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
 
            <hr style={{ margin: "20px 0" }} />
        </div>
    )
}
 
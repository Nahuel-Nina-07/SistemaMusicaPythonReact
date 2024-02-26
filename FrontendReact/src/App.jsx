import { useState,useEffect } from 'react'

function UsersItems({username,email,password,id_role}){
  return(
    <article className='w-96 bg-gray-100 rounded-xl shadow-lg shadow-gray-700 mx-auto mt-10 p-5'>
      <h3 className='text-center text-2xl mb-5'>{username}</h3>
      <p>Email:{email}</p>
      <p>Password:{password}</p>
      <p>ID:{id_role}</p>
      <div className='flex justify-center my-5 '>
        <button className='bg-red-700 text-gray-700 w-32 font-semibold rounded-xl h-10 hover:bg-red-900 hover:text-gray-200'>Eliminar</button>
      </div>
    </article>
  )
}

function App() {

  const [users, setUsers] = useState([])
  const getUsers = async () => {
    const allusers = await fetch('http://localhost:8000/admin/users')
    const usersJson = await allusers.json()
    setUsers(usersJson)
  }
  useEffect(() => {
    getUsers()
  }, [])

  return (
    <main className='w-full min-h-screen bg-gray-300 text-gray-800 pb-10'>
    <h1 className="text-3xl font-bold text-center py-10">This is my app</h1>
    <div>
      {
        users.length === 0 ? "Loader ...": users.map(user => (
          <UsersItems 
          key={user.id} 
          username={user.username} 
          email={user.email} 
          password={user.password} 
          id_role={user.id_role}/>
        ))
      }
    </div>
    </main>
  )
}

export default App

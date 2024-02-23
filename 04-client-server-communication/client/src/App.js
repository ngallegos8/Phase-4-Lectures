
import {useEffect, useState} from 'react'
import EditProductionForm from "./components/EditProductionForm"
function App(){
  const [productions, setProductions] = useState([])
  const [title, setTitle] = useState("")
  const [genre, setGenre] = useState("")
  const [description, setDescription] = useState("")
  const [editProduction, setEditProduction] = useState(false);
  const [production_edit, setProductionEdit] = useState(false)

  // GET request
  useEffect(() => {
    fetch("/productions")
    .then(response => response.json())
    .then(setProductions)
  }, [])
  
  console.log(productions)

  const handleEdit = (production) => {
    setEditProduction(!editProduction)
    setProductionEdit(production)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const newProduction = {
      title: title,
      genre: genre,
      description: description
    }
    try {
      fetch("/productions", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(newProduction)
      })
      .then(response => response.json())
      await setProductions((prevProduction) => [...prevProduction, newProduction])

      setTitle("")
      setGenre("")
      setDescription("")
    }
    catch (error){
      console.log("Cannot Create Production", error)
    }
  }

  const handleDelete = (id) => (
    fetch(`/productions/${id}`, {
      method: "DELETE"
    })
    .then((response) => {
      if (response.ok){
        setProductions((prevProduction) => prevProduction.filter((production) => production.id !== id))
      }
      else{
        console.error("Failed to delete", response.status)
      }
    })
      .catch((error) => {
        console.error("Error deleting production", error)
      })
    )
  
  return (
    <div>
      {editProduction ? (
        <EditProductionForm production={production_edit} setEditProduction={setEditProduction} setProductions={setProductions} />
      ):(
      <form onSubmit={handleSubmit}>
        <label>Title:</label>
        <input type="text" name="title" value={title} onChange={(e) => setTitle(e.currentTarget.value)}/>

        <label>Genre:</label>
        <input type="text" name="genre"value={genre} onChange={(e) => setGenre(e.currentTarget.value)}/>

        <label>Description:</label>
        <textarea name="description" value={description} onChange={(e) => setDescription(e.currentTarget.value)}/>

        <button type="submit">Create Production</button>
      </form>)
      }

      <hr />
      {productions.map((production) => (
        <div key={production.id}>
          <h2>{production.title}</h2>
          <p>{production.genre}</p>
          <p>{production.description}</p>
          <button onClick={()=> handleEdit(production)}>Edit</button>
          <button onClick={()=> handleDelete(production.id)}>Delete</button>
        </div>
      ))}
    </div>
  )
}


export default App



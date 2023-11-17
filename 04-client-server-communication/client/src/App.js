
import {useEffect, useState} from 'react'
import EditProductionForm from "./components/EditProductionForm"
function App(){
  const [productions, setProductions] = useState([])
  const [title, setTitle] = useState("")
  const [genre, setGenre] = useState("")
  const [description, setDescription] = useState("")
  const [editProduction, setEditProduction] = useState(false);
  const [production_edit, setProductionEdit] = useState(false)

  return (
    <div>
      {true ? (
        <EditProductionForm production={production_edit} setEditProduction={setEditProduction} setProductions={setProductions} />
      ):(
      <form>
        <label>Title:</label>
        <input type="text" name="title"/>

        <label>Genre:</label>
        <input type="text" name="genre"/>

        <label>Description:</label>
        <textarea name="description" />

        <button type="submit">Create Production</button>
      </form>)
      }

      <hr />
      {
        <div>
          <h2>{}</h2>
          <p>{}</p>
          <p>{}</p>
          <button>Edit</button>
          <button>Delete</button>
        </div>
      }
    </div>
  )
}


export default App



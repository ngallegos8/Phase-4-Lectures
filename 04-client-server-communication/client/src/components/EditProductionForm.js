import {useState} from "react"
function EditProductionForm({production, setEditProduction, setProductions}){

    const [title, setTitle] = useState(production.title);
    const [genre, setGenre] = useState(production.genre);
    const [description, setDescription] = useState(production.description);

    function handleSubmit(e){
      e.preventDefault()
      const updatedProduction = {
        title: title,
        genre: genre,
        description: description
      }
      fetch(`/productions/${production.id}`, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(updatedProduction)
      })
      .then(res => res.json())
      .then((updatedData) => {
        setProductions((prevProduction) => prevProduction.map((prev) =>
        prev.id === updatedData.id ? updatedData : prev
        ))
      })
      setEditProduction(false)
      .catch((error) => {
        console.error("Cannot Update", error)
      })
    }

      return (
        <form>
          <label>Title:</label>
          <input type="text" name="title" value={title} onChange={(e) => setTitle(e.target.value)}/>
    
          <label>Genre:</label>
          <input type="text" name="genre"value={genre} onChange={(e) => setGenre(e.target.value)}/>
    
          <label>Description:</label>
          <textarea
            name="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
    
          <button type="submit">Update Production</button>
        </form>
      );

}

export default EditProductionForm
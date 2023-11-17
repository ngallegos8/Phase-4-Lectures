import {useState} from "react"
function EditProductionForm({production, setEditProduction, setProductions}){

    const [title, setTitle] = useState(production.title);
    const [genre, setGenre] = useState(production.genre);
    const [description, setDescription] = useState(production.description);

      return (
        <form>
          <label>Title:</label>
          <input type="text" name="title"/>
    
          <label>Genre:</label>
          <input type="text" name="genre"/>
    
          <label>Description:</label>
          <textarea
            name="description"
          ></textarea>
    
          <button type="submit">Update Production</button>
        </form>
      );

}

export default EditProductionForm
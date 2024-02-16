import axios from 'axios'
import React, { useEffect, useState } from 'react'

function ExtractDataForm() {
    const [ url, setUrl] = useState('')
    const [loading, setLoading] = useState(false)
    const [errormessage, setErrorMessage] = useState('')
    const [insert, setInsert ] = useState('')
    const [data , setData ] = useState('')

    useEffect(( ) => {
      axios.get("/api/data_extraction")
      .then((res) => {
        setData(res.data)
      }).catch(() => {
        alert('please wait we are fetching data')
      })
    })
    const handleSubmit =  async (e) => {
          e.preventDefault();
          setLoading(true);
        try{
                const response = await axios.post('/api/data_extraction', {url});
                console.log('Data extracted', response.data)
                setLoading(false)
                setErrorMessage('');
            }
            catch (error){
            console.error("Fetching data ....", error)
            setLoading(false)
            setErrorMessage('Failed to extract data')
            }
    }
  return (
    <form action='' onSubmit={handleSubmit}>
        <input type='text' onChange={ (e) =>  setUrl(e.target.value)} />
        <input type='file' onChange={(e) => setInsert(e.target.value)} />
        {/* <label htmlFor='fileInput' >Upload File from Google Drive</label>
        <input type="file" id='fileInput' className='fileInput' accept='.pdf, .docx, .xls, .xlsx'/> */}
        <button type='submit' disabled={loading} onClick={setData}>Extracted Data</button>
        {errormessage && <p>{errormessage}</p>}
    </form>
  )
}

export default ExtractDataForm
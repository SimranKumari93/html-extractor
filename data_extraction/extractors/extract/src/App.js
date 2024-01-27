import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'
import ExtractDataForm from './components/ExtractDataForm';
// import FormComponent from './components/FormComponent';

function App() {
  const [htmlAssets, setHtmlAssets] = useState([]);
  useEffect(() => {
    axios.get('/api/html_assets/')
      .then(response => {
        setHtmlAssets(response.data);
      })
      .catch(error => {
        console.error('Error fetching HTML assets:', error);
      });
  }, []);

  return (
    <div>
      <h1 className='blue-text'>HTML Assets</h1>
      <h1 className='blue-text' st>Welcome to the data extraction system!</h1>
      <ExtractDataForm/>
      {/* <FormComponent/> */}
      <ul>
        {htmlAssets.map(asset => (
          <li key={asset.id}>
            {asset.name} - {asset.url}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

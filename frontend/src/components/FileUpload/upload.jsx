import React, { useState } from 'react';
import axios from 'axios';
import './upload.css';

const Upload = () => {
  const base_url='http://127.0.0.1:8000/'

  const [file, setFile] = useState(null);

  const [uploadStatus, setUploadStatus] = useState('');

  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file_upload', file);

    axios.post(`${base_url}uploadfile/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        console.log(response);
        setUploadStatus('Upload successful!');
      })
      .catch(error => {
        console.log(error);
        setUploadStatus('Upload failed!');
      });

    console.log('File uploaded:', file);
  };

  return (
    <div className="upload">
      <span className="material-icons upload-icon">cloud_upload</span>
      <form onSubmit={handleSubmit} className='upload-form'>
        <div className="upload-input">
          <input type="file" onChange={handleChange} />
          <button  className="upload-button" type="submit">
           Convert to MIDI
          </button>
          {uploadStatus && <p>{uploadStatus}</p>}
        </div>
      </form>
    </div>
  );
};

export default Upload;

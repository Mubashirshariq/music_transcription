import React from 'react';
import './homepage.css';
import AudioRecorder from '../AudioRecorder/audiorecorder';
import Upload from '../FileUpload/upload';

const HomePage = () => {
  return (
  <>
    <div className="home-page">
      <div className="card">
        <AudioRecorder />
        <h2 className='text-black text-2xl font-semibold mt-10'>Record Audio</h2>
        
      </div>
      <div className="card" >
        <Upload />
        <h2 className='text-black text-2xl font-semibold mt-11'>Upload Audio</h2>
      </div>
      
    </div>
 </>
  );
};

export default HomePage;

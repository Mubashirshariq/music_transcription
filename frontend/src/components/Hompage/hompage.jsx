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
      </div>
      <div className="card" >
        <Upload />
      </div>
      
    </div>
 </>
  );
};

export default HomePage;

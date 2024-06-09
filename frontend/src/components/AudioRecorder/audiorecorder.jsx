import React, { useState, useEffect, useRef } from 'react';
import { MediaRecorder,register } from 'extendable-media-recorder';
import { connect } from 'extendable-media-recorder-wav-encoder';
import './audiorecorder.css';
import axios from 'axios';

const AudioRecorder = () => {
  const [canRecord, setCanRecord] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [audioURL, setAudioURL] = useState('');
  const [isUploading, setIsUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState('');
  const recorderRef = useRef(null);
  const chunksRef = useRef([]);
  const base_url='http://127.0.0.1:8000/';
  useEffect(() => {
    setUpAudio();
  }, []);

  const setUpAudio = async () => {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      console.log('getUserMedia supported');
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        await register(await connect());
        recorderRef.current = new MediaRecorder(stream, { mimeType: 'audio/wav' });
        recorderRef.current.ondataavailable = e => {
          chunksRef.current.push(e.data);
        };
        recorderRef.current.onstop = e => {
          let blob = new Blob(chunksRef.current, { type: 'audio/wav' });
          chunksRef.current = [];
          let audioURL = URL.createObjectURL(blob);
          setAudioURL(audioURL);
          uploadAudio(blob);
        };
        setCanRecord(true);
      } catch (err) {
        console.log('The following error occurred: ' + err);
      }
    }
  };

  const toggleMic = () => {
    if (!canRecord) return;
    setIsRecording(!isRecording);
    if (!isRecording) {
      recorderRef.current.start();
    } else {
      recorderRef.current.stop();
    }
  };

  const uploadAudio = async (blob) => {
    setIsUploading(true);
    setUploadStatus('Uploading...');
  
      const formData = new FormData();
      formData.append('audio', blob, 'recording.wav');

      axios.post(`${base_url}uploadaudio/`, formData, {
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
      }
      


  return (
    <div className="audio-recorder">
      <button className={`mic-toggle ${isRecording ? 'is-recording' : ''} mt-10`} onClick={toggleMic} disabled={isUploading}>
        <span className="material-icons">mic</span>
      </button>
      <audio className="playback" controls src={audioURL}></audio>
      {isUploading && <p>{uploadStatus}</p>}
    </div>
  );
};

export default AudioRecorder;
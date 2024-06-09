from fastapi import FastAPI, File, UploadFile, Request
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

app = FastAPI()

UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

RECORDINGS_DIR = Path('recordings')
RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)

MIDI_OUTPUT_DIRECTORY = Path('midi')
MIDI_OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path for recording
@app.post("/uploadaudio/")
async def audioUpload(request: Request, audio: UploadFile = File(...)):
    data = await audio.read()
    save_to = RECORDINGS_DIR / audio.filename
    with open(save_to, "wb") as f:
        f.write(data)
    
    # Run basic_pitch prediction
    model_output, midi_data, note_events = predict(
        str(save_to),
        minimum_frequency=50.0,
        maximum_frequency=2000.0
    )
    
    # Save the MIDI data to a file
    output_midi_path = MIDI_OUTPUT_DIRECTORY / "output.mid"
    midi_data.write(str(output_midi_path))

    return {"filename": audio.filename, "output_midi": str(output_midi_path)}

# Path for file upload
@app.post("/uploadfile/")
async def fileUpload(request: Request, file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR / file_upload.filename
    with open(save_to, "wb") as f:
        f.write(data)

     # Run basic_pitch prediction
    model_output, midi_data, note_events = predict(
        str(save_to),
        minimum_frequency=50.0,
        maximum_frequency=2000.0
    )
    
    # Save the MIDI data to a file
    output_midi_path = MIDI_OUTPUT_DIRECTORY / "output.mid"
    midi_data.write(str(output_midi_path))
    return {"filename": file_upload.filename}

from fastapi import FastAPI, File, UploadFile, Request
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import time

app = FastAPI()

UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

RECORDINGS_DIR = Path('recordings')
RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)

MIDI_OUTPUT_DIRECTORY = Path('midi')
MIDI_OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

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

# Function to generate a unique filename with a timestamp
def generate_unique_base_name(directory: Path, base_filename: str) -> str:
    timestamp = int(time.time())
    unique_base_name = f"{timestamp}_{base_filename}"
    return unique_base_name

# Path for recording
@app.post("/uploadaudio/")
async def audioUpload(request: Request, audio: UploadFile = File(...)):
    data = await audio.read()
    base_filename = generate_unique_base_name(RECORDINGS_DIR, audio.filename)
    save_to = RECORDINGS_DIR / base_filename
    with open(save_to, "wb") as f:
        f.write(data)
    
    # Run basic_pitch prediction
    model_output, midi_data, note_events = predict(
        str(save_to),
        minimum_frequency=50.0,
        maximum_frequency=2000.0
    )
    
    # Save the MIDI data to a file with the same base name
    midi_filename = f"{base_filename.rsplit('.', 1)[0]}.mid"  # Change extension to .mid
    output_midi_path = MIDI_OUTPUT_DIRECTORY / midi_filename
    midi_data.write(str(output_midi_path))

    return {"filename": audio.filename, "output_midi": str(output_midi_path)}

# Path for file upload
@app.post("/uploadfile/")
async def fileUpload(request: Request, file_upload: UploadFile):
    data = await file_upload.read()
    base_filename = generate_unique_base_name(UPLOAD_DIR, file_upload.filename)
    save_to = UPLOAD_DIR / base_filename
    with open(save_to, "wb") as f:
        f.write(data)

    # Run basic_pitch prediction
    model_output, midi_data, note_events = predict(
        str(save_to),
        minimum_frequency=50.0,
        maximum_frequency=2000.0
    )
    
    # Save the MIDI data to a file with the same base name
    midi_filename = f"{base_filename.rsplit('.', 1)[0]}.mid"  # Change extension to .mid
    output_midi_path = MIDI_OUTPUT_DIRECTORY / midi_filename
    midi_data.write(str(output_midi_path))

    return {"filename": file_upload.filename, "output_midi": str(output_midi_path)}

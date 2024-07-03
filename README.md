# Musical  Transcription and assistance via Generative AI

This repository contains a web application for music transcription. The frontend is built with React, and the backend is powered by FastAPI. The application allows users to record audio or upload audio files, and then it transcribes the audio into MIDI files.

## Features

- Record audio directly from the browser.
- Upload audio files for transcription.
- Transcribe audio to MIDI using Basic Pitch.

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI
- **MIDI Transcription**: Basic Pitch

## Setup Instructions

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Python 3.7+](https://www.python.org/)
- [venv](https://docs.python.org/3/library/venv.html) (for creating virtual environments)

### Frontend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/music_transcription.git
    cd music_transcription
    ```

2. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```

3. Install the dependencies:
    ```sh
    npm install
    ```

4. Start the frontend development server:
    ```sh
    npm run dev
    ```

### Backend Setup
Now create one more terminal to run the backend
1. Navigate to the `backend` directory:
    ```sh
    cd music_transcription
    cd backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv myenv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source myenv/bin/activate
        ```

5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

## Usage

Once both the frontend and backend servers are running, you can access the application by navigating to `http://localhost:5173` in your web browser.



### Example Usage

1. Record audio or upload an audio file using the web interface.
2. The backend will process the audio and transcribe it to a MIDI file.
3. The midi file is saved in MIDI folder inside the backend folder as of now.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes you'd like to make.

## License

This project is licensed under the GNU Public License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Basic Pitch](https://github.com/spotify/basic-pitch) for MIDI transcription.



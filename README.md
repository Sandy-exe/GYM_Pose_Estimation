
# GYM_POSE_ESTIMATION

**GYM_POSE_ESTIMATION** is an AI-driven posture recognition system designed to assess injury risks during gym exercises. By leveraging computer vision and artificial intelligence, this project captures and analyzes user posture in real-time, providing immediate feedback to minimize injury risks and enhance workout effectiveness. 

Currently, the system is focused on analyzing posture for bicep curls. Future development will extend the system to evaluate a wider range of gym exercises.

## Project Components

1. **Pose Estimation**: Utilizes Mediapipe to detect and analyze human pose.
2. **Angle Calculation**: Computes joint angles to evaluate posture accuracy.
3. **Text-to-Speech (TTS)**: Provides audible feedback on detected posture issues.
4. **Camera Detection**: Ensures camera availability for capturing real-time video.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/GYM_POSE_ESTIMATION.git
    cd GYM_POSE_ESTIMATION
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main application**:
    ```bash
    python main.py
    ```

2. The application will start the camera feed and continuously analyze the user's posture, providing feedback through text-to-speech.

## File Structure

- `main.py`: The main entry point of the application, handling the camera feed and integration of modules.
- `modules/pose_estimation.py`: Contains logic for pose estimation using Mediapipe.
- `modules/angle_calculation.py`: Functions for calculating joint angles.
- `modules/text_to_speech.py`: Manages text-to-speech functionality.
- `modules/camera_detection.py`: Utility for detecting available cameras.
- `requirements.txt`: Lists required Python packages.

## Notes

- Ensure you have the required hardware (camera) and software (Python packages) set up before running the application.
- For optimal performance, use a high-resolution camera.

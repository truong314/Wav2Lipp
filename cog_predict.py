from cog import BasePredictor, Input, Path
import subprocess

class Predictor(BasePredictor):
    def predict(
        self,
        audio_path: Path = Input(description="Path to input audio file"),
        face_path: Path = Input(description="Path to input face image"),
        checkpoint_path: str = Input(description="Path to Wav2Lip checkpoint", default="checkpoints/wav2lip.pth"),
        outfile: str = Input(description="Output video filename", default="results/output.mp4"),
    ) -> Path:
        # Call the original Wav2Lip predict.py script
        cmd = [
            "python", "predict.py",
            "--checkpoint_path", checkpoint_path,
            "--face", str(face_path),
            "--audio", str(audio_path),
            "--outfile", outfile,
        ]
        subprocess.run(cmd, check=True)
        return Path(outfile)

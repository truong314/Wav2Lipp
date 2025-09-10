from cog import BasePredictor, Input
import inference  # import the repo's inference.py

class Predictor(BasePredictor):
    def predict(
        self,
        audio_path: str = Input(description="Path to input audio file"),
        face_path: str = Input(description="Path to input face image")
    ) -> str:
        # ⚠️ adjust this depending on how inference.py works
        result = inference.main(audio_path, face_path)
        return str(result)

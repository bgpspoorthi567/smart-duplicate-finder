import librosa
import numpy as np

def extract_audio_features(path):
    try:
        y, sr = librosa.load(path, mono=True)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return np.mean(mfcc.T, axis=0)
    except:
        return None

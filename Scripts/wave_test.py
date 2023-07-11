import numpy as np
import sounddevice as sd
from scipy.signal import resample, resample_poly

def generate_waveform(frequency, waveform_type, duration=1, sampling_rate=44100) -> np.ndarray:
    """
    Generates a waveform of a specified frequency and type. Supports sine and square.
    #TODO: Add sawtooth?

    Parameters:
        - frequency (float): The frequency of the waveform in Hertz.
        - waveform_type (str): The type of waveform to generate. Valid options are 'sine' and 'square'.
        - duration (float, optional): The duration of the waveform in seconds. Default: 1 second.
        - sampling_rate (int, optional): The sampling rate of the waveform in samples per second. Default: 44100 Hz.

    Returns:
        numpy.ndarray: 1-dimensional NumPy array.
    """

    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

    if waveform_type == 'sine':
        x = np.sin(2 * np.pi * frequency * t)
    elif waveform_type == 'square':
        x = np.sign(np.sin(2 * np.pi * frequency * t))
    else:
        raise ValueError('Choose either "sine" or "square".')

    # Normalize
    x = x / np.max(np.abs(x))

    return x

def transpose_waveform(waveform, transposition_factor, sampling_rate):
    new_sampling_rate = sampling_rate * transposition_factor
    transposed_waveform = resample(waveform, int(len(waveform) * (new_sampling_rate / sampling_rate)))

    return transposed_waveform

def add_noise(waveform, amplitude=0.06):
    noise = np.random.normal(scale=amplitude, size=len(waveform))
    noisy_waveform = waveform + noise

    return noisy_waveform

if __name__ == "__main__":
    f = 440  # Sine wave @ 440 Hz
    x = generate_waveform(f, 'sine')
    sd.play(x)
    sd.wait()

    sd.play(add_noise(x))
    sd.wait()

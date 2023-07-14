import numpy as np
import sounddevice as sd
from scipy.signal import resample, resample_poly, convolve2d

def generate_waveform(frequency, type, duration=1, sampling_rate=44100) -> np.ndarray:
    """
    Generates a waveform of a specified frequency and type.

    Parameters:
        - frequency (float): The frequency of the waveform in Hertz.
        - type (str): The type of waveform to generate. Valid options are 'sine', 'square' and 'saw'.
        - duration (float, optional): The duration of the waveform in seconds. Default: 1 second.
        - sampling_rate (int, optional): The sampling rate of the waveform in samples per second. Default: 44100 Hz.

    Returns:
        numpy.ndarray: 1-dimensional NumPy array.
    """

    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

    if type == 'sine':
        x = np.sin(2 * np.pi * frequency * t)
    elif type == 'square':
        x = np.sign(np.sin(2 * np.pi * frequency * t))
    elif type == 'saw':
        x = 2 * (np.mod(frequency * t, 1) - 0.5)
    else:
        raise ValueError('Choose either "sine", "square" or "saw".')

    # Normalize
    x = x / np.max(np.abs(x))

    return x

def add_noise(waveform, amplitude=0.06):
    noise = np.random.normal(scale=amplitude, size=len(waveform))
    return waveform + noise

def make_matrix(waveform, **kwargs):
    """
    Reshapes a waveform array into a matrix with the specified shape.

    Parameters:
        waveform: Input waveform array.
        shape: Desired shape of the matrix. Defaults to (210, 210).
    """

    matrix_shape = kwargs.get('shape', (210, 210)) # Default shape fits 1 sec @ 44.1kHz
    matrix = np.reshape(waveform, matrix_shape)

    return matrix

def make_array(matrix):
    return np.reshape(matrix, -1)

def row_col_swap(waveform_matrix):
    return np.transpose(waveform_matrix)

if __name__ == "__main__":
    x = generate_waveform(frequency=440, type='saw')
    sd.play(x)
    sd.wait()

    x = make_matrix(x)

    x = row_col_swap(x)

    x = make_array(x)

    sd.play(x)
    sd.wait()
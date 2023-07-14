import numpy as np
import sounddevice as sd

def generate_waveform(frequency, type, dur=1, sampling_rate=44100) -> np.ndarray:
    """
    Generates a waveform of a specified frequency and type.

    Parameters:
        - frequency (float): The frequency of the waveform in Hertz.
        - type (str): The type of waveform to generate. Valid options are 'sine', 'square' and 'saw'.
        - dur (float, optional): The duration of the waveform in seconds. Default: 1 second.
        - sampling_rate (int, optional): The sampling rate of the waveform in samples per second. Default: 44100 Hz.

    Returns:
        numpy.ndarray: 1-dimensional NumPy array.
    """

    t = np.linspace(0, dur, int(dur * sampling_rate), endpoint=False)

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

def convert_waveform(waveform, **kwargs):
    """
    Converts a waveform array to a matrix or a matrix to an array based on the input type.

    Parameters:
        waveform: Input waveform array or matrix.
        shape: Desired shape of the matrix. Defaults to (210, 210).

    Returns:
        ndarray: Matrix representation of the waveform if input is an array.
        ndarray: Flattened array representation of the matrix if input is a matrix.
    """
    if isinstance(waveform, np.ndarray) and waveform.ndim == 1:
        matrix_shape = kwargs.get('shape', (210, 210)) # Default shape fits 1 sec @ 44.1kHz
        matrix = np.reshape(waveform, matrix_shape)
        return matrix
    elif isinstance(waveform, np.ndarray) and waveform.ndim > 1:
        return np.reshape(waveform, -1)
    else:
        raise ValueError("Input waveform must be a 1-dimensional array or a matrix.")

def row_col_swap(waveform_matrix):
    return np.transpose(waveform_matrix)


def bitcrush(waveform, bit_depth):
    """
    Reduces the bit depth of either a waveform array or waveform matrix.
    """
    max_value = np.max(waveform)
    quantization_levels = 2 ** bit_depth - 1
    quantize = np.round(waveform / max_value * quantization_levels) / quantization_levels
    return quantize * max_value


if __name__ == "__main__":
    d = generate_waveform(frequency=587.33, type='saw', dur=0.05)
    a = generate_waveform(frequency=880, type='saw', dur=0.1)
    gs = generate_waveform(frequency=830.61, type='saw', dur=0.3)
    g = generate_waveform(frequency=783.99, type='saw', dur=0.3)
    f = generate_waveform(frequency=698.46, type='saw', dur=0.1)

    sd.play(d)
    sd.wait()

    sd.play(d)
    sd.wait()

    sd.play(a)
    sd.wait()

    sd.play(gs)
    sd.wait()

    sd.play(g)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(d)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(g)
    sd.wait()

    d = bitcrush(d, 0.7)

    sd.play(d)
    sd.wait()

    sd.play(d)
    sd.wait()

    a = bitcrush(a, 0.9)

    sd.play(a)
    sd.wait()

    sd.play(gs)
    sd.wait()

    sd.play(g)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(d)
    sd.wait()

    sd.play(f)
    sd.wait()

    sd.play(g)
    sd.wait()


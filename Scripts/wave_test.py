import numpy as np
import sounddevice as sd
from scipy.signal import butter, filtfilt

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
    elif type == 'noise':
        x = np.random.random_sample(int(dur * sampling_rate)) * 2 - 1
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

def tailify(waveform, sample_rate=44100, tail_duration=0.2, amplitude=0.1):
    tail_samples = int(tail_duration * sample_rate)

    # Create fading tail envelope
    tail_env = np.linspace(1.0, 0.0, tail_samples)

    # Apply the fading tail to the waveform
    waveform[-tail_samples:] *= amplitude * tail_env

    return waveform / np.max(np.abs(waveform))

def pass_filter(waveform, sample_rate=44100, cutoff_frequency=250, btype='low'):

    nyquist_frequency = 0.5 * sample_rate # ayy its nyquist
    normalized_cutoff_frequency = cutoff_frequency / nyquist_frequency
    b, a = butter(4, normalized_cutoff_frequency, btype=btype)

    filtered_waveform = filtfilt(b, a, waveform)

    return filtered_waveform / np.max(np.abs(filtered_waveform))


if __name__ == "__main__":

    snare = tailify(generate_waveform(500, 'sine', 0.2))
    kick = tailify(pass_filter(generate_waveform(250, 'sine', 0.2)))
    hat = tailify(pass_filter(generate_waveform(2000, 'noise', 0.2), cutoff_frequency=1400, btype='low'), tail_duration=0.1)

    for i in range(20):
        sd.play(kick)
        sd.wait()

        sd.play(hat)
        sd.wait()

        sd.play(snare)
        sd.wait()

        sd.play(hat)
        sd.wait()



    freq = 440.0
    for i in range(9):
        waveform = generate_waveform(frequency=freq, type='square', dur=0.02)

        # Play the waveform
        sd.play(bitcrush(waveform, bit_depth=freq*0.01))
        sd.wait()

        freq += 20
    
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

    gs = bitcrush(gs, 0.7)
    g = bitcrush(g, 0.9)

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


    d = generate_waveform(frequency=587.33, type='sine', dur=0.05)
    a = generate_waveform(frequency=880, type='sine', dur=0.1)
    gs = generate_waveform(frequency=830.61, type='sine', dur=0.3)
    g = generate_waveform(frequency=783.99, type='sine', dur=0.3)
    f = generate_waveform(frequency=698.46, type='sine', dur=0.1)


    d = bitcrush(d, 0.7)

    sd.play(d)
    sd.wait()

    sd.play(d)
    sd.wait()

    a = bitcrush(a, 0.9)

    sd.play(a)
    sd.wait()

    gs = bitcrush(gs, 0.7)
    g = bitcrush(g, 0.9)

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
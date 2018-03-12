import numpy as np
from scipy.fftpack import fft
import utils as utils

def choose_frequencies():
    """    
    :return: [int, int, int]
    """
    freq1 = 12
    freq2 = 10
    freq3 = 15
    return [freq1, freq2, freq3]


def add_the_waves(freqs):
    """
    :param freqs: [int, int, int]
    :return: [np.array, np.array, np.array, np.array]
        representing wave1, wave2, wave3, sum of waves
        each array contains 500(by default) discrete values for plotting a sinusoidal
    """
    _, _, t = utils.get_wave_timing()
    w1, w2, w3 = utils.make_waves(t, freqs)
    sum_waves = w1+w2+w3
    return [w1, w2, w3, sum_waves]


def demo_fft(sum_waves):
    num_samples, spacing, _ = utils.get_wave_timing()
    y_fft = ftt(sum_waves)
    x_fft = np.linspace(0.0, 1.0/spacing, num_samples)
    return x_fft, y_fft
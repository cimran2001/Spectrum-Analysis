import os
import math
import pickle
from dataclasses import dataclass
from typing import Iterable, Dict, Optional
from pprint import pprint

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

FIGURES_PATH = './Figures'
FILENAME = './data.dat'
SAVE_FIGURES_MODE = False


@dataclass
class Data:
    title: str
    frequencies: np.array
    spectrums: Dict[str, np.array]
    measurements: np.array
    timeline: np.array


def import_data(filename: str) -> Optional[Data]:
    if not os.path.exists(filename):
        return None

    with open(filename, 'rb') as f:
        data = pickle.load(f)

    title = data['Title']

    freq_max = data['Frequency Max']
    freq_min = data['Frequency Min']
    freq_step = data['Frequency Step']
    freqs = np.arange(freq_min, freq_max, freq_step)

    spectrums = data['Pure Spectrums']
    measurements = np.array([i['Data'] for i in data['Measurements']])
    timeline = np.array([i['Time'] * 3600 for i in data['Measurements']])

    return Data(title, freqs, spectrums, measurements, timeline)


def plot_spectrums(frequencies: np.array, spectrums: Dict[str, np.array], save_figure: bool = False) -> None:
    for name, values in spectrums.items():
        plt.clf()
        title = f'{name}\'s Spectrum'
        plt.title(title)
        plt.plot(frequencies, values)
        plt.xlabel('Frequencies, Hz')
        plt.ylabel('Intensity, a.u.')
        if save_figure:
            plt.savefig(f"{FIGURES_PATH}/{title}.png")
        else:
            plt.show()


def get_peaks_all(spectrums: Dict[str, np.array]) -> Dict[str, np.array]:
    peaks = {}
    for name, values in spectrums.items():
        peak_values, _ = find_peaks(values)
        peaks[name] = peak_values
    return peaks


def get_concentrations(frequencies: np.array, measurements: np.array, spectrums: np.array) -> np.array:
    def solution_spectrum(_, *concentrations: Iterable[float]) -> np.array:
        return sum(spectrum * concentration for spectrum, concentration in zip(spectrums.values(), concentrations))

    calculated_concentrations = (np.array([
        curve_fit(solution_spectrum, frequencies, measurement, p0=[1] * len(spectrums))[0]
        for measurement in measurements]) * 1e-6).transpose()
    return calculated_concentrations


def plot_concentrations(timeline: np.array, concentrations: np.array,
                        labels: Iterable[str], save_figure: bool = False) -> None:
    plt.clf()
    for row, label in enumerate(labels):
        plt.plot(timeline, concentrations[row], label=label)
    plt.xlabel('Elapsed time, seconds')
    plt.ylabel('Concentrations, moles')
    plt.legend()
    if save_figure:
        plt.savefig(f'{FIGURES_PATH}/Concentrations.png')
    else:
        plt.show()


def is_product(concentration: np.array) -> bool:
    return concentration[-1] > concentration[0]


def get_random_product_concentration(concentrations: np.array) -> Optional[np.array]:
    return next(filter(is_product, concentrations), None)


def get_reaction_rate(concentrations: np.array, timeline: np.array) -> float:
    product_concentration = get_random_product_concentration(concentrations)
    product_based_rate = np.diff(product_concentration) / np.diff(timeline)
    rates = product_based_rate / math.prod(
        np.array([concentration[:-1] for concentration in concentrations if not is_product(concentration)]))
    return rates.mean()


def main() -> None:
    data = import_data(FILENAME)
    if data is None:
        print('Couldn\'t read data. Terminating...')
        return

    plot_spectrums(data.frequencies, data.spectrums, SAVE_FIGURES_MODE)
    peaks = get_peaks_all(data.spectrums)
    pprint(peaks)
    concentrations = get_concentrations(data.frequencies, data.measurements, data.spectrums)
    plot_concentrations(data.timeline, concentrations, data.spectrums.keys(), SAVE_FIGURES_MODE)
    k = get_reaction_rate(concentrations, data.timeline)
    print(f'Reaction rate: {k:.2}')


# Code starts here
if __name__ == '__main__':
    main()

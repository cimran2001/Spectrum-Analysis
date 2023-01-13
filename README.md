# Spectrum Analysis

## Introduction

This project is created to analyze a NMR spectrum of the mixture and calculate the concentrations of the compounds and the rate of the reaction between them.

It's written using only Python 3.
Successfully tested on Python 3.10.8.

## Packages

There are the list of packages needed for this project:
* Build-in packages:
  * **os** - check if data file exists to eliminate the risk of *FileNotFoundError*
  * **math** - calculate the product of matrices
  * **dataclasses** - creation of a dataclass to store data
  * **typing** - type hints
  * **pprint** - pretty-printing of a collection
  * **pickle** - working with binary files
* Third-party packages:
  * **numpy** - working with arrays (tested on version 1.24.1)
  * **matplotlib** - plotting data (tested on version 3.6.3)
  * **scipy** - functions for scientific and technical computing (tested on version 1.10.0)

All third-party packages are listed in [requirements.txt](./requirements.txt) file. 

Install packages on Windows:
```
$ pip install -r requirements.txt
```

Install packages on UNIX (Linux or macOS):
```
$ pip3 install -r requirements.txt
```


## Data representation 

The data should be given in a binary file in a special format. Here is how the data should be presented:

* **Title** - the title of this data
* **Frequency Min** - minimal value of NMR spectrum's frequency range
* **Frequency Max** - maximal value of NMR spectrum's frequency range
* **Frequency Step** - step value of NMR spectrum's frequency range
* **Pure Spectrums** - spectrums of the components.
* **Measurements** - list of measurements which includes:
  * **Time** - when a measurement has been taken (given in hours)
  * **Data** - the result of the measurement

## Usage

1. Open terminal in a folder where you want to clone the repository.
2. Replace the existing *data.dat* with your own data.
3. Enter this code in terminal:
```
$ git clone https://github.com/cimran2001/Spectrum-Analysis 'Spectrum Analysis'
$ cd 'Spectrum Analysis'
```
4. Run this code on Python:
* On Windows:
```
$ python main.py
```
* On Linux
```
$ python3 main.py
```

## Results

Here are an example of the results of calculations including peaks of the spectrum for given data including peak values of spectrums and reaction rate constant's value:

> {\
> &nbsp;&nbsp;&nbsp;&nbsp;
> 'Acetic Acid': array([20330]),\
> &nbsp;&nbsp;&nbsp;&nbsp;
> 'Propanol': array([ 9018,  9208,  9397, 16488, 16539, 16724, 16910, 17095, 17280,
>      17466, 32751, 32931, 33111]),\
> &nbsp;&nbsp;&nbsp;&nbsp;
> 'Propylacetate': array([ 8916,  9088,  9261, 17755, 17930, 18105, 18279, 18454, 18628,
>       20380, 41075, 41123, 41300, 41479])\
> }
>
> Reaction rate: 5.2

Figures folder has newly created graphs' images if image save mode is *True*.

![Acetic Acid's Spectrum](Figures/Acetic%20Acid's%20Spectrum.png)
![Propanol's Spectrum](Figures/Propanol's%20Spectrum.png)
![Propylacetate's Spectrum](Figures/Propylacetate's%20Spectrum.png)
![Concentrations](Figures/Concentrations.png)

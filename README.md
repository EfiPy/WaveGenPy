# Introduction
wav file generator.  
1. it can have different amplitude, frequency in multichannel wav file 
3. it uses different plug-in to produce different wave form.
# Wave file command
```
python3 SampleTone.py          # basic waveform from InToneFunc.py plu-in
python3 SampleSquareFourier.py # squarewave by fourier series from plu-in InSquareFourier.py
``` 
## Help 
```
python3 SampleTone.py  -h
usage: SampleTone.py [-h] [-t DURATION] [-r {8,16,24,32}] [-s SAMPLERATE]
                     [-o OUTPUT] [-c CHANNELS]
                     [-w {square,sine,triangle,sawtooth,dc}]
                     [-W {square,sine,triangle,sawtooth,dc} [{square,sine,triangle,sawtooth,dc} ...]]
                     [-f FREQUENCY] [-F FREQUENCYS [FREQUENCYS ...]]
                     [-v VOLUME] [-V VOLUMES [VOLUMES ...]] [-p PHASE]
                     [-P PHASES [PHASES ...]]

Generate wave file.

optional arguments:
  -h, --help            show this help message and exit
  -t DURATION           set wav's duration in seconds (3.0)
  -r {8,16,24,32}       set wav's resolution
  -s SAMPLERATE         set wav's sampling rate [8000Hz:1000000000Hz]
  -o OUTPUT             set name of wav file
  -c CHANNELS           set wav's channels [1:16]
  -w {square,sine,triangle,sawtooth,dc}
                        set wav's default wave form
  -W {square,sine,triangle,sawtooth,dc} [{square,sine,triangle,sawtooth,dc} ...]
                        set wav's wave forms for multichannel
  -f FREQUENCY          set wav's default frequency [0:20000]
  -F FREQUENCYS [FREQUENCYS ...]
                        set wav's each frequency for each channel [0:20000]
  -v VOLUME             set wav's default amplitude [0:100]
  -V VOLUMES [VOLUMES ...]
                        set wav's each amplitude for each channel [0:100]
  -p PHASE              set wav's default phase [-360:360]
  -P PHASES [PHASES ...]
                        set wav's each phase for each channel [-360:360]
```
# Wav file spec
[WaveFile Gem](https://wavefilegem.com/how_wave_files_work.html)  
[Audio File Format Specifications](http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html)

# Samples 
## SampleTone.py uses InToneFunc.py plu-in.  
### Generate 4 channels wav file  
```
python3 SampleTone.py -c 4 -w sine
```
![SampleToneBasic](https://github.com/EfiPy/WaveGenPy/blob/master/Screenshot/SampleToneBasic.png?raw=true)
### Generate wav file, each channel has different wave form  
```
python3 SampleTone.py -W sine square triangle sawtooth dc -f 30 -t 0.3 -v 70
```
Produce 5 channels wave file which includes these wave form... sine wave, square wave, triangle wave, sawtooth wave and dc.  
Sample rate: default (48kHz).  
Resilution: 16 bits  
Length: 0.3 second.  
Amplitude: 70 of 100  
Wave frequency: 30Hz  
![SampleToneWave](https://github.com/EfiPy/WaveGenPy/blob/master/Screenshot/SampleToneWave.png?raw=true)
### Generate wav file, each channel has different phase  
```
python3 SampleTone.py -w sine -P -270 -180 -90 0 90 180 270 -f 30 -t 0.3 -v 70
```
Phase: -270, -180, -90, 0, 90, 180, 270
![SampleTonePhase](https://github.com/EfiPy/WaveGenPy/blob/master/Screenshot/SampleTonePhase.png?raw=true)
## SampleSquareFourier.py uses InSquareFourier.py plu-in.  
### Produce squrewave from fourier series  
```
python3 SampleSquareFourier.py -f 30 -t 0.3 -v 70 -W SF1 SF2 SF3 SF4 SF5 SF30
```
squrewave by fourier series with N = 1, 2, 3, 30  
![SampleSquareFourier](https://github.com/EfiPy/WaveGenPy/blob/master/Screenshot/SampleSquareFourier.png?raw=true)

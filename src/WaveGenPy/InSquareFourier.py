import math

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)
#
# nth (int):                The Nth sample from start of wave form
# SampleRate (float):       Sampling Rate
# ChannelInfo: (Frequency, Amplitude, Phase)
# Frequency (float):        Wave frequency
# Amplitude (0.0 ~ 1.0):    Wave amplitude
# Phase (0 ~ 360):          Wave phase
#

def SquareFourierN (Num, nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo
  t = float(nth) / float (SampleRate)

  r = 0.0
  for k in range (1, Num + 1):
    r += math.sin(2 * (2 * k - 1) * math.pi * ( f * t + p / 360.0)) / (2 * k - 1)

  return PackFunc(a * 4 * (r / math.pi))

WavformDict = {
    'SF1':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 1, nth, SampleRate, ChannelInfo, PackFunc),
    'SF2':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 2, nth, SampleRate, ChannelInfo, PackFunc),
    'SF3':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 3, nth, SampleRate, ChannelInfo, PackFunc),
    'SF4':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 4, nth, SampleRate, ChannelInfo, PackFunc),
    'SF5':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 5, nth, SampleRate, ChannelInfo, PackFunc),
    'SF6':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 6, nth, SampleRate, ChannelInfo, PackFunc),
    'SF7':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 7, nth, SampleRate, ChannelInfo, PackFunc),
    'SF8':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 8, nth, SampleRate, ChannelInfo, PackFunc),
    'SF9':  lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN ( 9, nth, SampleRate, ChannelInfo, PackFunc),
    'SF10': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (10, nth, SampleRate, ChannelInfo, PackFunc),
    'SF11': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (11, nth, SampleRate, ChannelInfo, PackFunc),
    'SF12': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (12, nth, SampleRate, ChannelInfo, PackFunc),
    'SF13': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (13, nth, SampleRate, ChannelInfo, PackFunc),
    'SF14': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (14, nth, SampleRate, ChannelInfo, PackFunc),
    'SF15': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (15, nth, SampleRate, ChannelInfo, PackFunc),
    'SF16': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (16, nth, SampleRate, ChannelInfo, PackFunc),
    'SF17': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (17, nth, SampleRate, ChannelInfo, PackFunc),
    'SF18': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (18, nth, SampleRate, ChannelInfo, PackFunc),
    'SF19': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (19, nth, SampleRate, ChannelInfo, PackFunc),
    'SF20': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (20, nth, SampleRate, ChannelInfo, PackFunc),
    'SF21': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (21, nth, SampleRate, ChannelInfo, PackFunc),
    'SF22': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (22, nth, SampleRate, ChannelInfo, PackFunc),
    'SF23': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (23, nth, SampleRate, ChannelInfo, PackFunc),
    'SF24': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (24, nth, SampleRate, ChannelInfo, PackFunc),
    'SF25': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (25, nth, SampleRate, ChannelInfo, PackFunc),
    'SF26': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (26, nth, SampleRate, ChannelInfo, PackFunc),
    'SF27': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (27, nth, SampleRate, ChannelInfo, PackFunc),
    'SF28': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (28, nth, SampleRate, ChannelInfo, PackFunc),
    'SF29': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (29, nth, SampleRate, ChannelInfo, PackFunc),
    'SF30': lambda nth, SampleRate, ChannelInfo, PackFunc: SquareFourierN (30, nth, SampleRate, ChannelInfo, PackFunc),
}

WavformName = tuple (WavformDict.keys ())

#
# Test code
#
if __name__ == '__main__':

  NUM_SECONDS   = 0.1
  SAMPLE_RATE   = 48000
  WAVFORM       = ['SF1', 'SF2', 'SF3', 'SF4', 'SF5']
  FREQUENCY     = [440,         1000,       5000,       5000]
  VOLUME        = [10.0/100,    20.0/100,   30.0/100,   100.0/100] # 100/100
  RESOLUTION    = 32

  import wave
  from OutWaveFunc import WavPackDict

  ChannelInfo = tuple(zip (WAVFORM, FREQUENCY, VOLUME))

  file = wave.open('SquareFourier.wav','wb')
  file.setnchannels (len(ChannelInfo))
  file.setsampwidth (RESOLUTION//8)
  file.setframerate (SAMPLE_RATE)

  print ('CHANNELS', len(ChannelInfo))
  print ('WAVFORM', WAVFORM)
  print ('FREQUENCY', FREQUENCY)
  print ('VOLUME',      VOLUME)

  PackFun = WavPackDict [RESOLUTION]

  for i in range (int (NUM_SECONDS * SAMPLE_RATE)):

    data = b''

    for Wavform, Frequency, Volume in ChannelInfo:

        data += WavformDict [Wavform] (i, SAMPLE_RATE, (Frequency, Volume, 0), PackFun)

    file.writeframesraw(data)

  file.close()

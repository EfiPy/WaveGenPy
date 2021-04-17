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

#
# generate DC
#
def DC (nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo
  return PackFunc (a)

#
# Sine Function: generate sine wave
#
def SineWav (nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo
  t = float(nth) / float (SampleRate)

  r = a * math.sin(2 * math.pi * ( f * t + p / 360.0))
  return PackFunc (r)

def SquareWav (nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo

  # t = float(nth) / float (SampleRate)
  # r = a if math.sin(2 * math.pi * f * t) > 0 else -a
  # r = a if ((2 * math.pi * f * t) % (2 * math.pi)) > math.pi else -a
  # r = a if ((2 * f * t) % 2.0) > 1 else -a

  phase = (p / 360.0) * SampleRate

  r = -a if (((f * nth + phase) % SampleRate)) > (SampleRate / 2) else a

  return PackFunc (r)

def TriangleWav (nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo

  phase = (p / 360.0) * SampleRate

  t1 = (f * nth + phase) % SampleRate
  t2 = SampleRate / 4
  if t1 < t2:
    r = t1 / t2
  elif t1 < t2 * 2:
    r = ((t2 * 2) - t1) / t2
  elif t1 < t2 * 3:
    r = - (t1 - (t2 * 2)) / t2
  else:
    r = - ((t2 * 4) - t1) / t2

  r = r * a

  return PackFunc (r)

def SawtoothWav (nth, SampleRate, ChannelInfo, PackFunc):

  f, a, p = ChannelInfo

  phase = (p / 360.0) * SampleRate

  t1 = (f * nth + phase) % SampleRate
  t2 = SampleRate / 2
  if t1 < t2:
    r = t1 / t2
  else:
    r = - ((t2 * 2) - t1) / t2

  r = r * a

  return PackFunc (r)

WavformDict = {
    'sine':       SineWav,
    'square':     SquareWav,
    'triangle':   TriangleWav,
    'sawtooth':   SawtoothWav,
    'dc':         DC,
}

WavformName = tuple (WavformDict.keys ())

#
# Test code
#
if __name__ == '__main__':

  NUM_SECONDS   = 0.1
  SAMPLE_RATE   = 48000
  WAVFORM       = ['dc',        'dc',       'dc',      'sine']
  FREQUENCY     = [440,         1000,       5000,       5000]
  VOLUME        = [10.0/100,    20.0/100,   30.0/100,   100.0/100] # 100/100
  RESOLUTION    = 32

  import wave
  from OutWaveFunc import WavPackDict

  ChannelInfo = tuple(zip (WAVFORM, FREQUENCY, VOLUME))

  file = wave.open('InToneFunc%d.wav' % RESOLUTION,'wb')
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

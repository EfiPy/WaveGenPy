#!/usr/bin/python3

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

import WaveGenPy.InToneFunc as InToneFunc

import WaveGenPy.WavePara as WavePara

para = WavePara.Get (InToneFunc.WavformName)
WavePara.Dump (para)

import WaveGenPy.WaveGenEngine as WaveGenEngine
from WaveGenPy.OutWaveFunc    import WavPackDict

OutWave = WaveGenEngine.Tone (*para, InToneFunc.WavformDict, WavPackDict)
print ('parameters...')
print (OutWave)

OutWave.Generate ()

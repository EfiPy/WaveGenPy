import argparse

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

from WaveGenPy.ParaBase import MaxFrequency
from WaveGenPy.ParaBase import MaxVolume
from WaveGenPy.ParaBase import MaxChannels
from WaveGenPy.ParaBase import MaxSampleRate
from WaveGenPy.ParaBase import MinSampleRate
from WaveGenPy.ParaBase import MinPhase
from WaveGenPy.ParaBase import MaxPhase

from WaveGenPy.ParaBase import CheckFrequency
from WaveGenPy.ParaBase import CheckSampleRate
from WaveGenPy.ParaBase import CheckPhase
from WaveGenPy.ParaBase import Dump

def Get (WavformName):
    parser = argparse.ArgumentParser(description='Generate wave file.')

    parser.add_argument('-t', action = 'store', type = float,
                            help = "set wav's duration in seconds (3.0)", default = 3.0, dest = 'duration')

    parser.add_argument('-r', action = 'store', type = int , choices = [8, 16, 24, 32],
                            help = "set wav's resolution", default = 16, dest = 'resolution')

    parser.add_argument('-s', action = 'store', type = CheckSampleRate,
                            help = "set wav's sampling rate [%dHz:%dHz]" % (MinSampleRate, MaxSampleRate), default = 48000, dest = 'samplerate')

    parser.add_argument('-o', action = 'store',
                            help = 'set name of wav file', default = 'WaveGenPy.wav', dest = 'output')

    #
    # Channel number
    #
    parser.add_argument('-c', action = 'store', type = int,
                            help = "set wav's channels [1:%d]" % MaxChannels, default = 2, dest = 'channels')

    #
    # Channel info - phase
    #

    #
    # Channel info - Wave function
    #
    parser.add_argument('-w', action = 'store', choices = WavformName [:],
                            help = "set wav's default wave form", default = WavformName[0], dest = 'Wavform')

    parser.add_argument('-W', action = 'store', choices = WavformName [:], nargs='+',
                            help = "set wav's wave forms for multichannel", default = None, dest = 'Wavforms')

    #
    # Channel info - frequency
    #
    parser.add_argument('-f', action = 'store', type = CheckFrequency,
                            help = "set wav's default frequency [0:%d]" % MaxFrequency, default = 1000, dest = 'frequency')

    parser.add_argument('-F', action = 'store', type = CheckFrequency, nargs='+',
                            help = "set wav's each frequency for each channel [0:%d]" % MaxFrequency, default = None, dest = 'frequencys')

    #
    # Channel info - volume
    #
    parser.add_argument('-v', action = 'store', type = float,
                            help = "set wav's default amplitude [0:%d]" % MaxVolume, default = 100, dest = 'volume')

    parser.add_argument('-V', action = 'store', type = float, nargs='+',
                            help = "set wav's each amplitude for each channel [0:%d]" % MaxVolume, default = None, dest = 'volumes')

    #
    # Channel info - phase
    #
    parser.add_argument('-p', action = 'store', type = CheckPhase,
                            help = "set wav's default phase [%d:%d]" % (MinPhase, MaxPhase), default = 0, dest = 'phase')

    parser.add_argument('-P', action = 'store', type = CheckPhase, nargs='+',
                            help = "set wav's each phase for each channel [%d:%d]" % (MinPhase, MaxPhase), default = None, dest = 'phases')

    args = parser.parse_args()

    assert args.duration > 0.0, 'Duration must be higher than 0 seconds.'

    ChannelWavform   = 1
    ChannelFrequency = 1
    ChannelVolume    = 1
    ChannelPhase     = 1

    if (args.Wavforms is not None):
        ChannelWavform = len (args.Wavforms)
        WAVFORM = list (args.Wavforms)
    else:
        WAVFORM = [args.Wavform]

    if (args.frequencys is not None):
        assert all (x >= 0 and x <= MaxFrequency for x in args.frequencys)
        ChannelFrequency = len (args.frequencys)
        FREQUENCY = list (args.frequencys)
    else:
        FREQUENCY = [args.frequency]

    if (args.volumes is not None):
        assert all (x >= 0 and x <= MaxVolume for x in args.volumes)
        ChannelVolume = len (args.volumes)
        VOLUME = list (args.volumes)
    else:
        VOLUME = [args.volume]

    if (args.phases is not None):
        assert all (x >= MinPhase and x <= MaxPhase for x in args.phases)
        ChannelPhase = len (args.phases)
        PHASE = list (args.phases)
    else:
        PHASE = [args.phase]

    SAMPLE_RATE = args.samplerate   # Sampleing Rate
    NUM_SECONDS = args.duration     # seconds
    OUTPUT_FILE = args.output       # oiutput file name
    RESOLUTION  = args.resolution   # Resolution

    CHANNELS = max (args.channels, ChannelWavform, ChannelFrequency, ChannelVolume, ChannelPhase)

    if (CHANNELS > ChannelWavform):
        WAVFORM   += [args.Wavform]   * (CHANNELS - ChannelWavform)

    if (CHANNELS > ChannelFrequency):
        FREQUENCY += [args.frequency] * (CHANNELS - ChannelFrequency)

    if (CHANNELS > ChannelVolume):
        VOLUME    += [args.volume]    * (CHANNELS - ChannelVolume)

    if (CHANNELS > ChannelPhase):
        PHASE     += [args.phase]     * (CHANNELS - ChannelPhase)

    CHANNELS = tuple (zip (WAVFORM, FREQUENCY, VOLUME, PHASE))
    WAVINFO = (OUTPUT_FILE, NUM_SECONDS, SAMPLE_RATE, RESOLUTION)

    return WAVINFO, CHANNELS

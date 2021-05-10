import argparse

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

MaxFrequency    = 20000
MaxVolume       = 100
MaxChannels     = 16
MaxSampleRate   = 1000000000
MinSampleRate   = 8000
MinPhase        = -360
MaxPhase        = 360

def CheckFrequency (arg):
    try:
        value = int(arg)
    except ValueError as err:
       raise argparse.ArgumentTypeError(str(err))

    if value < 0 or value > MaxFrequency:
        message = "Expected frenquency 0 <= value <= %d, got value = %d" % (MaxFrequency, value)
        raise argparse.ArgumentTypeError(message)

    return value

def CheckSampleRate (arg):
    try:
        value = int(arg)
    except ValueError as err:
       raise argparse.ArgumentTypeError(str(err))

    if value < MinSampleRate or value > MaxSampleRate:
        message = "Expected sample rate %d <= value <= %d, got value = %d" % (MinSampleRate, MaxSampleRate, value)
        raise argparse.ArgumentTypeError(message)

    return value

def CheckPhase (arg):
    try:
        value = int(arg)
    except ValueError as err:
       raise argparse.ArgumentTypeError(str(err))

    if value < MinPhase or value > MaxPhase:
        message = "Expected phase %d <= value <= %d, got value = %d" % (MinPhase, MaxPhase, value)
        raise argparse.ArgumentTypeError(message)

    return value

def Dump (para):
    # WAVFORM, SAMPLE_RATE, NUM_SECONDS, FREQUENCY, RESOLUTION, CHANNELS, VOLUME, OUTPUT_FILE = para
    # OUTPUT_FILE, NUM_SECONDS, SAMPLE_RATE, RESOLUTION, CHANNELS = para
    WAVINFO, CHANNELS = para
    OUTPUT_FILE, NUM_SECONDS, SAMPLE_RATE, RESOLUTION = WAVINFO

    log = '''
  Generating wave.

    File Info:
        OUTPUT_FILE  %s
        NUM_SECONDS  %ss
        SAMPLE_RATE  %sHz
        RESOLUTION   %sbits
        CHANNEL_NUM  %d
    ''' % (
        str(OUTPUT_FILE),
        str(NUM_SECONDS),
        str(SAMPLE_RATE),
        str(RESOLUTION),
        len (CHANNELS)
    )

    for WAVFORM, FREQUENCY, VOLUME, PHASE in CHANNELS:
        log += '''
    Channel Info:
        WAVFORM      %s
        FREQUENCY    %sHz
        VOLUME       %s
        PHASE        %s
''' % (
        str(WAVFORM),
        str(FREQUENCY),
        str(VOLUME),
        str(PHASE),
    )

    print (log)

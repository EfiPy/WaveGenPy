

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

class Tone:
    def __init__ (Self,
                  WavInfo     = ('WaveGenEngine.wav', 3.0, 48000, 16),
                  ChannelInfo = ((None, 1000, 100, 0),),
                  WavformDict = None,
                  WavPackDict = None,
                  WavPackOp   = None
                  ):

        (Self.OutName,
         Self.NumSeconds,
         Self.SampleRate,
         Self.Resolution,
         ) = WavInfo

        DefaultWave = ChannelInfo[0][0]
        assert (WavformDict != None) and (WavPackDict != None) and (DefaultWave in WavformDict.keys ())

        ChannelTmp = [(WavformDict [Wavform], Frequency, Volume / 100, Phase) for Wavform, Frequency, Volume, Phase in ChannelInfo]
        Self.ChannelInfo = ChannelTmp
        Self.ChannelNum  = len (Self.ChannelInfo)

        Self.PackFunc   = WavPackDict[Self.Resolution]
        Self.PackOp     = WavPackOp

        Self.Info = {
            'OutName'   : Self.OutName,
            'NumSeconds': Self.NumSeconds,
            'SampleRate': Self.SampleRate,
            'Resolution': Self.Resolution,
            'Resolution': Self.ChannelNum,
            'ChannelInfo'  : [],
        }
        for Wavform, Frequency, Volume, Phase in ChannelInfo:
            Self.Info['ChannelInfo'].append ({'Wavform':   Wavform,
                                              'Frequency': Frequency,
                                              'Volume':    Volume,
                                              'Phase':     Phase,
                                              })

    def __str__ (Self):
        return str (Self.Info)

    __repr__ = __str__

    def Generate (Self, OutName = None):

        fName = OutName if OutName != None else Self.OutName

        Output = Self.PackOp (fName, Self.ChannelNum, Self.Resolution, Self.SampleRate)

        for i in range(int(Self.NumSeconds * Self.SampleRate)):

            data = b''

            for WavformGen, Frequency, Volume, Phase in Self.ChannelInfo:
                data += WavformGen (i, Self.SampleRate, (Frequency, Volume, Phase), Self.PackFunc)

            Output.Save (data)

        Output.Close ()

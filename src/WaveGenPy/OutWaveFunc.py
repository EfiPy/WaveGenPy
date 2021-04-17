import struct

# Copyright (C) 2021 MaxWu (EfiPy.Core@gmail.com)

PackWav8  = lambda Amp: struct.pack ('<B', int ((Amp + 1) * 127.9))
PackWav16 = lambda Amp: int  (Amp * 32767).to_bytes (2, 'little', signed=True)
PackWav24 = lambda Amp: int (Amp * 8388607).to_bytes (3, 'little', signed=True)
PackWav32 = lambda Amp: int (Amp * 2147483647).to_bytes (4, 'little', signed=True)

WavPackDict = {
    'fmt': 'wav',
    8:  PackWav8,
    16: PackWav16,
    24: PackWav24,
    32: PackWav32,
}


# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class AudioSourceDone(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAudioSourceDone(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = AudioSourceDone()
        x.Init(buf, n + offset)
        return x

    # AudioSourceDone
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # AudioSourceDone
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def AudioSourceDoneStart(builder): builder.StartObject(1)
def AudioSourceDoneAddId(builder, id): builder.PrependInt32Slot(0, id, 0)
def AudioSourceDoneEnd(builder): return builder.EndObject()

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class DynamicRobots(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDynamicRobots(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = DynamicRobots()
        x.Init(buf, n + offset)
        return x

    # DynamicRobots
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # DynamicRobots
    def Immovable(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, a + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # DynamicRobots
    def ImmovableAsNumpy(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(tdw.flatbuffers.number_types.BoolFlags, o)
        return 0

    # DynamicRobots
    def ImmovableLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DynamicRobots
    def Transforms(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, a + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # DynamicRobots
    def TransformsAsNumpy(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(tdw.flatbuffers.number_types.Float32Flags, o)
        return 0

    # DynamicRobots
    def TransformsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DynamicRobots
    def Joints(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, a + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # DynamicRobots
    def JointsAsNumpy(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(tdw.flatbuffers.number_types.Float32Flags, o)
        return 0

    # DynamicRobots
    def JointsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DynamicRobots
    def Sleeping(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, a + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # DynamicRobots
    def SleepingAsNumpy(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(tdw.flatbuffers.number_types.BoolFlags, o)
        return 0

    # DynamicRobots
    def SleepingLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def DynamicRobotsStart(builder): builder.StartObject(4)
def DynamicRobotsAddImmovable(builder, immovable): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(immovable), 0)
def DynamicRobotsStartImmovableVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def DynamicRobotsAddTransforms(builder, transforms): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(transforms), 0)
def DynamicRobotsStartTransformsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DynamicRobotsAddJoints(builder, joints): builder.PrependUOffsetTRelativeSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(joints), 0)
def DynamicRobotsStartJointsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DynamicRobotsAddSleeping(builder, sleeping): builder.PrependUOffsetTRelativeSlot(3, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(sleeping), 0)
def DynamicRobotsStartSleepingVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def DynamicRobotsEnd(builder): return builder.EndObject()

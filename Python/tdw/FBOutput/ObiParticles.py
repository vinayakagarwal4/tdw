# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class ObiParticles(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsObiParticles(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = ObiParticles()
        x.Init(buf, n + offset)
        return x

    # ObiParticles
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # ObiParticles
    def Solvers(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ObiSolverData import ObiSolverData
            obj = ObiSolverData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObiParticles
    def SolversLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObiParticles
    def Actors(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ObiActorData import ObiActorData
            obj = ObiActorData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ObiParticles
    def ActorsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ObiParticlesStart(builder): builder.StartObject(2)
def ObiParticlesAddSolvers(builder, solvers): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(solvers), 0)
def ObiParticlesStartSolversVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObiParticlesAddActors(builder, actors): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(actors), 0)
def ObiParticlesStartActorsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObiParticlesEnd(builder): return builder.EndObject()

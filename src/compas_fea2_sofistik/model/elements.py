from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.elements import BeamElement
from compas_fea2.model.elements import Face
from compas_fea2.model.elements import HexahedronElement
from compas_fea2.model.elements import MassElement
from compas_fea2.model.elements import MembraneElement
from compas_fea2.model.elements import PentahedronElement
from compas_fea2.model.elements import ShellElement
from compas_fea2.model.elements import SpringElement
from compas_fea2.model.elements import StrutElement
from compas_fea2.model.elements import TetrahedronElement
from compas_fea2.model.elements import TieElement
from compas_fea2.model.elements import TrussElement

class SofistikBeamElement(BeamElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.BeamElement`.\n
    """
    __doc__ += BeamElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikBeamElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)

    def jobdata(self):
        """Generate the jobdata for Beam Elements in the SOFiSTiK. This is part
        of the programme module SOFiMSHA.

        Warning
        -------
        By default DIV(=Equal partitioning of beam) is set to 1
        """

        return "BEAM NO {} NA {} NE {} NCS {} DIV 1".format(self.key+1,
                                                            self.nodes[0].key+1,
                                                            self.nodes[1].key+1,
                                                            self.section.key+1)


class SofistikFace(Face):
    """Sofistik implementation of :class:`compas_fea2.model.elements.Face`.\n
    """
    __doc__ += Face.__doc__

    def __init__(self, *, nodes, tag, element=None, name=None):
        super(SofistikFace, self).__init__(nodes=nodes, tag=tag, element=element, name=name)
        raise NotImplementedError

class SofistikHexahedronElement(HexahedronElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.HexahedronElement`.\n
    """
    __doc__ += HexahedronElement.__doc__

    def __init__(self, *, nodes, section, implementation=None, name=None, **kwargs):
        super(SofistikHexahedronElement, self).__init__(nodes=nodes, section=section, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikMassElement(MassElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.MassElement`.\n
    """
    __doc__ += MassElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikMassElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikMembraneElement(MembraneElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.MembraneElement`.\n
    """
    __doc__ += MembraneElement.__doc__

    def __init__(self, *, nodes, frame, section=None, implementation=None, rigid=False, name=None, **kwargs):
        super(SofistikMembraneElement, self).__init__(nodes=nodes, frame=frame, section=section, implementation=implementation, rigid=rigid, name=name, **kwargs)
        raise NotImplementedError

class SofistikPentahedronElement(PentahedronElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.PentahedronElement`.\n
    """
    __doc__ += PentahedronElement.__doc__

    def __init__(self, *, nodes, section, implementation=None, name=None, **kwargs):
        super(SofistikPentahedronElement, self).__init__(nodes=nodes, section=section, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikShellElement(ShellElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.ShellElement`.\n
    """
    __doc__ += ShellElement.__doc__

    def __init__(self, *, nodes, frame=None, section=None, implementation=None, rigid=False, name=None, **kwargs):
        super(SofistikShellElement, self).__init__(nodes=nodes, frame=frame, section=section, implementation=implementation, rigid=rigid, name=name, **kwargs)

    def jobdata(self):
        "QUA CI SARà SOLO IL COMANDO QUAD. I nodes della mesh dovrebbero uscire da nodes.py"

    # Occore lavorare con self._faces (vedi Shell element con il metodo _construct_faces). In pratica self._faces è un dizionario con key-values pari a key della faccia-indice dei nodi
    # perciò in NO {} ci andrà il numero di questo binomio, mentre in N1, N2, N3, N4 i 4 numeri del values del dizionario. Quindi mi serve sapere com accedere al numero di binomi in un 
    # dizionario, accedere ai singoli valori del 'valore rispetto ad una chiave'. Scritto con il culo ma ok. 
    # Poi dovrò trovare un modo per accedere al valore di MNO e T.
    

        #return """QUAD NO {} N1 {} N2 {} N3 {} N4 {} MNO {} T {}""".format(node._key for node in face._nodes for face in self._faces)
                                                                            #self._key for node in self._nodes for face in self._faces)
                                                                            #node[0] for node in self._nodes for face in self._faces)
        #string = ["KEY_A {0} KEY_B {1} KEY_C {2} KEY_D {3}".format([node._key for node in face._nodes]) for face in self._faces]
        string = ["QUAD NO {0} N1 {1} N2 {2} N3 {3} N4 {4} MNO {5}".format(i,
                                                                   *[node._key for node in face._nodes]) for i, face in enumerate(self._faces)]
        return string

class SofistikSpringElement(SpringElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.SpringElement`.\n
    """
    __doc__ += SpringElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikSpringElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikStrutElement(StrutElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.StrutElement`.\n
    """
    __doc__ += StrutElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikStrutElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikTetrahedronElement(TetrahedronElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.TetrahedronElement`.\n
    """
    __doc__ += TetrahedronElement.__doc__

    def __init__(self, *, nodes, section, implementation=None, name=None, **kwargs):
        super(SofistikTetrahedronElement, self).__init__(nodes=nodes, section=section, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError

class SofistikTieElement(TieElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.TieElement`.\n
    """
    __doc__ += TieElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikTieElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError


class SofistikTrussElement(TrussElement):
    """Sofistik implementation of :class:`compas_fea2.model.elements.TrussElement`.\n
    """
    __doc__ += TrussElement.__doc__

    def __init__(self, *, nodes, section, frame=None, implementation=None, name=None, **kwargs):
        super(SofistikTrussElement, self).__init__(nodes=nodes, section=section, frame=frame, implementation=implementation, name=name, **kwargs)
        raise NotImplementedError



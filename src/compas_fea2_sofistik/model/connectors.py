from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.connectors import SpringConnector
from compas_fea2.model.connectors import ZeroLengthSpringConnector


class SofistikSpringConnector(SpringConnector):
    """Sofistik implementation of :class:`compas_fea2.model.connectors.SpringConnector`.\n"""

    __doc__ += SpringConnector.__doc__

    def __init__(self, nodes, section, yielding=None, failure=None, **kwargs):
        super(SofistikSpringConnector, self).__init__(nodes, section, yielding, failure, **kwargs)

    def jobdata(self):
        return f"SPRI NA {self.nodes[0].input_key} NE {self.nodes[-1].input_key} DX 1 CP {self.section.axial} CT {self.section.lateral} CM {self.section.rotational} CRAC {self.failure['c']}"


class SofistikZeroLengthSpringConnector(ZeroLengthSpringConnector):
    """Sofistik implementation of :class:`compas_fea2.model.connectors.ZeroLengthSpringConnector`.\n"""

    __doc__ += ZeroLengthSpringConnector.__doc__

    def __init__(self, nodes, section, directions, yielding=None, failure=None, **kwargs):
        super(SofistikZeroLengthSpringConnector, self).__init__(nodes, section, directions, yielding, failure, **kwargs)

    def _stiffness_values(self):
        return {"CP": self.section.axial, "CT": self.section.lateral, "CM": self.section.rotational}

    def _direction_values(self):
        return {"DX": self.directions[0]/1000, "DY": self.directions[1]/1000, "DZ": self.directions[2]/1000}

    def _to_string(self, d):
        return " ".join([k+" "+str(v) for k, v in d.items() if v!=0])

    def jobdata(self):
        return f"SPRI NA {self.nodes[0].input_key} NE {self.nodes[-1].input_key} {self._to_string(self._direction_values())} {self._to_string(self._stiffness_values())} CRAC {self.failure['c']} MUE 1.1" #FIXME add remaining parameters

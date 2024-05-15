from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.connectors import SpringConnector


class SofistikSpringConnector(SpringConnector):
    """Sofistik implementation of :class:`compas_fea2.model.ics.InitialStressField`.\n
    """
    __doc__ += SpringConnector.__doc__

    def __init__(self, nodes, **kwargs):
        super(SofistikSpringConnector, self).__init__(nodes, **kwargs)

    @property
    def input_key(self):
        return self._key+1+self.part.key*1_000_000

    def jobdata(self):
        return f"SPRI NA {self.nodes[0].input_key} NE {self.nodes[-1].input_key} CP 2000.0 2000.0 CRAC 0"

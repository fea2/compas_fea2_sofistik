from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.nodes import Node

class SofistikNode(Node):
    """Sofistik implementation of :class:`compas_fea2.model.nodes.Node`.\n

    Note
    ----
    The nodes key numbering in compas_fea2 starts from 0, while in Sofistik starts
    from 1. The conversion in automatically resolved by compas_fea2.

    """
    __doc__ += Node.__doc__

    def __init__(self, xyz, mass=None, name=None, **kwargs):
        super(SofistikNode, self).__init__(xyz=xyz, mass=mass, name=name, **kwargs)

    @property
    def input_key(self):
        return self._key+1+self.part.key*1_000_000

    def jobdata(self):
        """Generate the jobdata for the input file of the command
        'NODE - Nodes, Coordinates and Constraints' defined in the SOFiSTiK
        programme module SOFiMSHA.

        Parameters
        ----------
        None

        Returns
        -------
        str
            input file data line.
        """
        return """NODE {} X {} Y {} Z {}""".format(self.input_key,
                                                      self.x,
                                                      self.y,
                                                      self.z)


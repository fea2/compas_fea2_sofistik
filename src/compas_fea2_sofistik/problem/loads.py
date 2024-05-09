from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.problem.loads import NodeLoad
from compas_fea2.problem.loads import GravityLoad
from compas_fea2.problem.loads import HarmonicPointLoad
from compas_fea2.problem.loads import HarmonicPressureLoad
from compas_fea2.problem.loads import PrestressLoad
from compas_fea2.problem.loads import ThermalLoad
from compas_fea2.problem.loads import TributaryLoad




class SofistikGravityLoad(GravityLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.GravityLoad`.\n
    """
    __doc__ += GravityLoad.__doc__

    def __init__(self, g, x=0, y=0, z=-1, name=None, **kwargs):
        super(SofistikGravityLoad, self).__init__(g=g, x=x, y=y, z=z, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikHarmonicPointLoad(HarmonicPointLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.HarmonicPointLoad`.\n
    """
    __doc__ += HarmonicPointLoad.__doc__

    def __init__(self, components, axes='global', name=None, **kwargs):
        super(SofistikHarmonicPointLoad, self).__init__(components=components, axes=axes, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikHarmonicPressureLoad(HarmonicPressureLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.HarmonicPressureLoad`.\n
    """
    __doc__ += HarmonicPressureLoad.__doc__

    def __init__(self, components, axes='global', name=None, **kwargs):
        super(SofistikHarmonicPressureLoad, self).__init__(components=components, axes=axes, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError



class SofistikNodeLoad(NodeLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.PointLoad`.\n
    """
    __doc__ += NodeLoad.__doc__

    def __init__(self, x=None, y=None, z=None, xx=None, yy=None, zz=None, axes='global', name=None, **kwargs):
        super(SofistikNodeLoad, self).__init__(x=x, y=y, z=z, xx=xx, yy=yy, zz=zz, axes=axes, name=name, **kwargs)
        """Generate the data for the input file for any bc.

        Parameters
        ----------
        nodes : [:class:`compas_fea2.model.nodes.Node]
            The nodes where the boundary condition is applied.

        Returns
        -------
        str
            input file data string
        """

    def jobdata(self, nodes):
        comp = {'x':'p1','y':'p2','z':'p3','xx':'p4','yy':'p5','zz':'p6'}
        return "\n".join(["NODE NO {} TYPE VV {}".format(node.key+1,
                                            ' '.join([comp[c] for c in comp if getattr(self, c)]))
                    for node in nodes])

class SofistikPrestressLoad(PrestressLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.PrestressLoad`.\n
    """
    __doc__ += PrestressLoad.__doc__

    def __init__(self, components, axes='global', name=None, **kwargs):
        super(SofistikPrestressLoad, self).__init__(components=components, axes=axes, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikThermalLoad(ThermalLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.ThermalLoad`.\n
    """
    __doc__ += ThermalLoad.__doc__

    def __init__(self, components, axes='global', name=None, **kwargs):
        super(SofistikThermalLoad, self).__init__(components=components, axes=axes, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikTributaryLoad(TributaryLoad):
    """Sofistik implementation of :class:`compas_fea2.problem.loads.TributaryLoad`.\n
    """
    __doc__ += TributaryLoad.__doc__

    def __init__(self, components, axes='global', name=None, **kwargs):
        super(SofistikTributaryLoad, self).__init__(components=components, axes=axes, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError

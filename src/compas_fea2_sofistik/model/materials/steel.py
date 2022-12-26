from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.materials.steel import Steel

class SofistikSteel(Steel):
    """Sofistik implementation of :class:`compas_fea2.model.materials.steel.Steel`.\n
    """
    __doc__ += Steel.__doc__

    def __init__(self, *, fy, fu, eu, E, v, density, name=None, **kwargs):
        super(SofistikSteel, self).__init__(fy=fy, fu=fu, eu=eu, E=E, v=v, density=density, name=name, **kwargs)
        raise NotImplementedError


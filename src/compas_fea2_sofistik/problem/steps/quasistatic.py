from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.problem.steps.quasistatic import DirectCyclicStep
from compas_fea2.problem.steps.quasistatic import QuasiStaticStep

class SofistikDirectCyclicStep(DirectCyclicStep):
    """Sofistik implementation of :class:`compas_fea2.problem.steps.quasistatic.DirectCyclicStep`.\n
    """
    __doc__ += DirectCyclicStep.__doc__

    def __init__(self, name=None, **kwargs):
        super(SofistikDirectCyclicStep, self).__init__(name=name, **kwargs)
        raise NotImplementedError


class SofistikQuasiStaticStep(QuasiStaticStep):
    """Sofistik implementation of :class:`compas_fea2.problem.steps.quasistatic.QuasiStaticStep`.\n
    """
    __doc__ += QuasiStaticStep.__doc__

    def __init__(self, name=None, **kwargs):
        super(SofistikQuasiStaticStep, self).__init__(name=name, **kwargs)
        raise NotImplementedError



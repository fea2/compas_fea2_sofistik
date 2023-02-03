from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.problem.steps.static import StaticRiksStep
from compas_fea2.problem.steps.static import StaticStep

#TODO Implement Displacements

class SofistikStaticRiksStep(StaticRiksStep):
    """Sofistik implementation of :class:`compas_fea2.problem.steps.static.StaticRiksStep`.\n
    """
    __doc__ += StaticRiksStep.__doc__

    def __init__(self, max_increments=100, initial_inc_size=1, min_inc_size=1e-05, time=1, nlgeom=False, modify=True, name=None, **kwargs):
        super(SofistikStaticRiksStep, self).__init__(max_increments=max_increments, initial_inc_size=initial_inc_size, min_inc_size=min_inc_size, time=time, nlgeom=nlgeom, modify=modify, name=name, **kwargs)
        raise NotImplementedError

class SofistikStaticStep(StaticStep):
    """Sofistik implementation of :class:`compas_fea2.problem.steps.static.StaticStep`.\n
    """
    __doc__ += StaticStep.__doc__

    def __init__(self, max_increments=100, initial_inc_size=1, min_inc_size=1e-05, time=1, nlgeom=False, modify=True, name=None, **kwargs):
        super(SofistikStaticStep, self).__init__(max_increments=max_increments, initial_inc_size=initial_inc_size, min_inc_size=min_inc_size, time=time, nlgeom=nlgeom, modify=modify, name=name, **kwargs)
        self._stype = 'Static'

    def jobdata(self):
        return """
$ LOADS and DISPLACEMENTS
+prog sofiload
LC {} TITL '{}'

head loads
{}
end

$DISPLACEMENTS
{}
""".format(self.key+1,
           self.name,
           "\n".join([pattern.load.jobdata(pattern.distribution) for pattern in self.loads]) or "$None",
           "\n".join([pattern.load.jobdata(pattern.distribution) for pattern in self.displacements]) or "$None")


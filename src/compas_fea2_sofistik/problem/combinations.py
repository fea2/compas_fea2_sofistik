from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.problem import LoadCombination

dofs = ['x',  'y',  'z',  'xx', 'yy', 'zz']


class SofistikLoadCombination(LoadCombination):
    """Sofistik implementation of :class:`compas_fea2.problem.LoadCombination`.\n
    """
    __doc__ += LoadCombination.__doc__

    def __init__(self, factors, name=None, **kwargs):
        super(SofistikLoadCombination, self).__init__(factors=factors, name=name, **kwargs)

    def jobdata(self):
        index = self.problem._steps_order.index(self.step)
        # loads = '\n'.join([load.jobdata([node]) for node, load in self.node_load])

        # FIXME change "PERM" to the specific case
        # load_cases_jobdata = "\n".join(f"LC {n} TYPE PERM NAME {load_case}" for n, load_case in enumerate(self.factors.keys()))
        load_jobdata = "\n".join(load.jobdata([node]) for node, load in self.node_load)
        return load_jobdata
        # return "\n".join(load_cases_jobdata, load_jobdata)



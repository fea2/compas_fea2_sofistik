from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from compas_fea2.results import Result, DisplacementResult, StressResult
from compas_fea2.results import DisplacementFieldResults, StressFieldResults

class SofistikResult(Result):

    def __init__(self, location, name=None, *args, **kwargs):
        super(SofistikResult, self).__init__(location, name=name, *args, **kwargs)


class SofistikDisplacementResult(DisplacementResult):

    def __init__(self, location, u1=0., u2=0., u3=0., name=None, *args, **kwargs):
        super(SofistikDisplacementResult, self).__init__(location, u1, u2, u3, name=name, *args, **kwargs)


class SofistikStressResult(StressResult):

    def __init__(self, location, local_stress_tensor, name=None, *args, **kwargs):
        super(SofistikStressResult, self).__init__(location, local_stress_tensor, name=name, *args, **kwargs)


class SofistikDisplacementFieldResults(DisplacementFieldResults):
    def __init__(self, problem, name=None, *args, **kwargs):
        super(SofistikDisplacementFieldResults, self).__init__(problem, name=name, *args, **kwargs)

class SofistikStressFieldResults(StressFieldResults):
    def __init__(self, problem, name=None, *args, **kwargs):
        super(SofistikStressFieldResults, self).__init__(problem, name, *args, **kwargs)


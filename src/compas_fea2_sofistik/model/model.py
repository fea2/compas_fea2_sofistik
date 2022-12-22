from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.model import Model

class SofistikModel(Model):
    """Sofistik implementation of :class:`compas_fea2.model.model.Model`.\n
    """
    __doc__ += Model.__doc__

    def __init__(self, *, name=None, description=None, author=None, **kwargs):
        super(SofistikModel, self).__init__(name=name, description=description, author=author, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


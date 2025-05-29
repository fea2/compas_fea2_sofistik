
from compas_fea2.model.parts import Part
from compas_fea2.model.parts import RigidPart

class SofistikPart(Part):
    """Sofistik implementation of :class:`compas_fea2.model.parts.Part`.\n
    """
    __doc__ += Part.__doc__

    def __init__(self, name=None, **kwargs):
        super(SofistikPart, self).__init__(name=name, **kwargs)

    def jobdata(self):
        """Generate the jobdata string
        """
        return """



""".format(
            "\n".join([node.jobdata() for node in self.nodes]),
            "\n".join([element.jobdata() for element in self.elements])
            )


class SofistikRigidPart(RigidPart):
    """Sofistik implementation of :class:`compas_fea2.model.parts.RigidPart`.\n
    """
    __doc__ += RigidPart.__doc__

    def __init__(self, reference_point=None, name=None, **kwargs):
        super(SofistikRigidPart, self).__init__(reference_point=reference_point, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


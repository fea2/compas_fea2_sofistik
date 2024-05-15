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

    def jobdata(self):
        return """
+PROG AQUA
$ PARTS

HEAD Materials and Sections
$ MATERIALS
{}
$ SECTIONS
{}
end

+prog sofimsha
HEAD Geometry
syst spac gdir negz gdiv 10000
$ NODES
{}
$ ELEMENTS
{}
$ CONNECTORS
{}
end

$ ICs
$ BCs
+prog sofimsha
head Constraints
syst rest
ctrl rest 2
{}

end
""".format(
        "\n".join([material.jobdata() for material in self.materials]),
        "\n".join([section.jobdata() for section in self.sections]),
        "\n".join([node.jobdata() for node in self.nodes]),
        "\n".join([element.jobdata() for element in self.elements]),
        "\n".join([connector.jobdata() for connector in self.connectors]),
        "\n".join([bc.jobdata(nodes) for bc, nodes in self.bcs.items()]),
           )



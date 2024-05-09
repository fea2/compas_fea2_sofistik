from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.materials.material import ElasticIsotropic
from compas_fea2.model.materials.material import ElasticOrthotropic
from compas_fea2.model.materials.material import ElasticPlastic
from compas_fea2.model.materials.material import Stiff
from compas_fea2.model.materials.material import UserMaterial


class SofistikElasticIsotropic(ElasticIsotropic):
    """Sofistik implementation of :class:`compas_fea2.model.materials.material.ElasticIsotropic`.\n
    """
    __doc__ += ElasticIsotropic.__doc__

    def __init__(self, *, E, v, density, expansion=None, name=None, **kwargs):
        super(SofistikElasticIsotropic, self).__init__(E=E, v=v, density=density, expansion=expansion, name=name, **kwargs)

    def jobdata(self):
        """Generates the common string information for the input file of the command
        'MAT - General Material Properties' defined in the SOFiSTiK programme module AQUA.

        Parameters
        ----------
        NO : ---
            Material number
        E : ---
            Elastic Modulus
        MUE : ---
            Poisson's ratio
        G : ---
            Shear modulus
        GAM : --
            Specif weigth
        ALFA : ---
            Thermal expansion coefficient
        Returns
        -------
        input file data line (str)
        """
        return "MAT NO {} {} {} {} {} {}".format(self.key+1,
                                                 "E {}".format(self.E) if self.E else "",
                                                 "MUE {}".format(self.v) if self.v else"",
                                                 "G {}".format(self.G) if self.G else "",
                                                 "GAM {}".format(self.density) if self.density else "",
                                                 "ALFA {}".format(self.expansion) if self.expansion else "")


class SofistikElasticOrthotropic(ElasticOrthotropic):
    """Sofistik implementation of :class:`compas_fea2.model.materials.material.ElasticOrthotropic`.\n
    """
    __doc__ += ElasticOrthotropic.__doc__

    def __init__(self, *, Ex, Ey, Ez, vxy, vyz, vzx, Gxy, Gyz, Gzx, density, expansion=None, name=None, **kwargs):
        super(SofistikElasticOrthotropic, self).__init__(Ex=Ex, Ey=Ey, Ez=Ez, vxy=vxy, vyz=vyz, vzx=vzx,
                                                         Gxy=Gxy, Gyz=Gyz, Gzx=Gzx, density=density, expansion=expansion, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikElasticPlastic(ElasticPlastic):
    """Sofistik implementation of :class:`compas_fea2.model.materials.material.ElasticPlastic`.\n
    """
    __doc__ += ElasticPlastic.__doc__

    def __init__(self, *, E, v, density, strain_stress, expansion=None, name=None, **kwargs):
        super(SofistikElasticPlastic, self).__init__(E=E, v=v, density=density, strain_stress=strain_stress, expansion=expansion, name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikStiff(Stiff):
    """Sofistik implementation of :class:`compas_fea2.model.materials.material.Stiff`.\n
    """
    __doc__ += Stiff.__doc__

    def __init__(self, name=None, **kwargs):
        super(SofistikStiff, self).__init__(name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError


class SofistikUserMaterial(UserMaterial):
    """Sofistik implementation of :class:`compas_fea2.model.materials.material.UserMaterial`.\n
    """
    __doc__ += UserMaterial.__doc__

    def __init__(self, name=None, **kwargs):
        super(SofistikUserMaterial, self).__init__(name=name, **kwargs)
        raise NotImplementedError

    def jobdata(self):
        raise NotImplementedError

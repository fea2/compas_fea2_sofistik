from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.sections import AngleSection
from compas_fea2.model.sections import BeamSection
from compas_fea2.model.sections import BoxSection
from compas_fea2.model.sections import CircularSection
from compas_fea2.model.sections import HexSection
from compas_fea2.model.sections import ISection
from compas_fea2.model.sections import MassSection
from compas_fea2.model.sections import MembraneSection
from compas_fea2.model.sections import PipeSection
from compas_fea2.model.sections import RectangularSection
from compas_fea2.model.sections import ShellSection
from compas_fea2.model.sections import SolidSection
from compas_fea2.model.sections import SpringSection
from compas_fea2.model.sections import StrutSection
from compas_fea2.model.sections import TieSection
from compas_fea2.model.sections import TrapezoidalSection
from compas_fea2.model.sections import TrussSection


class SofistikAngleSection(AngleSection):

    #FIXME: Double-check the orientation of the section in sofistik

    """Sofistik implementation of :class:`compas_fea2.model.sections.AngleSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += AngleSection.__doc__

    def __init__(self, w, h, t, material, name=None, **kwargs):
        super(SofistikAngleSection, self).__init__(w=w, h=h, t=t, material=material, name=name, **kwargs)

    def jobdata(self):
        string = "SECT NO {} TITL 'ANGLE-SECTION' MNO {}\n".format(self.key+1,
                                                        self.material.key+1)
        string += "POLY TYPE O\n"
        string += "VERT 1 {} {}\n".format(-self.w/2, -self.h/2)
        string += "VERT 2 {} {}\n".format(self.w/2, -self.h/2)
        string += "VERT 3 {} {}\n".format(self.w/2, -self.h/2 + self.t)
        string += "VERT 4 {} {}\n".format(-self.w/2 + self.t, - self.h/2 + self.t)
        string += "VERT 5 {} {}\n".format(-self.w/2 + self.t, self.h/2)
        string += "VERT 6 {} {}\n".format(-self.w/2, self.h/2)
        return string

class SofistikBeamSection(BeamSection):

    #FIXME: Discuss about concept of BeamSection

    """Sofistik implementation of :class:`compas_fea2.model.sections.BeamSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += BeamSection.__doc__

    def __init__(self, *, A, Ixx, Iyy, Ixy, Avx, Avy, J, g0, gw, material, name=None, **kwargs):
        super(SofistikBeamSection, self).__init__(A=A, Ixx=Ixx, Iyy=Iyy, Ixy=Ixy,
                                                  Avx=Avx, Avy=Avy, J=J, g0=g0, gw=gw, material=material, name=name, **kwargs)

    @property
    def jobdata(self):
        self._jobdata = "SVAL NO {} MNO {} A {} IZ {} IY {} IYZ {} AZ {} AY {} IT {} G0? {} GW? {}".format(self.key+1,
                                                                                                           self.material.key+1,
                                                                                                           self.A,
                                                                                                           self.Ixx,
                                                                                                           self.Iyy,
                                                                                                           self.Ixy,
                                                                                                           self.Avx,
                                                                                                           self.Avy,
                                                                                                           self.J,
                                                                                                           self.g0,
                                                                                                           self.gw)
        return self._jobdata



class SofistikBoxSection(BoxSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.BoxSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.
    To create hollow sections, material number 0 (MNO 0) is assigned to the inner polygon and the actual material to the outer polygon.
    Currently, it is assumed that the thickness of all four sides of the BoxSection is the same and equal to tw.

    """
    __doc__ += BoxSection.__doc__

    # TODO Since in the BoxSection is still needed the implementation of different thickness along the 4 sides,
    # here it is assumed that the 4 sides has the same thickness value tw

    def __init__(self, w, h, tw, tf, material, name=None, **kwargs):
        super(SofistikBoxSection, self).__init__(w=w, h=h, tw=tw, tf=tf, material=material, name=name, **kwargs)

    def jobdata(self):
        string = "SECT NO {} TITL 'BOX-SECTION' MNO {}\n".format(self.key+1,
                                                        self.material.key+1)
        string += "POLY TYPE O\n"

        string += "VERT 1  {} {}\n".format(-self.w/2, -self.h/2)
        string += "VERT 2  {} {}\n".format(self.w/2, -self.h/2)
        string += "VERT 3  {} {}\n".format(self.w/2, self.h/2)
        string += "VERT 4  {} {}\n".format(-self.w/2, self.h/2)

        string += "POLY TYPE O MNO 0\n"

        string += "VERT 5  {} {}\n".format(-self.w/2 + self.tw, -self.h/2 + self.tw)
        string += "VERT 6  {} {}\n".format(self.w/2 - self.tw, -self.h/2 + self.tw)
        string += "VERT 7  {} {}\n".format(self.w/2 - self.tw, self.h/2 - self.tw)
        string += "VERT 8  {} {}\n".format(-self.w/2 + self.tw, self.h/2 - self.tw)

        return string


class SofistikCircularSection(CircularSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.CircularSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.
    A Solid CircularSection in sofistik uses the SCIT command with thickess (T) equal to 0.0

    """
    __doc__ += CircularSection.__doc__

    def __init__(self, r, material, name=None, **kwargs):
        super(SofistikCircularSection, self).__init__(r=r, material=material, name=name, **kwargs)

    def jobdata(self):
        return "SCIT NO {} D {} T 0.0 MNO {}".format(self.key+1,
                                                        2*self.r,
                                                        self.material.key+1)


class SofistikHexSection(HexSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.HexSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += HexSection.__doc__

    def __init__(self, r, t, material, name=None, **kwargs):
        super(SofistikHexSection, self).__init__(r=r, t=t, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikISection(ISection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.ISection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += ISection.__doc__

    def __init__(self, w, h, tw, tf, material, name=None, **kwargs):
        super(SofistikISection, self).__init__(w=w, h=h, tw=tw, tf=tf, material=material, name=name, **kwargs)

    def jobdata(self):
        string = "SECT NO {} TITL 'I-SECTION' MNO {}\n".format(self.key+1,
                                                        self.material.key+1)
        string += "POLY TYPE O\n"

        string += "VERT 1  {} {}\n".format(-self.w/2,-self.h/2)
        string += "VERT 2  {} {}\n".format(self.w/2, -self.h/2)
        string += "VERT 3  {} {}\n".format(self.w/2, -self.h/2 + self.tf)
        string += "VERT 4  {} {}\n".format(self.tw/2, -self.h/2 + self.tf)
        string += "VERT 5  {} {}\n".format(self.tw/2, self.h/2 - self.tf)
        string += "VERT 6  {} {}\n".format(self.w/2, self.h/2 - self.tf)
        string += "VERT 7  {} {}\n".format(self.w/2, self.h/2)
        string += "VERT 8  {} {}\n".format(-self.w/2, self.h/2)
        string += "VERT 9  {} {}\n".format(-self.w/2, self.h/2 - self.tf)
        string += "VERT 10 {} {}\n".format(-self.tw/2, self.h/2 - self.tf)
        string += "VERT 11 {} {}\n".format(-self.tw/2, -self.h/2 + self.tf)
        string += "VERT 12 {} {}\n".format(-self.w/2, -self.h/2 + self.tf)

        return string

        # Other option is with the coordinate System with the 0,0 in the bottom left vertex
        # string += "VERT 1  {} {}\n".format(0, 0)
        # string += "VERT 2  {} {}\n".format(self.w, 0)
        # string += "VERT 3  {} {}\n".format(self.w, self.tf)
        # string += "VERT 4  {} {}\n".format(self.w/2 + self.tw/2, self.tf)
        # string += "VERT 5  {} {}\n".format(self.w/2 + self.tw/2, self.h - self.tf)
        # string += "VERT 6  {} {}\n".format(self.w, self.h - self.tf)
        # string += "VERT 7  {} {}\n".format(self.w, self.h)
        # string += "VERT 8  {} {}\n".format(0, self.h)
        # string += "VERT 9  {} {}\n".format(0, self.h - self.tf)
        # string += "VERT 10 {} {}\n".format(self.w/2 - self.tw/2, self.h - self.tf)
        # string += "VERT 11 {} {}\n".format(self.w/2 - self.tw/2, self.tf)
        # string += "VERT 12 {} {}\n".format(0, self.tf)


class SofistikMassSection(MassSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.MassSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += MassSection.__doc__

    def __init__(self, mass, name=None, **kwargs):
        super(SofistikMassSection, self).__init__(mass=mass, name=name, **kwargs)
        raise NotImplementedError


class SofistikMembraneSection(MembraneSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.MembraneSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += MembraneSection.__doc__

    def __init__(self, t, material, name=None, **kwargs):
        super(SofistikMembraneSection, self).__init__(t=t, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikPipeSection(PipeSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.PipeSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.
    A PipeSection in sofistik uses the SCIT command with thickess (T) not equal to 0.0

    """
    __doc__ += PipeSection.__doc__

    def __init__(self, r, t, material, name=None, **kwargs):
        super(SofistikPipeSection, self).__init__(r=r, t=t, material=material, name=name, **kwargs)

    def jobdata(self):
        return "SCIT NO {} D {} T {} MNO {}".format(self.key+1,
                                                        2*self.r,
                                                        self.t,
                                                        self.material.key+1)



class SofistikRectangularSection(RectangularSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.RectangularSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += RectangularSection.__doc__

    def __init__(self, w, h, material, name=None, **kwargs):
        super(SofistikRectangularSection, self).__init__(w=w, h=h, material=material, name=name, **kwargs)

    def jobdata(self):
        return "SREC NO {} H {} B {} MNO {}".format(self.key+1,
                                                    self.h,
                                                    self.w,
                                                    self.material.key+1)


class SofistikShellSection(ShellSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.ShellSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += ShellSection.__doc__

    def __init__(self, t, material, name=None, **kwargs):
        super(SofistikShellSection, self).__init__(t=t, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikSolidSection(SolidSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.SolidSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += SolidSection.__doc__

    def __init__(self, material, name=None, **kwargs):
        super(SofistikSolidSection, self).__init__(material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikSpringSection(SpringSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.SpringSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += SpringSection.__doc__

    def __init__(self, forces=None, displacements=None, stiffness=None, name=None, **kwargs):
        super(SofistikSpringSection, self).__init__(forces=forces,
                                                    displacements=displacements, stiffness=stiffness, name=name, **kwargs)
        raise NotImplementedError


class SofistikStrutSection(StrutSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.StrutSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += StrutSection.__doc__

    def __init__(self, A, material, name=None, **kwargs):
        super(SofistikStrutSection, self).__init__(A=A, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikTieSection(TieSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.TieSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += TieSection.__doc__

    def __init__(self, A, material, name=None, **kwargs):
        super(SofistikTieSection, self).__init__(A=A, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikTrapezoidalSection(TrapezoidalSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.TrapezoidalSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += TrapezoidalSection.__doc__

    def __init__(self, w1, w2, h, material, name=None, **kwargs):
        super(SofistikTrapezoidalSection, self).__init__(w1=w1, w2=w2, h=h, material=material, name=name, **kwargs)
        raise NotImplementedError


class SofistikTrussSection(TrussSection):
    """Sofistik implementation of :class:`compas_fea2.model.sections.TrussSection`.\n

    Note
    ----
    The section key in sofistik starts from 1.

    """
    __doc__ += TrussSection.__doc__

    def __init__(self, A, material, name=None, **kwargs):
        super(SofistikTrussSection, self).__init__(A=A, material=material, name=name, **kwargs)
        raise NotImplementedError



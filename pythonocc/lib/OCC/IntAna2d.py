# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _IntAna2d.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_IntAna2d', [dirname(__file__)])
        except ImportError:
            import _IntAna2d
            return _IntAna2d
        if fp is not None:
            try:
                _mod = imp.load_module('_IntAna2d', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _IntAna2d = swig_import_helper()
    del swig_import_helper
else:
    import _IntAna2d
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _IntAna2d.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_IntAna2d.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_IntAna2d.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_IntAna2d.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_IntAna2d.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_IntAna2d.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_IntAna2d.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_IntAna2d.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_IntAna2d.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_IntAna2d.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_IntAna2d.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_IntAna2d.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_IntAna2d.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_IntAna2d.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_IntAna2d.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_IntAna2d.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_IntAna2d.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _IntAna2d.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.gp
import OCC.Standard
def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass

class IntAna2d_AnaIntersection(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Empty constructor. IsDone returns False.

        :rtype: None

        * Intersection between two lines.

        :param L1:
        :type L1: gp_Lin2d
        :param L2:
        :type L2: gp_Lin2d
        :rtype: None

        * Intersection between two circles.

        :param C1:
        :type C1: gp_Circ2d
        :param C2:
        :type C2: gp_Circ2d
        :rtype: None

        * Intersection between a line and a circle.

        :param L:
        :type L: gp_Lin2d
        :param C:
        :type C: gp_Circ2d
        :rtype: None

        * Intersection between a line and a conic.

        :param L:
        :type L: gp_Lin2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between a circle and another conic.

        :param C:
        :type C: gp_Circ2d
        :param Co:
        :type Co: IntAna2d_Conic &
        :rtype: None

        * Intersection between an ellipse and another conic.

        :param E:
        :type E: gp_Elips2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between a parabola and another conic.

        :param P:
        :type P: gp_Parab2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between an hyperbola and another conic.

        :param H:
        :type H: gp_Hypr2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        """
        _IntAna2d.IntAna2d_AnaIntersection_swiginit(self,_IntAna2d.new_IntAna2d_AnaIntersection(*args))
    def Perform(self, *args):
        """
        * Intersection between two lines.

        :param L1:
        :type L1: gp_Lin2d
        :param L2:
        :type L2: gp_Lin2d
        :rtype: None

        * Intersection between two circles.

        :param C1:
        :type C1: gp_Circ2d
        :param C2:
        :type C2: gp_Circ2d
        :rtype: None

        * Intersection between a line and a circle.

        :param L:
        :type L: gp_Lin2d
        :param C:
        :type C: gp_Circ2d
        :rtype: None

        * Intersection between a line and a conic.

        :param L:
        :type L: gp_Lin2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between a circle and another conic.

        :param C:
        :type C: gp_Circ2d
        :param Co:
        :type Co: IntAna2d_Conic &
        :rtype: None

        * Intersection between an ellipse and another conic.

        :param E:
        :type E: gp_Elips2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between a parabola and another conic.

        :param P:
        :type P: gp_Parab2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        * Intersection between an hyperbola and another conic.

        :param H:
        :type H: gp_Hypr2d
        :param C:
        :type C: IntAna2d_Conic &
        :rtype: None

        """
        return _IntAna2d.IntAna2d_AnaIntersection_Perform(self, *args)

    def IsDone(self, *args):
        """
        * Returns True if the computation was succesfull.

        :rtype: bool

        """
        return _IntAna2d.IntAna2d_AnaIntersection_IsDone(self, *args)

    def IsEmpty(self, *args):
        """
        * Returns True when there is no intersection, i-e - no intersection point - the elements are not identical. The element may be parallel in this case.

        :rtype: bool

        """
        return _IntAna2d.IntAna2d_AnaIntersection_IsEmpty(self, *args)

    def IdenticalElements(self, *args):
        """
        * For the intersection between an element of gp and a conic known by an implicit equation, the result will be True if the element of gp verifies the implicit equation. For the intersection between two Lin2d or two Circ2d, the result will be True if the elements are identical. The function returns False in all the other cases.

        :rtype: bool

        """
        return _IntAna2d.IntAna2d_AnaIntersection_IdenticalElements(self, *args)

    def ParallelElements(self, *args):
        """
        * For the intersection between two Lin2d or two Circ2d, the function returns True if the elements are parallel. The function returns False in all the other cases.

        :rtype: bool

        """
        return _IntAna2d.IntAna2d_AnaIntersection_ParallelElements(self, *args)

    def NbPoints(self, *args):
        """
        * returns the number of IntPoint between the 2 curves.

        :rtype: int

        """
        return _IntAna2d.IntAna2d_AnaIntersection_NbPoints(self, *args)

    def Point(self, *args):
        """
        * returns the intersection point of range N; If (N<=0) or (N>NbPoints), an exception is raised.

        :param N:
        :type N: int
        :rtype: IntAna2d_IntPoint

        """
        return _IntAna2d.IntAna2d_AnaIntersection_Point(self, *args)

    __swig_destroy__ = _IntAna2d.delete_IntAna2d_AnaIntersection
IntAna2d_AnaIntersection.Perform = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_Perform,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.IsDone = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_IsDone,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.IsEmpty = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_IsEmpty,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.IdenticalElements = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_IdenticalElements,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.ParallelElements = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_ParallelElements,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.NbPoints = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_NbPoints,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection.Point = new_instancemethod(_IntAna2d.IntAna2d_AnaIntersection_Point,None,IntAna2d_AnaIntersection)
IntAna2d_AnaIntersection_swigregister = _IntAna2d.IntAna2d_AnaIntersection_swigregister
IntAna2d_AnaIntersection_swigregister(IntAna2d_AnaIntersection)

class IntAna2d_Conic(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param C:
        :type C: gp_Circ2d
        :rtype: None

        :param C:
        :type C: gp_Lin2d
        :rtype: None

        :param C:
        :type C: gp_Parab2d
        :rtype: None

        :param C:
        :type C: gp_Hypr2d
        :rtype: None

        :param C:
        :type C: gp_Elips2d
        :rtype: None

        """
        _IntAna2d.IntAna2d_Conic_swiginit(self,_IntAna2d.new_IntAna2d_Conic(*args))
    def Value(self, *args):
        """
        * value of the function F at the point X,Y.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :rtype: float

        """
        return _IntAna2d.IntAna2d_Conic_Value(self, *args)

    def Grad(self, *args):
        """
        * returns the value of the gradient of F at the point X,Y.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :rtype: gp_XY

        """
        return _IntAna2d.IntAna2d_Conic_Grad(self, *args)

    def ValAndGrad(self, *args):
        """
        * Returns the value of the function and its gradient at the point X,Y.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :param Val:
        :type Val: float &
        :param Grd:
        :type Grd: gp_XY
        :rtype: None

        """
        return _IntAna2d.IntAna2d_Conic_ValAndGrad(self, *args)

    def Coefficients(self, *args):
        """
        * returns the coefficients of the polynomial equation wich defines the conic: A.X**2 + B.Y**2 + 2.C.X*Y + 2.D.X + 2.E.Y + F = 0.

        :param A:
        :type A: float &
        :param B:
        :type B: float &
        :param C:
        :type C: float &
        :param D:
        :type D: float &
        :param E:
        :type E: float &
        :param F:
        :type F: float &
        :rtype: None

        """
        return _IntAna2d.IntAna2d_Conic_Coefficients(self, *args)

    def NewCoefficients(self, *args):
        """
        * Returns the coefficients of the polynomial equation ( written in the natural coordinates system ) A x x + B y y + 2 C x y + 2 D x + 2 E y + F in the local coordinates system defined by Axis

        :param A:
        :type A: float &
        :param B:
        :type B: float &
        :param C:
        :type C: float &
        :param D:
        :type D: float &
        :param E:
        :type E: float &
        :param F:
        :type F: float &
        :param Axis:
        :type Axis: gp_Ax2d
        :rtype: None

        """
        return _IntAna2d.IntAna2d_Conic_NewCoefficients(self, *args)

    __swig_destroy__ = _IntAna2d.delete_IntAna2d_Conic
IntAna2d_Conic.Value = new_instancemethod(_IntAna2d.IntAna2d_Conic_Value,None,IntAna2d_Conic)
IntAna2d_Conic.Grad = new_instancemethod(_IntAna2d.IntAna2d_Conic_Grad,None,IntAna2d_Conic)
IntAna2d_Conic.ValAndGrad = new_instancemethod(_IntAna2d.IntAna2d_Conic_ValAndGrad,None,IntAna2d_Conic)
IntAna2d_Conic.Coefficients = new_instancemethod(_IntAna2d.IntAna2d_Conic_Coefficients,None,IntAna2d_Conic)
IntAna2d_Conic.NewCoefficients = new_instancemethod(_IntAna2d.IntAna2d_Conic_NewCoefficients,None,IntAna2d_Conic)
IntAna2d_Conic_swigregister = _IntAna2d.IntAna2d_Conic_swigregister
IntAna2d_Conic_swigregister(IntAna2d_Conic)

class IntAna2d_IntPoint(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Create an intersection point between 2 parametric 2d lines. X,Y are the coordinate of the point. U1 is the parameter on the first element, U2 the parameter on the second one.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :param U1:
        :type U1: float
        :param U2:
        :type U2: float
        :rtype: None

        * Create an intersection point between a parametric 2d line, and a line given by an implicit equation (ImplicitCurve). X,Y are the coordinate of the point. U1 is the parameter on the parametric element. Empty constructor. It's necessary to use one of the SetValue method after this one.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :param U1:
        :type U1: float
        :rtype: None

        :rtype: None

        """
        _IntAna2d.IntAna2d_IntPoint_swiginit(self,_IntAna2d.new_IntAna2d_IntPoint(*args))
    def SetValue(self, *args):
        """
        * Set the values for a 'non-implicit' point.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :param U1:
        :type U1: float
        :param U2:
        :type U2: float
        :rtype: void

        * Set the values for an 'implicit' point.

        :param X:
        :type X: float
        :param Y:
        :type Y: float
        :param U1:
        :type U1: float
        :rtype: void

        """
        return _IntAna2d.IntAna2d_IntPoint_SetValue(self, *args)

    def Value(self, *args):
        """
        * Returns the geometric point.

        :rtype: gp_Pnt2d

        """
        return _IntAna2d.IntAna2d_IntPoint_Value(self, *args)

    def SecondIsImplicit(self, *args):
        """
        * Returns True if the second curve is implicit.

        :rtype: bool

        """
        return _IntAna2d.IntAna2d_IntPoint_SecondIsImplicit(self, *args)

    def ParamOnFirst(self, *args):
        """
        * Returns the parameter on the first element.

        :rtype: float

        """
        return _IntAna2d.IntAna2d_IntPoint_ParamOnFirst(self, *args)

    def ParamOnSecond(self, *args):
        """
        * Returns the parameter on the second element. If the second element is an implicit curve, an exception is raised.

        :rtype: float

        """
        return _IntAna2d.IntAna2d_IntPoint_ParamOnSecond(self, *args)

    def _CSFDB_GetIntAna2d_IntPointmyu1(self, *args):
        """
        :rtype: float

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyu1(self, *args)

    def _CSFDB_SetIntAna2d_IntPointmyu1(self, *args):
        """
        :param p:
        :type p: float
        :rtype: None

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyu1(self, *args)

    def _CSFDB_GetIntAna2d_IntPointmyu2(self, *args):
        """
        :rtype: float

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyu2(self, *args)

    def _CSFDB_SetIntAna2d_IntPointmyu2(self, *args):
        """
        :param p:
        :type p: float
        :rtype: None

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyu2(self, *args)

    def _CSFDB_GetIntAna2d_IntPointmyp(self, *args):
        """
        :rtype: gp_Pnt2d

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyp(self, *args)

    def _CSFDB_GetIntAna2d_IntPointmyimplicit(self, *args):
        """
        :rtype: bool

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyimplicit(self, *args)

    def _CSFDB_SetIntAna2d_IntPointmyimplicit(self, *args):
        """
        :param p:
        :type p: bool
        :rtype: None

        """
        return _IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyimplicit(self, *args)

    __swig_destroy__ = _IntAna2d.delete_IntAna2d_IntPoint
IntAna2d_IntPoint.SetValue = new_instancemethod(_IntAna2d.IntAna2d_IntPoint_SetValue,None,IntAna2d_IntPoint)
IntAna2d_IntPoint.Value = new_instancemethod(_IntAna2d.IntAna2d_IntPoint_Value,None,IntAna2d_IntPoint)
IntAna2d_IntPoint.SecondIsImplicit = new_instancemethod(_IntAna2d.IntAna2d_IntPoint_SecondIsImplicit,None,IntAna2d_IntPoint)
IntAna2d_IntPoint.ParamOnFirst = new_instancemethod(_IntAna2d.IntAna2d_IntPoint_ParamOnFirst,None,IntAna2d_IntPoint)
IntAna2d_IntPoint.ParamOnSecond = new_instancemethod(_IntAna2d.IntAna2d_IntPoint_ParamOnSecond,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_GetIntAna2d_IntPointmyu1 = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyu1,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_SetIntAna2d_IntPointmyu1 = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyu1,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_GetIntAna2d_IntPointmyu2 = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyu2,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_SetIntAna2d_IntPointmyu2 = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyu2,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_GetIntAna2d_IntPointmyp = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyp,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_GetIntAna2d_IntPointmyimplicit = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_GetIntAna2d_IntPointmyimplicit,None,IntAna2d_IntPoint)
IntAna2d_IntPoint._CSFDB_SetIntAna2d_IntPointmyimplicit = new_instancemethod(_IntAna2d.IntAna2d_IntPoint__CSFDB_SetIntAna2d_IntPointmyimplicit,None,IntAna2d_IntPoint)
IntAna2d_IntPoint_swigregister = _IntAna2d.IntAna2d_IntPoint_swigregister
IntAna2d_IntPoint_swigregister(IntAna2d_IntPoint)




# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _Hermit.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Hermit', [dirname(__file__)])
        except ImportError:
            import _Hermit
            return _Hermit
        if fp is not None:
            try:
                _mod = imp.load_module('_Hermit', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Hermit = swig_import_helper()
    del swig_import_helper
else:
    import _Hermit
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
    __swig_destroy__ = _Hermit.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_Hermit.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Hermit.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Hermit.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Hermit.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Hermit.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Hermit.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Hermit.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Hermit.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Hermit.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Hermit.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Hermit.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Hermit.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Hermit.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Hermit.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Hermit.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Hermit.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _Hermit.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Geom
import OCC.MMgt
import OCC.Standard
import OCC.gp
import OCC.TCollection
import OCC.GeomAbs
import OCC.TColgp
import OCC.TColStd
import OCC.Geom2d
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

class hermit(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def Solution(*args):
        """
        * //!returns the correct spline a(u) which will  be multiplicated with BS later.

        :param BS:
        :type BS: Handle_Geom_BSplineCurve &
        :param TolPoles: default value is 0.000001
        :type TolPoles: float
        :param TolKnots: default value is 0.000001
        :type TolKnots: float
        :rtype: Handle_Geom2d_BSplineCurve

        * //!returns the correct spline a(u) which will  be multiplicated with BS later.

        :param BS:
        :type BS: Handle_Geom2d_BSplineCurve &
        :param TolPoles: default value is 0.000001
        :type TolPoles: float
        :param TolKnots: default value is 0.000001
        :type TolKnots: float
        :rtype: Handle_Geom2d_BSplineCurve

        """
        return _Hermit.hermit_Solution(*args)

    Solution = staticmethod(Solution)
    def Solutionbis(*args):
        """
        * //!returns the knots to insert to a(u) to  stay with a constant sign and in the  tolerances.

        :param BS:
        :type BS: Handle_Geom_BSplineCurve &
        :param Knotmin:
        :type Knotmin: float &
        :param Knotmax:
        :type Knotmax: float &
        :param TolPoles: default value is 0.000001
        :type TolPoles: float
        :param TolKnots: default value is 0.000001
        :type TolKnots: float
        :rtype: void

        """
        return _Hermit.hermit_Solutionbis(*args)

    Solutionbis = staticmethod(Solutionbis)
    def __init__(self): 
        _Hermit.hermit_swiginit(self,_Hermit.new_hermit())
    __swig_destroy__ = _Hermit.delete_hermit
hermit_swigregister = _Hermit.hermit_swigregister
hermit_swigregister(hermit)

def hermit_Solution(*args):
  """
    * //!returns the correct spline a(u) which will  be multiplicated with BS later.

    :param BS:
    :type BS: Handle_Geom_BSplineCurve &
    :param TolPoles: default value is 0.000001
    :type TolPoles: float
    :param TolKnots: default value is 0.000001
    :type TolKnots: float
    :rtype: Handle_Geom2d_BSplineCurve

    * //!returns the correct spline a(u) which will  be multiplicated with BS later.

    :param BS:
    :type BS: Handle_Geom2d_BSplineCurve &
    :param TolPoles: default value is 0.000001
    :type TolPoles: float
    :param TolKnots: default value is 0.000001
    :type TolKnots: float
    :rtype: Handle_Geom2d_BSplineCurve

    """
  return _Hermit.hermit_Solution(*args)

def hermit_Solutionbis(*args):
  """
    * //!returns the knots to insert to a(u) to  stay with a constant sign and in the  tolerances.

    :param BS:
    :type BS: Handle_Geom_BSplineCurve &
    :param Knotmin:
    :type Knotmin: float &
    :param Knotmax:
    :type Knotmax: float &
    :param TolPoles: default value is 0.000001
    :type TolPoles: float
    :param TolKnots: default value is 0.000001
    :type TolKnots: float
    :rtype: void

    """
  return _Hermit.hermit_Solutionbis(*args)




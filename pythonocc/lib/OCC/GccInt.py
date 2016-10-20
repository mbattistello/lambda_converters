# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _GccInt.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_GccInt', [dirname(__file__)])
        except ImportError:
            import _GccInt
            return _GccInt
        if fp is not None:
            try:
                _mod = imp.load_module('_GccInt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _GccInt = swig_import_helper()
    del swig_import_helper
else:
    import _GccInt
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
    __swig_destroy__ = _GccInt.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_GccInt.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_GccInt.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_GccInt.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_GccInt.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_GccInt.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_GccInt.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_GccInt.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_GccInt.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_GccInt.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_GccInt.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_GccInt.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_GccInt.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_GccInt.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_GccInt.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_GccInt.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_GccInt.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _GccInt.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.MMgt
import OCC.Standard
import OCC.gp
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

GccInt_Lin = _GccInt.GccInt_Lin
GccInt_Cir = _GccInt.GccInt_Cir
GccInt_Ell = _GccInt.GccInt_Ell
GccInt_Par = _GccInt.GccInt_Par
GccInt_Hpr = _GccInt.GccInt_Hpr
GccInt_Pnt = _GccInt.GccInt_Pnt
class GccInt_Bisec(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def ArcType(self, *args):
        """
        * Returns the type of bisecting object (line, circle, parabola, hyperbola, ellipse, point).

        :rtype: GccInt_IType

        """
        return _GccInt.GccInt_Bisec_ArcType(self, *args)

    def Point(self, *args):
        """
        * Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.

        :rtype: gp_Pnt2d

        """
        return _GccInt.GccInt_Bisec_Point(self, *args)

    def Line(self, *args):
        """
        * Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.

        :rtype: gp_Lin2d

        """
        return _GccInt.GccInt_Bisec_Line(self, *args)

    def Circle(self, *args):
        """
        * Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.

        :rtype: gp_Circ2d

        """
        return _GccInt.GccInt_Bisec_Circle(self, *args)

    def Hyperbola(self, *args):
        """
        * Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.

        :rtype: gp_Hypr2d

        """
        return _GccInt.GccInt_Bisec_Hyperbola(self, *args)

    def Parabola(self, *args):
        """
        * Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.

        :rtype: gp_Parab2d

        """
        return _GccInt.GccInt_Bisec_Parabola(self, *args)

    def Ellipse(self, *args):
        """
        * Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.

        :rtype: gp_Elips2d

        """
        return _GccInt.GccInt_Bisec_Ellipse(self, *args)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_Bisec(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_Bisec
GccInt_Bisec.ArcType = new_instancemethod(_GccInt.GccInt_Bisec_ArcType,None,GccInt_Bisec)
GccInt_Bisec.Point = new_instancemethod(_GccInt.GccInt_Bisec_Point,None,GccInt_Bisec)
GccInt_Bisec.Line = new_instancemethod(_GccInt.GccInt_Bisec_Line,None,GccInt_Bisec)
GccInt_Bisec.Circle = new_instancemethod(_GccInt.GccInt_Bisec_Circle,None,GccInt_Bisec)
GccInt_Bisec.Hyperbola = new_instancemethod(_GccInt.GccInt_Bisec_Hyperbola,None,GccInt_Bisec)
GccInt_Bisec.Parabola = new_instancemethod(_GccInt.GccInt_Bisec_Parabola,None,GccInt_Bisec)
GccInt_Bisec.Ellipse = new_instancemethod(_GccInt.GccInt_Bisec_Ellipse,None,GccInt_Bisec)
GccInt_Bisec_swigregister = _GccInt.GccInt_Bisec_swigregister
GccInt_Bisec_swigregister(GccInt_Bisec)

class Handle_GccInt_Bisec(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_Bisec_swiginit(self,_GccInt.new_Handle_GccInt_Bisec(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_Bisec_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_Bisec
Handle_GccInt_Bisec.Nullify = new_instancemethod(_GccInt.Handle_GccInt_Bisec_Nullify,None,Handle_GccInt_Bisec)
Handle_GccInt_Bisec.IsNull = new_instancemethod(_GccInt.Handle_GccInt_Bisec_IsNull,None,Handle_GccInt_Bisec)
Handle_GccInt_Bisec.GetObject = new_instancemethod(_GccInt.Handle_GccInt_Bisec_GetObject,None,Handle_GccInt_Bisec)
Handle_GccInt_Bisec_swigregister = _GccInt.Handle_GccInt_Bisec_swigregister
Handle_GccInt_Bisec_swigregister(Handle_GccInt_Bisec)

def Handle_GccInt_Bisec_DownCast(*args):
  return _GccInt.Handle_GccInt_Bisec_DownCast(*args)
Handle_GccInt_Bisec_DownCast = _GccInt.Handle_GccInt_Bisec_DownCast

class GccInt_BCirc(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting curve whose geometry is the 2D circle Circ.

        :param Circ:
        :type Circ: gp_Circ2d
        :rtype: None

        """
        _GccInt.GccInt_BCirc_swiginit(self,_GccInt.new_GccInt_BCirc(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BCirc(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BCirc
GccInt_BCirc_swigregister = _GccInt.GccInt_BCirc_swigregister
GccInt_BCirc_swigregister(GccInt_BCirc)

class Handle_GccInt_BCirc(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BCirc_swiginit(self,_GccInt.new_Handle_GccInt_BCirc(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BCirc_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BCirc
Handle_GccInt_BCirc.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BCirc_Nullify,None,Handle_GccInt_BCirc)
Handle_GccInt_BCirc.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BCirc_IsNull,None,Handle_GccInt_BCirc)
Handle_GccInt_BCirc.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BCirc_GetObject,None,Handle_GccInt_BCirc)
Handle_GccInt_BCirc_swigregister = _GccInt.Handle_GccInt_BCirc_swigregister
Handle_GccInt_BCirc_swigregister(Handle_GccInt_BCirc)

def Handle_GccInt_BCirc_DownCast(*args):
  return _GccInt.Handle_GccInt_BCirc_DownCast(*args)
Handle_GccInt_BCirc_DownCast = _GccInt.Handle_GccInt_BCirc_DownCast

class GccInt_BElips(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting curve whose geometry is the 2D ellipse Ellipse.

        :param Ellipse:
        :type Ellipse: gp_Elips2d
        :rtype: None

        """
        _GccInt.GccInt_BElips_swiginit(self,_GccInt.new_GccInt_BElips(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BElips(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BElips
GccInt_BElips_swigregister = _GccInt.GccInt_BElips_swigregister
GccInt_BElips_swigregister(GccInt_BElips)

class Handle_GccInt_BElips(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BElips_swiginit(self,_GccInt.new_Handle_GccInt_BElips(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BElips_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BElips
Handle_GccInt_BElips.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BElips_Nullify,None,Handle_GccInt_BElips)
Handle_GccInt_BElips.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BElips_IsNull,None,Handle_GccInt_BElips)
Handle_GccInt_BElips.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BElips_GetObject,None,Handle_GccInt_BElips)
Handle_GccInt_BElips_swigregister = _GccInt.Handle_GccInt_BElips_swigregister
Handle_GccInt_BElips_swigregister(Handle_GccInt_BElips)

def Handle_GccInt_BElips_DownCast(*args):
  return _GccInt.Handle_GccInt_BElips_DownCast(*args)
Handle_GccInt_BElips_DownCast = _GccInt.Handle_GccInt_BElips_DownCast

class GccInt_BHyper(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting curve whose geometry is the 2D hyperbola Hyper.

        :param Hyper:
        :type Hyper: gp_Hypr2d
        :rtype: None

        """
        _GccInt.GccInt_BHyper_swiginit(self,_GccInt.new_GccInt_BHyper(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BHyper(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BHyper
GccInt_BHyper_swigregister = _GccInt.GccInt_BHyper_swigregister
GccInt_BHyper_swigregister(GccInt_BHyper)

class Handle_GccInt_BHyper(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BHyper_swiginit(self,_GccInt.new_Handle_GccInt_BHyper(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BHyper_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BHyper
Handle_GccInt_BHyper.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BHyper_Nullify,None,Handle_GccInt_BHyper)
Handle_GccInt_BHyper.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BHyper_IsNull,None,Handle_GccInt_BHyper)
Handle_GccInt_BHyper.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BHyper_GetObject,None,Handle_GccInt_BHyper)
Handle_GccInt_BHyper_swigregister = _GccInt.Handle_GccInt_BHyper_swigregister
Handle_GccInt_BHyper_swigregister(Handle_GccInt_BHyper)

def Handle_GccInt_BHyper_DownCast(*args):
  return _GccInt.Handle_GccInt_BHyper_DownCast(*args)
Handle_GccInt_BHyper_DownCast = _GccInt.Handle_GccInt_BHyper_DownCast

class GccInt_BLine(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting line whose geometry is the 2D line Line.

        :param Line:
        :type Line: gp_Lin2d
        :rtype: None

        """
        _GccInt.GccInt_BLine_swiginit(self,_GccInt.new_GccInt_BLine(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BLine(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BLine
GccInt_BLine_swigregister = _GccInt.GccInt_BLine_swigregister
GccInt_BLine_swigregister(GccInt_BLine)

class Handle_GccInt_BLine(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BLine_swiginit(self,_GccInt.new_Handle_GccInt_BLine(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BLine_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BLine
Handle_GccInt_BLine.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BLine_Nullify,None,Handle_GccInt_BLine)
Handle_GccInt_BLine.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BLine_IsNull,None,Handle_GccInt_BLine)
Handle_GccInt_BLine.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BLine_GetObject,None,Handle_GccInt_BLine)
Handle_GccInt_BLine_swigregister = _GccInt.Handle_GccInt_BLine_swigregister
Handle_GccInt_BLine_swigregister(Handle_GccInt_BLine)

def Handle_GccInt_BLine_DownCast(*args):
  return _GccInt.Handle_GccInt_BLine_DownCast(*args)
Handle_GccInt_BLine_DownCast = _GccInt.Handle_GccInt_BLine_DownCast

class GccInt_BParab(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting curve whose geometry is the 2D parabola Parab.

        :param Parab:
        :type Parab: gp_Parab2d
        :rtype: None

        """
        _GccInt.GccInt_BParab_swiginit(self,_GccInt.new_GccInt_BParab(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BParab(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BParab
GccInt_BParab_swigregister = _GccInt.GccInt_BParab_swigregister
GccInt_BParab_swigregister(GccInt_BParab)

class Handle_GccInt_BParab(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BParab_swiginit(self,_GccInt.new_Handle_GccInt_BParab(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BParab_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BParab
Handle_GccInt_BParab.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BParab_Nullify,None,Handle_GccInt_BParab)
Handle_GccInt_BParab.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BParab_IsNull,None,Handle_GccInt_BParab)
Handle_GccInt_BParab.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BParab_GetObject,None,Handle_GccInt_BParab)
Handle_GccInt_BParab_swigregister = _GccInt.Handle_GccInt_BParab_swigregister
Handle_GccInt_BParab_swigregister(Handle_GccInt_BParab)

def Handle_GccInt_BParab_DownCast(*args):
  return _GccInt.Handle_GccInt_BParab_DownCast(*args)
Handle_GccInt_BParab_DownCast = _GccInt.Handle_GccInt_BParab_DownCast

class GccInt_BPoint(GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs a bisecting object whose geometry is the 2D point Point.

        :param Point:
        :type Point: gp_Pnt2d
        :rtype: None

        """
        _GccInt.GccInt_BPoint_swiginit(self,_GccInt.new_GccInt_BPoint(*args))
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GccInt_BPoint(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _GccInt.delete_GccInt_BPoint
GccInt_BPoint_swigregister = _GccInt.GccInt_BPoint_swigregister
GccInt_BPoint_swigregister(GccInt_BPoint)

class Handle_GccInt_BPoint(Handle_GccInt_Bisec):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _GccInt.Handle_GccInt_BPoint_swiginit(self,_GccInt.new_Handle_GccInt_BPoint(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GccInt.Handle_GccInt_BPoint_DownCast)
    __swig_destroy__ = _GccInt.delete_Handle_GccInt_BPoint
Handle_GccInt_BPoint.Nullify = new_instancemethod(_GccInt.Handle_GccInt_BPoint_Nullify,None,Handle_GccInt_BPoint)
Handle_GccInt_BPoint.IsNull = new_instancemethod(_GccInt.Handle_GccInt_BPoint_IsNull,None,Handle_GccInt_BPoint)
Handle_GccInt_BPoint.GetObject = new_instancemethod(_GccInt.Handle_GccInt_BPoint_GetObject,None,Handle_GccInt_BPoint)
Handle_GccInt_BPoint_swigregister = _GccInt.Handle_GccInt_BPoint_swigregister
Handle_GccInt_BPoint_swigregister(Handle_GccInt_BPoint)

def Handle_GccInt_BPoint_DownCast(*args):
  return _GccInt.Handle_GccInt_BPoint_DownCast(*args)
Handle_GccInt_BPoint_DownCast = _GccInt.Handle_GccInt_BPoint_DownCast




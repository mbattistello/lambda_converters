# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _Hatch.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Hatch', [dirname(__file__)])
        except ImportError:
            import _Hatch
            return _Hatch
        if fp is not None:
            try:
                _mod = imp.load_module('_Hatch', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Hatch = swig_import_helper()
    del swig_import_helper
else:
    import _Hatch
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
    __swig_destroy__ = _Hatch.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_Hatch.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Hatch.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Hatch.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Hatch.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Hatch.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Hatch.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Hatch.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Hatch.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Hatch.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Hatch.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Hatch.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Hatch.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Hatch.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Hatch.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Hatch.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Hatch.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _Hatch.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.gp
import OCC.TCollection
import OCC.MMgt
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

Hatch_XLINE = _Hatch.Hatch_XLINE
Hatch_YLINE = _Hatch.Hatch_YLINE
Hatch_ANYLINE = _Hatch.Hatch_ANYLINE
class Hatch_Hatcher(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Returns a empty hatcher. <Tol> is the tolerance for intersections.

        :param Tol:
        :type Tol: float
        :param Oriented: default value is Standard_True
        :type Oriented: bool
        :rtype: None

        """
        _Hatch.Hatch_Hatcher_swiginit(self,_Hatch.new_Hatch_Hatcher(*args))
    def Tolerance(self, *args):
        """
        :param Tol:
        :type Tol: float
        :rtype: None

        :rtype: float

        """
        return _Hatch.Hatch_Hatcher_Tolerance(self, *args)

    def AddLine(self, *args):
        """
        * Add a line <L> to be trimmed. <T> the type is only kept from information. It is not used in the computation.

        :param L:
        :type L: gp_Lin2d
        :param T: default value is Hatch_ANYLINE
        :type T: Hatch_LineForm
        :rtype: None

        * Add an infinite line on direction <D> at distance <Dist> from the origin to be trimmed. <Dist> may be negative.  If O is the origin of the 2D plane, and V the vector perpendicular to D (in the direct direction).  A point P is on the line if :  OP dot V = Dist The parameter of P on the line is  OP dot D

        :param D:
        :type D: gp_Dir2d
        :param Dist:
        :type Dist: float
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_AddLine(self, *args)

    def AddXLine(self, *args):
        """
        * Add an infinite line parallel to the Y-axis at abciss <X>.

        :param X:
        :type X: float
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_AddXLine(self, *args)

    def AddYLine(self, *args):
        """
        * Add an infinite line parallel to the X-axis at ordinate <Y>.

        :param Y:
        :type Y: float
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_AddYLine(self, *args)

    def Trim(self, *args):
        """
        * Trims the lines at intersections with <L>.

        :param L:
        :type L: gp_Lin2d
        :param Index: default value is 0
        :type Index: int
        :rtype: None

        * Trims the lines at intersections with <L> in the parameter range <Start>, <End>

        :param L:
        :type L: gp_Lin2d
        :param Start:
        :type Start: float
        :param End:
        :type End: float
        :param Index: default value is 0
        :type Index: int
        :rtype: None

        * Trims the line at intersection with the oriented segment P1,P2.

        :param P1:
        :type P1: gp_Pnt2d
        :param P2:
        :type P2: gp_Pnt2d
        :param Index: default value is 0
        :type Index: int
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_Trim(self, *args)

    def NbLines(self, *args):
        """
        * Returns the number of lines.

        :rtype: int

        """
        return _Hatch.Hatch_Hatcher_NbLines(self, *args)

    def Line(self, *args):
        """
        * Returns the line of index <I>.

        :param I:
        :type I: int
        :rtype: gp_Lin2d

        """
        return _Hatch.Hatch_Hatcher_Line(self, *args)

    def LineForm(self, *args):
        """
        * Returns the type of the line of index <I>.

        :param I:
        :type I: int
        :rtype: Hatch_LineForm

        """
        return _Hatch.Hatch_Hatcher_LineForm(self, *args)

    def IsXLine(self, *args):
        """
        * Returns True if the line of index <I> has a constant X value.

        :param I:
        :type I: int
        :rtype: bool

        """
        return _Hatch.Hatch_Hatcher_IsXLine(self, *args)

    def IsYLine(self, *args):
        """
        * Returns True if the line of index <I> has a constant Y value.

        :param I:
        :type I: int
        :rtype: bool

        """
        return _Hatch.Hatch_Hatcher_IsYLine(self, *args)

    def Coordinate(self, *args):
        """
        * Returns the X or Y coordinate of the line of index <I> if it is a X or a Y line.

        :param I:
        :type I: int
        :rtype: float

        """
        return _Hatch.Hatch_Hatcher_Coordinate(self, *args)

    def NbIntervals(self, *args):
        """
        * Returns the total number of intervals on all the lines.

        :rtype: int

        * Returns the number of intervals on line of index <I>.

        :param I:
        :type I: int
        :rtype: int

        """
        return _Hatch.Hatch_Hatcher_NbIntervals(self, *args)

    def Start(self, *args):
        """
        * Returns the first parameter of interval <J> on line <I>.

        :param I:
        :type I: int
        :param J:
        :type J: int
        :rtype: float

        """
        return _Hatch.Hatch_Hatcher_Start(self, *args)

    def StartIndex(self, *args):
        """
        * Returns the first Index and Par2 of interval <J> on line <I>.

        :param I:
        :type I: int
        :param J:
        :type J: int
        :param Index:
        :type Index: int &
        :param Par2:
        :type Par2: float &
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_StartIndex(self, *args)

    def End(self, *args):
        """
        * Returns the last parameter of interval <J> on line <I>.

        :param I:
        :type I: int
        :param J:
        :type J: int
        :rtype: float

        """
        return _Hatch.Hatch_Hatcher_End(self, *args)

    def EndIndex(self, *args):
        """
        * Returns the last Index and Par2 of interval <J> on line <I>.

        :param I:
        :type I: int
        :param J:
        :type J: int
        :param Index:
        :type Index: int &
        :param Par2:
        :type Par2: float &
        :rtype: None

        """
        return _Hatch.Hatch_Hatcher_EndIndex(self, *args)

    __swig_destroy__ = _Hatch.delete_Hatch_Hatcher
Hatch_Hatcher.Tolerance = new_instancemethod(_Hatch.Hatch_Hatcher_Tolerance,None,Hatch_Hatcher)
Hatch_Hatcher.AddLine = new_instancemethod(_Hatch.Hatch_Hatcher_AddLine,None,Hatch_Hatcher)
Hatch_Hatcher.AddXLine = new_instancemethod(_Hatch.Hatch_Hatcher_AddXLine,None,Hatch_Hatcher)
Hatch_Hatcher.AddYLine = new_instancemethod(_Hatch.Hatch_Hatcher_AddYLine,None,Hatch_Hatcher)
Hatch_Hatcher.Trim = new_instancemethod(_Hatch.Hatch_Hatcher_Trim,None,Hatch_Hatcher)
Hatch_Hatcher.NbLines = new_instancemethod(_Hatch.Hatch_Hatcher_NbLines,None,Hatch_Hatcher)
Hatch_Hatcher.Line = new_instancemethod(_Hatch.Hatch_Hatcher_Line,None,Hatch_Hatcher)
Hatch_Hatcher.LineForm = new_instancemethod(_Hatch.Hatch_Hatcher_LineForm,None,Hatch_Hatcher)
Hatch_Hatcher.IsXLine = new_instancemethod(_Hatch.Hatch_Hatcher_IsXLine,None,Hatch_Hatcher)
Hatch_Hatcher.IsYLine = new_instancemethod(_Hatch.Hatch_Hatcher_IsYLine,None,Hatch_Hatcher)
Hatch_Hatcher.Coordinate = new_instancemethod(_Hatch.Hatch_Hatcher_Coordinate,None,Hatch_Hatcher)
Hatch_Hatcher.NbIntervals = new_instancemethod(_Hatch.Hatch_Hatcher_NbIntervals,None,Hatch_Hatcher)
Hatch_Hatcher.Start = new_instancemethod(_Hatch.Hatch_Hatcher_Start,None,Hatch_Hatcher)
Hatch_Hatcher.StartIndex = new_instancemethod(_Hatch.Hatch_Hatcher_StartIndex,None,Hatch_Hatcher)
Hatch_Hatcher.End = new_instancemethod(_Hatch.Hatch_Hatcher_End,None,Hatch_Hatcher)
Hatch_Hatcher.EndIndex = new_instancemethod(_Hatch.Hatch_Hatcher_EndIndex,None,Hatch_Hatcher)
Hatch_Hatcher_swigregister = _Hatch.Hatch_Hatcher_swigregister
Hatch_Hatcher_swigregister(Hatch_Hatcher)

class Hatch_Line(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param L:
        :type L: gp_Lin2d
        :param T:
        :type T: Hatch_LineForm
        :rtype: None

        """
        _Hatch.Hatch_Line_swiginit(self,_Hatch.new_Hatch_Line(*args))
    def AddIntersection(self, *args):
        """
        * Insert a new intersection in the sorted list.

        :param Par1:
        :type Par1: float
        :param Start:
        :type Start: bool
        :param Index:
        :type Index: int
        :param Par2:
        :type Par2: float
        :param theToler:
        :type theToler: float
        :rtype: None

        """
        return _Hatch.Hatch_Line_AddIntersection(self, *args)

    __swig_destroy__ = _Hatch.delete_Hatch_Line
Hatch_Line.AddIntersection = new_instancemethod(_Hatch.Hatch_Line_AddIntersection,None,Hatch_Line)
Hatch_Line_swigregister = _Hatch.Hatch_Line_swigregister
Hatch_Line_swigregister(Hatch_Line)

class Hatch_Parameter(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param Par1:
        :type Par1: float
        :param Start:
        :type Start: bool
        :param Index: default value is 0
        :type Index: int
        :param Par2: default value is 0
        :type Par2: float
        :rtype: None

        """
        _Hatch.Hatch_Parameter_swiginit(self,_Hatch.new_Hatch_Parameter(*args))
    __swig_destroy__ = _Hatch.delete_Hatch_Parameter
Hatch_Parameter_swigregister = _Hatch.Hatch_Parameter_swigregister
Hatch_Parameter_swigregister(Hatch_Parameter)

class Hatch_SequenceNodeOfSequenceOfLine(OCC.TCollection.TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param I:
        :type I: Hatch_Line &
        :param n:
        :type n: TCollection_SeqNodePtr &
        :param p:
        :type p: TCollection_SeqNodePtr &
        :rtype: None

        """
        _Hatch.Hatch_SequenceNodeOfSequenceOfLine_swiginit(self,_Hatch.new_Hatch_SequenceNodeOfSequenceOfLine(*args))
    def Value(self, *args):
        """
        :rtype: Hatch_Line

        """
        return _Hatch.Hatch_SequenceNodeOfSequenceOfLine_Value(self, *args)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Hatch_SequenceNodeOfSequenceOfLine(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _Hatch.delete_Hatch_SequenceNodeOfSequenceOfLine
Hatch_SequenceNodeOfSequenceOfLine.Value = new_instancemethod(_Hatch.Hatch_SequenceNodeOfSequenceOfLine_Value,None,Hatch_SequenceNodeOfSequenceOfLine)
Hatch_SequenceNodeOfSequenceOfLine_swigregister = _Hatch.Hatch_SequenceNodeOfSequenceOfLine_swigregister
Hatch_SequenceNodeOfSequenceOfLine_swigregister(Hatch_SequenceNodeOfSequenceOfLine)

class Handle_Hatch_SequenceNodeOfSequenceOfLine(OCC.TCollection.Handle_TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_swiginit(self,_Hatch.new_Handle_Hatch_SequenceNodeOfSequenceOfLine(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_DownCast)
    __swig_destroy__ = _Hatch.delete_Handle_Hatch_SequenceNodeOfSequenceOfLine
Handle_Hatch_SequenceNodeOfSequenceOfLine.Nullify = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_Nullify,None,Handle_Hatch_SequenceNodeOfSequenceOfLine)
Handle_Hatch_SequenceNodeOfSequenceOfLine.IsNull = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_IsNull,None,Handle_Hatch_SequenceNodeOfSequenceOfLine)
Handle_Hatch_SequenceNodeOfSequenceOfLine.GetObject = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_GetObject,None,Handle_Hatch_SequenceNodeOfSequenceOfLine)
Handle_Hatch_SequenceNodeOfSequenceOfLine_swigregister = _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_swigregister
Handle_Hatch_SequenceNodeOfSequenceOfLine_swigregister(Handle_Hatch_SequenceNodeOfSequenceOfLine)

def Handle_Hatch_SequenceNodeOfSequenceOfLine_DownCast(*args):
  return _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_DownCast(*args)
Handle_Hatch_SequenceNodeOfSequenceOfLine_DownCast = _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfLine_DownCast

class Hatch_SequenceNodeOfSequenceOfParameter(OCC.TCollection.TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param I:
        :type I: Hatch_Parameter &
        :param n:
        :type n: TCollection_SeqNodePtr &
        :param p:
        :type p: TCollection_SeqNodePtr &
        :rtype: None

        """
        _Hatch.Hatch_SequenceNodeOfSequenceOfParameter_swiginit(self,_Hatch.new_Hatch_SequenceNodeOfSequenceOfParameter(*args))
    def Value(self, *args):
        """
        :rtype: Hatch_Parameter

        """
        return _Hatch.Hatch_SequenceNodeOfSequenceOfParameter_Value(self, *args)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Hatch_SequenceNodeOfSequenceOfParameter(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _Hatch.delete_Hatch_SequenceNodeOfSequenceOfParameter
Hatch_SequenceNodeOfSequenceOfParameter.Value = new_instancemethod(_Hatch.Hatch_SequenceNodeOfSequenceOfParameter_Value,None,Hatch_SequenceNodeOfSequenceOfParameter)
Hatch_SequenceNodeOfSequenceOfParameter_swigregister = _Hatch.Hatch_SequenceNodeOfSequenceOfParameter_swigregister
Hatch_SequenceNodeOfSequenceOfParameter_swigregister(Hatch_SequenceNodeOfSequenceOfParameter)

class Handle_Hatch_SequenceNodeOfSequenceOfParameter(OCC.TCollection.Handle_TCollection_SeqNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_swiginit(self,_Hatch.new_Handle_Hatch_SequenceNodeOfSequenceOfParameter(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_DownCast)
    __swig_destroy__ = _Hatch.delete_Handle_Hatch_SequenceNodeOfSequenceOfParameter
Handle_Hatch_SequenceNodeOfSequenceOfParameter.Nullify = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_Nullify,None,Handle_Hatch_SequenceNodeOfSequenceOfParameter)
Handle_Hatch_SequenceNodeOfSequenceOfParameter.IsNull = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_IsNull,None,Handle_Hatch_SequenceNodeOfSequenceOfParameter)
Handle_Hatch_SequenceNodeOfSequenceOfParameter.GetObject = new_instancemethod(_Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_GetObject,None,Handle_Hatch_SequenceNodeOfSequenceOfParameter)
Handle_Hatch_SequenceNodeOfSequenceOfParameter_swigregister = _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_swigregister
Handle_Hatch_SequenceNodeOfSequenceOfParameter_swigregister(Handle_Hatch_SequenceNodeOfSequenceOfParameter)

def Handle_Hatch_SequenceNodeOfSequenceOfParameter_DownCast(*args):
  return _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_DownCast(*args)
Handle_Hatch_SequenceNodeOfSequenceOfParameter_DownCast = _Hatch.Handle_Hatch_SequenceNodeOfSequenceOfParameter_DownCast

class Hatch_SequenceOfLine(OCC.TCollection.TCollection_BaseSequence):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        """
        _Hatch.Hatch_SequenceOfLine_swiginit(self,_Hatch.new_Hatch_SequenceOfLine(*args))
    def Clear(self, *args):
        """
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_Clear(self, *args)

    def Assign(self, *args):
        """
        :param Other:
        :type Other: Hatch_SequenceOfLine &
        :rtype: Hatch_SequenceOfLine

        """
        return _Hatch.Hatch_SequenceOfLine_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: Hatch_SequenceOfLine &
        :rtype: Hatch_SequenceOfLine

        """
        return _Hatch.Hatch_SequenceOfLine_Set(self, *args)

    def Append(self, *args):
        """
        :param T:
        :type T: Hatch_Line &
        :rtype: None

        :param S:
        :type S: Hatch_SequenceOfLine &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_Append(self, *args)

    def Prepend(self, *args):
        """
        :param T:
        :type T: Hatch_Line &
        :rtype: None

        :param S:
        :type S: Hatch_SequenceOfLine &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_Prepend(self, *args)

    def InsertBefore(self, *args):
        """
        :param Index:
        :type Index: int
        :param T:
        :type T: Hatch_Line &
        :rtype: None

        :param Index:
        :type Index: int
        :param S:
        :type S: Hatch_SequenceOfLine &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_InsertBefore(self, *args)

    def InsertAfter(self, *args):
        """
        :param Index:
        :type Index: int
        :param T:
        :type T: Hatch_Line &
        :rtype: None

        :param Index:
        :type Index: int
        :param S:
        :type S: Hatch_SequenceOfLine &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_InsertAfter(self, *args)

    def First(self, *args):
        """
        :rtype: Hatch_Line

        """
        return _Hatch.Hatch_SequenceOfLine_First(self, *args)

    def Last(self, *args):
        """
        :rtype: Hatch_Line

        """
        return _Hatch.Hatch_SequenceOfLine_Last(self, *args)

    def Split(self, *args):
        """
        :param Index:
        :type Index: int
        :param Sub:
        :type Sub: Hatch_SequenceOfLine &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_Split(self, *args)

    def Value(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: Hatch_Line

        """
        return _Hatch.Hatch_SequenceOfLine_Value(self, *args)

    def SetValue(self, *args):
        """
        :param Index:
        :type Index: int
        :param I:
        :type I: Hatch_Line &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_SetValue(self, *args)

    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: Hatch_Line

        """
        return _Hatch.Hatch_SequenceOfLine_ChangeValue(self, *args)

    def Remove(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: None

        :param FromIndex:
        :type FromIndex: int
        :param ToIndex:
        :type ToIndex: int
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfLine_Remove(self, *args)

    __swig_destroy__ = _Hatch.delete_Hatch_SequenceOfLine
Hatch_SequenceOfLine.Clear = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Clear,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Assign = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Assign,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Set = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Set,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Append = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Append,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Prepend = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Prepend,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.InsertBefore = new_instancemethod(_Hatch.Hatch_SequenceOfLine_InsertBefore,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.InsertAfter = new_instancemethod(_Hatch.Hatch_SequenceOfLine_InsertAfter,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.First = new_instancemethod(_Hatch.Hatch_SequenceOfLine_First,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Last = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Last,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Split = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Split,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Value = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Value,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.SetValue = new_instancemethod(_Hatch.Hatch_SequenceOfLine_SetValue,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.ChangeValue = new_instancemethod(_Hatch.Hatch_SequenceOfLine_ChangeValue,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine.Remove = new_instancemethod(_Hatch.Hatch_SequenceOfLine_Remove,None,Hatch_SequenceOfLine)
Hatch_SequenceOfLine_swigregister = _Hatch.Hatch_SequenceOfLine_swigregister
Hatch_SequenceOfLine_swigregister(Hatch_SequenceOfLine)

class Hatch_SequenceOfParameter(OCC.TCollection.TCollection_BaseSequence):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        """
        _Hatch.Hatch_SequenceOfParameter_swiginit(self,_Hatch.new_Hatch_SequenceOfParameter(*args))
    def Clear(self, *args):
        """
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_Clear(self, *args)

    def Assign(self, *args):
        """
        :param Other:
        :type Other: Hatch_SequenceOfParameter &
        :rtype: Hatch_SequenceOfParameter

        """
        return _Hatch.Hatch_SequenceOfParameter_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: Hatch_SequenceOfParameter &
        :rtype: Hatch_SequenceOfParameter

        """
        return _Hatch.Hatch_SequenceOfParameter_Set(self, *args)

    def Append(self, *args):
        """
        :param T:
        :type T: Hatch_Parameter &
        :rtype: None

        :param S:
        :type S: Hatch_SequenceOfParameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_Append(self, *args)

    def Prepend(self, *args):
        """
        :param T:
        :type T: Hatch_Parameter &
        :rtype: None

        :param S:
        :type S: Hatch_SequenceOfParameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_Prepend(self, *args)

    def InsertBefore(self, *args):
        """
        :param Index:
        :type Index: int
        :param T:
        :type T: Hatch_Parameter &
        :rtype: None

        :param Index:
        :type Index: int
        :param S:
        :type S: Hatch_SequenceOfParameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_InsertBefore(self, *args)

    def InsertAfter(self, *args):
        """
        :param Index:
        :type Index: int
        :param T:
        :type T: Hatch_Parameter &
        :rtype: None

        :param Index:
        :type Index: int
        :param S:
        :type S: Hatch_SequenceOfParameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_InsertAfter(self, *args)

    def First(self, *args):
        """
        :rtype: Hatch_Parameter

        """
        return _Hatch.Hatch_SequenceOfParameter_First(self, *args)

    def Last(self, *args):
        """
        :rtype: Hatch_Parameter

        """
        return _Hatch.Hatch_SequenceOfParameter_Last(self, *args)

    def Split(self, *args):
        """
        :param Index:
        :type Index: int
        :param Sub:
        :type Sub: Hatch_SequenceOfParameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_Split(self, *args)

    def Value(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: Hatch_Parameter

        """
        return _Hatch.Hatch_SequenceOfParameter_Value(self, *args)

    def SetValue(self, *args):
        """
        :param Index:
        :type Index: int
        :param I:
        :type I: Hatch_Parameter &
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_SetValue(self, *args)

    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: Hatch_Parameter

        """
        return _Hatch.Hatch_SequenceOfParameter_ChangeValue(self, *args)

    def Remove(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: None

        :param FromIndex:
        :type FromIndex: int
        :param ToIndex:
        :type ToIndex: int
        :rtype: None

        """
        return _Hatch.Hatch_SequenceOfParameter_Remove(self, *args)

    __swig_destroy__ = _Hatch.delete_Hatch_SequenceOfParameter
Hatch_SequenceOfParameter.Clear = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Clear,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Assign = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Assign,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Set = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Set,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Append = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Append,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Prepend = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Prepend,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.InsertBefore = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_InsertBefore,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.InsertAfter = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_InsertAfter,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.First = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_First,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Last = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Last,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Split = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Split,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Value = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Value,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.SetValue = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_SetValue,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.ChangeValue = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_ChangeValue,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter.Remove = new_instancemethod(_Hatch.Hatch_SequenceOfParameter_Remove,None,Hatch_SequenceOfParameter)
Hatch_SequenceOfParameter_swigregister = _Hatch.Hatch_SequenceOfParameter_swigregister
Hatch_SequenceOfParameter_swigregister(Hatch_SequenceOfParameter)




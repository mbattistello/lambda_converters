# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _AdvApprox.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_AdvApprox', [dirname(__file__)])
        except ImportError:
            import _AdvApprox
            return _AdvApprox
        if fp is not None:
            try:
                _mod = imp.load_module('_AdvApprox', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _AdvApprox = swig_import_helper()
    del swig_import_helper
else:
    import _AdvApprox
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
    __swig_destroy__ = _AdvApprox.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_AdvApprox.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_AdvApprox.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_AdvApprox.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_AdvApprox.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_AdvApprox.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_AdvApprox.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_AdvApprox.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_AdvApprox.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_AdvApprox.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_AdvApprox.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_AdvApprox.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_AdvApprox.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_AdvApprox.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_AdvApprox.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_AdvApprox.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_AdvApprox.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _AdvApprox.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.GeomAbs
import OCC.TColgp
import OCC.gp
import OCC.PLib
import OCC.math
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

class AdvApprox_ApproxAFunction(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Constructs approximator tool. Warning: the Func should be valid reference to object of type inherited from class EvaluatorFunction from Approx with life time longer than that of the approximator tool; //!	 the result should be formatted in the following way : <--Num1DSS--> <--2 * Num2DSS--> <--3 * Num3DSS--> R[0] .... R[Num1DSS].....  R[Dimension-1] the order in which each Subspace appears should be consistent with the tolerances given in the create function and the results will be given in that order as well that is : Curve2d(n) will correspond to the nth entry described by Num2DSS, Curve(n) will correspond to the nth entry described by Num3DSS The same type of schema applies to the Poles1d, Poles2d and Poles.

        :param Num1DSS:
        :type Num1DSS: int
        :param Num2DSS:
        :type Num2DSS: int
        :param Num3DSS:
        :type Num3DSS: int
        :param OneDTol:
        :type OneDTol: Handle_TColStd_HArray1OfReal &
        :param TwoDTol:
        :type TwoDTol: Handle_TColStd_HArray1OfReal &
        :param ThreeDTol:
        :type ThreeDTol: Handle_TColStd_HArray1OfReal &
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Continuity:
        :type Continuity: GeomAbs_Shape
        :param MaxDeg:
        :type MaxDeg: int
        :param MaxSeg:
        :type MaxSeg: int
        :param Func:
        :type Func: AdvApprox_EvaluatorFunction &
        :rtype: None

        * Approximation with user methode of cutting

        :param Num1DSS:
        :type Num1DSS: int
        :param Num2DSS:
        :type Num2DSS: int
        :param Num3DSS:
        :type Num3DSS: int
        :param OneDTol:
        :type OneDTol: Handle_TColStd_HArray1OfReal &
        :param TwoDTol:
        :type TwoDTol: Handle_TColStd_HArray1OfReal &
        :param ThreeDTol:
        :type ThreeDTol: Handle_TColStd_HArray1OfReal &
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Continuity:
        :type Continuity: GeomAbs_Shape
        :param MaxDeg:
        :type MaxDeg: int
        :param MaxSeg:
        :type MaxSeg: int
        :param Func:
        :type Func: AdvApprox_EvaluatorFunction &
        :param CutTool:
        :type CutTool: AdvApprox_Cutting &
        :rtype: None

        """
        _AdvApprox.AdvApprox_ApproxAFunction_swiginit(self,_AdvApprox.new_AdvApprox_ApproxAFunction(*args))
    def Approximation(*args):
        """
        :param TotalDimension:
        :type TotalDimension: int
        :param TotalNumSS:
        :type TotalNumSS: int
        :param LocalDimension:
        :type LocalDimension: TColStd_Array1OfInteger &
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Evaluator:
        :type Evaluator: AdvApprox_EvaluatorFunction &
        :param CutTool:
        :type CutTool: AdvApprox_Cutting &
        :param ContinuityOrder:
        :type ContinuityOrder: int
        :param NumMaxCoeffs:
        :type NumMaxCoeffs: int
        :param MaxSegments:
        :type MaxSegments: int
        :param TolerancesArray:
        :type TolerancesArray: TColStd_Array1OfReal &
        :param code_precis:
        :type code_precis: int
        :param NumCurves:
        :type NumCurves: int &
        :param NumCoeffPerCurveArray:
        :type NumCoeffPerCurveArray: TColStd_Array1OfInteger &
        :param LocalCoefficientArray:
        :type LocalCoefficientArray: TColStd_Array1OfReal &
        :param IntervalsArray:
        :type IntervalsArray: TColStd_Array1OfReal &
        :param ErrorMaxArray:
        :type ErrorMaxArray: TColStd_Array1OfReal &
        :param AverageErrorArray:
        :type AverageErrorArray: TColStd_Array1OfReal &
        :param ErrorCode:
        :type ErrorCode: int &
        :rtype: void

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Approximation(*args)

    Approximation = staticmethod(Approximation)
    def IsDone(self, *args):
        """
        :rtype: bool

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_IsDone(self, *args)

    def HasResult(self, *args):
        """
        :rtype: bool

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_HasResult(self, *args)

    def NbPoles(self, *args):
        """
        * as the name says

        :rtype: int

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_NbPoles(self, *args)

    def Poles1d(self, *args):
        """
        * returns the poles from the algorithms as is

        :rtype: Handle_TColStd_HArray2OfReal

        * returns the poles at Index from the 1d subspace

        :param Index:
        :type Index: int
        :param P:
        :type P: TColStd_Array1OfReal &
        :rtype: None

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Poles1d(self, *args)

    def Poles2d(self, *args):
        """
        * returns the poles from the algorithms as is

        :rtype: Handle_TColgp_HArray2OfPnt2d

        * returns the poles at Index from the 2d subspace

        :param Index:
        :type Index: int
        :param P:
        :type P: TColgp_Array1OfPnt2d
        :rtype: None

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Poles2d(self, *args)

    def Poles(self, *args):
        """
        * -- returns the poles from the algorithms as is

        :rtype: Handle_TColgp_HArray2OfPnt

        * returns the poles at Index from the 3d subspace

        :param Index:
        :type Index: int
        :param P:
        :type P: TColgp_Array1OfPnt
        :rtype: None

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Poles(self, *args)

    def Degree(self, *args):
        """
        :rtype: int

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Degree(self, *args)

    def NbKnots(self, *args):
        """
        :rtype: int

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_NbKnots(self, *args)

    def NumSubSpaces(self, *args):
        """
        :param Dimension:
        :type Dimension: int
        :rtype: int

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_NumSubSpaces(self, *args)

    def Knots(self, *args):
        """
        :rtype: Handle_TColStd_HArray1OfReal

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Knots(self, *args)

    def Multiplicities(self, *args):
        """
        :rtype: Handle_TColStd_HArray1OfInteger

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_Multiplicities(self, *args)

    def MaxError(self, *args):
        """
        * returns the error as is in the algorithms

        :param Dimension:
        :type Dimension: int
        :rtype: Handle_TColStd_HArray1OfReal

        :param Dimension:
        :type Dimension: int
        :param Index:
        :type Index: int
        :rtype: float

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_MaxError(self, *args)

    def AverageError(self, *args):
        """
        * returns the error as is in the algorithms

        :param Dimension:
        :type Dimension: int
        :rtype: Handle_TColStd_HArray1OfReal

        :param Dimension:
        :type Dimension: int
        :param Index:
        :type Index: int
        :rtype: float

        """
        return _AdvApprox.AdvApprox_ApproxAFunction_AverageError(self, *args)

    def DumpToString(self):
        """DumpToString(AdvApprox_ApproxAFunction self) -> std::string"""
        return _AdvApprox.AdvApprox_ApproxAFunction_DumpToString(self)

    __swig_destroy__ = _AdvApprox.delete_AdvApprox_ApproxAFunction
AdvApprox_ApproxAFunction.IsDone = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_IsDone,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.HasResult = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_HasResult,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.NbPoles = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_NbPoles,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Poles1d = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Poles1d,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Poles2d = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Poles2d,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Poles = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Poles,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Degree = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Degree,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.NbKnots = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_NbKnots,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.NumSubSpaces = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_NumSubSpaces,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Knots = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Knots,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.Multiplicities = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_Multiplicities,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.MaxError = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_MaxError,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.AverageError = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_AverageError,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction.DumpToString = new_instancemethod(_AdvApprox.AdvApprox_ApproxAFunction_DumpToString,None,AdvApprox_ApproxAFunction)
AdvApprox_ApproxAFunction_swigregister = _AdvApprox.AdvApprox_ApproxAFunction_swigregister
AdvApprox_ApproxAFunction_swigregister(AdvApprox_ApproxAFunction)

def AdvApprox_ApproxAFunction_Approximation(*args):
  """
    :param TotalDimension:
    :type TotalDimension: int
    :param TotalNumSS:
    :type TotalNumSS: int
    :param LocalDimension:
    :type LocalDimension: TColStd_Array1OfInteger &
    :param First:
    :type First: float
    :param Last:
    :type Last: float
    :param Evaluator:
    :type Evaluator: AdvApprox_EvaluatorFunction &
    :param CutTool:
    :type CutTool: AdvApprox_Cutting &
    :param ContinuityOrder:
    :type ContinuityOrder: int
    :param NumMaxCoeffs:
    :type NumMaxCoeffs: int
    :param MaxSegments:
    :type MaxSegments: int
    :param TolerancesArray:
    :type TolerancesArray: TColStd_Array1OfReal &
    :param code_precis:
    :type code_precis: int
    :param NumCurves:
    :type NumCurves: int &
    :param NumCoeffPerCurveArray:
    :type NumCoeffPerCurveArray: TColStd_Array1OfInteger &
    :param LocalCoefficientArray:
    :type LocalCoefficientArray: TColStd_Array1OfReal &
    :param IntervalsArray:
    :type IntervalsArray: TColStd_Array1OfReal &
    :param ErrorMaxArray:
    :type ErrorMaxArray: TColStd_Array1OfReal &
    :param AverageErrorArray:
    :type AverageErrorArray: TColStd_Array1OfReal &
    :param ErrorCode:
    :type ErrorCode: int &
    :rtype: void

    """
  return _AdvApprox.AdvApprox_ApproxAFunction_Approximation(*args)

class AdvApprox_Cutting(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def Delete(self, *args):
        """
        :rtype: void

        """
        return _AdvApprox.AdvApprox_Cutting_Delete(self, *args)

    def Value(self, *args):
        """
        :param a:
        :type a: float
        :param b:
        :type b: float
        :param cuttingvalue:
        :type cuttingvalue: float &
        :rtype: bool

        """
        return _AdvApprox.AdvApprox_Cutting_Value(self, *args)

    __swig_destroy__ = _AdvApprox.delete_AdvApprox_Cutting
AdvApprox_Cutting.Delete = new_instancemethod(_AdvApprox.AdvApprox_Cutting_Delete,None,AdvApprox_Cutting)
AdvApprox_Cutting.Value = new_instancemethod(_AdvApprox.AdvApprox_Cutting_Value,None,AdvApprox_Cutting)
AdvApprox_Cutting_swigregister = _AdvApprox.AdvApprox_Cutting_swigregister
AdvApprox_Cutting_swigregister(AdvApprox_Cutting)

class AdvApprox_SimpleApprox(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param TotalDimension:
        :type TotalDimension: int
        :param TotalNumSS:
        :type TotalNumSS: int
        :param Continuity:
        :type Continuity: GeomAbs_Shape
        :param WorkDegree:
        :type WorkDegree: int
        :param NbGaussPoints:
        :type NbGaussPoints: int
        :param JacobiBase:
        :type JacobiBase: Handle_PLib_JacobiPolynomial &
        :param Func:
        :type Func: AdvApprox_EvaluatorFunction &
        :rtype: None

        """
        _AdvApprox.AdvApprox_SimpleApprox_swiginit(self,_AdvApprox.new_AdvApprox_SimpleApprox(*args))
    def Perform(self, *args):
        """
        * Constructs approximator tool. Warning: the Func should be valid reference to object of type inherited from class EvaluatorFunction from Approx with life time longer than that of the approximator tool;

        :param LocalDimension:
        :type LocalDimension: TColStd_Array1OfInteger &
        :param LocalTolerancesArray:
        :type LocalTolerancesArray: TColStd_Array1OfReal &
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param MaxDegree:
        :type MaxDegree: int
        :rtype: None

        """
        return _AdvApprox.AdvApprox_SimpleApprox_Perform(self, *args)

    def IsDone(self, *args):
        """
        :rtype: bool

        """
        return _AdvApprox.AdvApprox_SimpleApprox_IsDone(self, *args)

    def Degree(self, *args):
        """
        :rtype: int

        """
        return _AdvApprox.AdvApprox_SimpleApprox_Degree(self, *args)

    def Coefficients(self, *args):
        """
        * returns the coefficients in the Jacobi Base

        :rtype: Handle_TColStd_HArray1OfReal

        """
        return _AdvApprox.AdvApprox_SimpleApprox_Coefficients(self, *args)

    def FirstConstr(self, *args):
        """
        * returns the constraints at First

        :rtype: Handle_TColStd_HArray2OfReal

        """
        return _AdvApprox.AdvApprox_SimpleApprox_FirstConstr(self, *args)

    def LastConstr(self, *args):
        """
        * returns the constraints at Last

        :rtype: Handle_TColStd_HArray2OfReal

        """
        return _AdvApprox.AdvApprox_SimpleApprox_LastConstr(self, *args)

    def SomTab(self, *args):
        """
        :rtype: Handle_TColStd_HArray1OfReal

        """
        return _AdvApprox.AdvApprox_SimpleApprox_SomTab(self, *args)

    def DifTab(self, *args):
        """
        :rtype: Handle_TColStd_HArray1OfReal

        """
        return _AdvApprox.AdvApprox_SimpleApprox_DifTab(self, *args)

    def MaxError(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: float

        """
        return _AdvApprox.AdvApprox_SimpleApprox_MaxError(self, *args)

    def AverageError(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: float

        """
        return _AdvApprox.AdvApprox_SimpleApprox_AverageError(self, *args)

    def DumpToString(self):
        """DumpToString(AdvApprox_SimpleApprox self) -> std::string"""
        return _AdvApprox.AdvApprox_SimpleApprox_DumpToString(self)

    __swig_destroy__ = _AdvApprox.delete_AdvApprox_SimpleApprox
AdvApprox_SimpleApprox.Perform = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_Perform,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.IsDone = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_IsDone,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.Degree = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_Degree,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.Coefficients = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_Coefficients,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.FirstConstr = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_FirstConstr,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.LastConstr = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_LastConstr,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.SomTab = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_SomTab,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.DifTab = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_DifTab,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.MaxError = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_MaxError,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.AverageError = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_AverageError,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox.DumpToString = new_instancemethod(_AdvApprox.AdvApprox_SimpleApprox_DumpToString,None,AdvApprox_SimpleApprox)
AdvApprox_SimpleApprox_swigregister = _AdvApprox.AdvApprox_SimpleApprox_swigregister
AdvApprox_SimpleApprox_swigregister(AdvApprox_SimpleApprox)

class AdvApprox_DichoCutting(AdvApprox_Cutting):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        """
        _AdvApprox.AdvApprox_DichoCutting_swiginit(self,_AdvApprox.new_AdvApprox_DichoCutting(*args))
    __swig_destroy__ = _AdvApprox.delete_AdvApprox_DichoCutting
AdvApprox_DichoCutting_swigregister = _AdvApprox.AdvApprox_DichoCutting_swigregister
AdvApprox_DichoCutting_swigregister(AdvApprox_DichoCutting)

class AdvApprox_PrefAndRec(AdvApprox_Cutting):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param RecomendedCut:
        :type RecomendedCut: TColStd_Array1OfReal &
        :param PrefferedCut:
        :type PrefferedCut: TColStd_Array1OfReal &
        :param Weight: default value is 5
        :type Weight: float
        :rtype: None

        """
        _AdvApprox.AdvApprox_PrefAndRec_swiginit(self,_AdvApprox.new_AdvApprox_PrefAndRec(*args))
    __swig_destroy__ = _AdvApprox.delete_AdvApprox_PrefAndRec
AdvApprox_PrefAndRec_swigregister = _AdvApprox.AdvApprox_PrefAndRec_swigregister
AdvApprox_PrefAndRec_swigregister(AdvApprox_PrefAndRec)

class AdvApprox_PrefCutting(AdvApprox_Cutting):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param CutPnts:
        :type CutPnts: TColStd_Array1OfReal &
        :rtype: None

        """
        _AdvApprox.AdvApprox_PrefCutting_swiginit(self,_AdvApprox.new_AdvApprox_PrefCutting(*args))
    __swig_destroy__ = _AdvApprox.delete_AdvApprox_PrefCutting
AdvApprox_PrefCutting_swigregister = _AdvApprox.AdvApprox_PrefCutting_swigregister
AdvApprox_PrefCutting_swigregister(AdvApprox_PrefCutting)




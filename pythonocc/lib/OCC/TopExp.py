# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _TopExp.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TopExp', [dirname(__file__)])
        except ImportError:
            import _TopExp
            return _TopExp
        if fp is not None:
            try:
                _mod = imp.load_module('_TopExp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TopExp = swig_import_helper()
    del swig_import_helper
else:
    import _TopExp
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
    __swig_destroy__ = _TopExp.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_TopExp.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_TopExp.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_TopExp.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_TopExp.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_TopExp.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_TopExp.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_TopExp.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_TopExp.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_TopExp.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_TopExp.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_TopExp.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_TopExp.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_TopExp.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_TopExp.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_TopExp.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_TopExp.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _TopExp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.TopoDS
import OCC.MMgt
import OCC.Standard
import OCC.TCollection
import OCC.TopLoc
import OCC.gp
import OCC.TopAbs
import OCC.TopTools
import OCC.TColStd
import OCC.Message
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

class topexp(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def MapShapes(*args):
        """
        * Tool to explore a topological data structure. Stores in the map <M> all the sub-shapes of <S> of type <T>. Warning: The map is not cleared at first.

        :param S:
        :type S: TopoDS_Shape &
        :param T:
        :type T: TopAbs_ShapeEnum
        :param M:
        :type M: TopTools_IndexedMapOfShape &
        :rtype: void

        * Stores in the map <M> all the sub-shapes of <S>.

        :param S:
        :type S: TopoDS_Shape &
        :param M:
        :type M: TopTools_IndexedMapOfShape &
        :rtype: void

        """
        return _TopExp.topexp_MapShapes(*args)

    MapShapes = staticmethod(MapShapes)
    def MapShapesAndAncestors(*args):
        """
        * Stores in the map <M> all the subshape of <S> of type <TS> for each one append to the list all the ancestors of type <TA>. For example map all the edges and bind the list of faces. Warning: The map is not cleared at first.

        :param S:
        :type S: TopoDS_Shape &
        :param TS:
        :type TS: TopAbs_ShapeEnum
        :param TA:
        :type TA: TopAbs_ShapeEnum
        :param M:
        :type M: TopTools_IndexedDataMapOfShapeListOfShape &
        :rtype: void

        """
        return _TopExp.topexp_MapShapesAndAncestors(*args)

    MapShapesAndAncestors = staticmethod(MapShapesAndAncestors)
    def FirstVertex(*args):
        """
        * Returns the Vertex of orientation FORWARD in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation

        :param E:
        :type E: TopoDS_Edge &
        :param CumOri: default value is Standard_False
        :type CumOri: bool
        :rtype: TopoDS_Vertex

        """
        return _TopExp.topexp_FirstVertex(*args)

    FirstVertex = staticmethod(FirstVertex)
    def LastVertex(*args):
        """
        * Returns the Vertex of orientation REVERSED in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation

        :param E:
        :type E: TopoDS_Edge &
        :param CumOri: default value is Standard_False
        :type CumOri: bool
        :rtype: TopoDS_Vertex

        """
        return _TopExp.topexp_LastVertex(*args)

    LastVertex = staticmethod(LastVertex)
    def Vertices(*args):
        """
        * Returns in Vfirst, Vlast the FORWARD and REVERSED vertices of the edge <E>. May be null shapes. CumOri = True : taking account the edge orientation

        :param E:
        :type E: TopoDS_Edge &
        :param Vfirst:
        :type Vfirst: TopoDS_Vertex &
        :param Vlast:
        :type Vlast: TopoDS_Vertex &
        :param CumOri: default value is Standard_False
        :type CumOri: bool
        :rtype: void

        * Returns in Vfirst, Vlast the first and last vertices of the open wire <W>. May be null shapes. if <W> is closed Vfirst and Vlast are a same vertex on <W>. if <W> is no manifold. VFirst and VLast are null shapes.

        :param W:
        :type W: TopoDS_Wire &
        :param Vfirst:
        :type Vfirst: TopoDS_Vertex &
        :param Vlast:
        :type Vlast: TopoDS_Vertex &
        :rtype: void

        """
        return _TopExp.topexp_Vertices(*args)

    Vertices = staticmethod(Vertices)
    def CommonVertex(*args):
        """
        * Finds the vertex <V> common to the two edges <E1,E2>, returns True if this vertex exists. Warning: <V> has sense only if the value <True> is returned

        :param E1:
        :type E1: TopoDS_Edge &
        :param E2:
        :type E2: TopoDS_Edge &
        :param V:
        :type V: TopoDS_Vertex &
        :rtype: bool

        """
        return _TopExp.topexp_CommonVertex(*args)

    CommonVertex = staticmethod(CommonVertex)
    def __init__(self): 
        _TopExp.topexp_swiginit(self,_TopExp.new_topexp())
    __swig_destroy__ = _TopExp.delete_topexp
topexp_swigregister = _TopExp.topexp_swigregister
topexp_swigregister(topexp)

def topexp_MapShapes(*args):
  """
    * Tool to explore a topological data structure. Stores in the map <M> all the sub-shapes of <S> of type <T>. Warning: The map is not cleared at first.

    :param S:
    :type S: TopoDS_Shape &
    :param T:
    :type T: TopAbs_ShapeEnum
    :param M:
    :type M: TopTools_IndexedMapOfShape &
    :rtype: void

    * Stores in the map <M> all the sub-shapes of <S>.

    :param S:
    :type S: TopoDS_Shape &
    :param M:
    :type M: TopTools_IndexedMapOfShape &
    :rtype: void

    """
  return _TopExp.topexp_MapShapes(*args)

def topexp_MapShapesAndAncestors(*args):
  """
    * Stores in the map <M> all the subshape of <S> of type <TS> for each one append to the list all the ancestors of type <TA>. For example map all the edges and bind the list of faces. Warning: The map is not cleared at first.

    :param S:
    :type S: TopoDS_Shape &
    :param TS:
    :type TS: TopAbs_ShapeEnum
    :param TA:
    :type TA: TopAbs_ShapeEnum
    :param M:
    :type M: TopTools_IndexedDataMapOfShapeListOfShape &
    :rtype: void

    """
  return _TopExp.topexp_MapShapesAndAncestors(*args)

def topexp_FirstVertex(*args):
  """
    * Returns the Vertex of orientation FORWARD in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation

    :param E:
    :type E: TopoDS_Edge &
    :param CumOri: default value is Standard_False
    :type CumOri: bool
    :rtype: TopoDS_Vertex

    """
  return _TopExp.topexp_FirstVertex(*args)

def topexp_LastVertex(*args):
  """
    * Returns the Vertex of orientation REVERSED in E. If there is none returns a Null Shape. CumOri = True : taking account the edge orientation

    :param E:
    :type E: TopoDS_Edge &
    :param CumOri: default value is Standard_False
    :type CumOri: bool
    :rtype: TopoDS_Vertex

    """
  return _TopExp.topexp_LastVertex(*args)

def topexp_Vertices(*args):
  """
    * Returns in Vfirst, Vlast the FORWARD and REVERSED vertices of the edge <E>. May be null shapes. CumOri = True : taking account the edge orientation

    :param E:
    :type E: TopoDS_Edge &
    :param Vfirst:
    :type Vfirst: TopoDS_Vertex &
    :param Vlast:
    :type Vlast: TopoDS_Vertex &
    :param CumOri: default value is Standard_False
    :type CumOri: bool
    :rtype: void

    * Returns in Vfirst, Vlast the first and last vertices of the open wire <W>. May be null shapes. if <W> is closed Vfirst and Vlast are a same vertex on <W>. if <W> is no manifold. VFirst and VLast are null shapes.

    :param W:
    :type W: TopoDS_Wire &
    :param Vfirst:
    :type Vfirst: TopoDS_Vertex &
    :param Vlast:
    :type Vlast: TopoDS_Vertex &
    :rtype: void

    """
  return _TopExp.topexp_Vertices(*args)

def topexp_CommonVertex(*args):
  """
    * Finds the vertex <V> common to the two edges <E1,E2>, returns True if this vertex exists. Warning: <V> has sense only if the value <True> is returned

    :param E1:
    :type E1: TopoDS_Edge &
    :param E2:
    :type E2: TopoDS_Edge &
    :param V:
    :type V: TopoDS_Vertex &
    :rtype: bool

    """
  return _TopExp.topexp_CommonVertex(*args)

class TopExp_Explorer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        * Creates an empty explorer, becomes usefull after Init.

        :rtype: None

        * Creates an Explorer on the Shape <S>.  <ToFind> is the type of shapes to search. TopAbs_VERTEX, TopAbs_EDGE, ...  <ToAvoid> is the type of shape to skip in the exploration. If <ToAvoid> is equal or less complex than <ToFind> or if <ToAVoid> is SHAPE it has no effect on the exploration.

        :param S:
        :type S: TopoDS_Shape &
        :param ToFind:
        :type ToFind: TopAbs_ShapeEnum
        :param ToAvoid: default value is TopAbs_SHAPE
        :type ToAvoid: TopAbs_ShapeEnum
        :rtype: None

        """
        _TopExp.TopExp_Explorer_swiginit(self,_TopExp.new_TopExp_Explorer(*args))
    def Init(self, *args):
        """
        * Resets this explorer on the shape S. It is initialized to search the shape S, for shapes of type ToFind, that are not part of a shape ToAvoid. If the shape ToAvoid is equal to TopAbs_SHAPE, or if it is the same as, or less complex than, the shape ToFind it has no effect on the search.

        :param S:
        :type S: TopoDS_Shape &
        :param ToFind:
        :type ToFind: TopAbs_ShapeEnum
        :param ToAvoid: default value is TopAbs_SHAPE
        :type ToAvoid: TopAbs_ShapeEnum
        :rtype: None

        """
        return _TopExp.TopExp_Explorer_Init(self, *args)

    def More(self, *args):
        """
        * Returns True if there are more shapes in the exploration.

        :rtype: bool

        """
        return _TopExp.TopExp_Explorer_More(self, *args)

    def Next(self, *args):
        """
        * Moves to the next Shape in the exploration. Exceptions Standard_NoMoreObject if there are no more shapes to explore.

        :rtype: None

        """
        return _TopExp.TopExp_Explorer_Next(self, *args)

    def Current(self, *args):
        """
        * Returns the current shape in the exploration. Exceptions Standard_NoSuchObject if this explorer has no more shapes to explore.

        :rtype: TopoDS_Shape

        """
        return _TopExp.TopExp_Explorer_Current(self, *args)

    def ReInit(self, *args):
        """
        * Reinitialize the exploration with the original arguments.

        :rtype: None

        """
        return _TopExp.TopExp_Explorer_ReInit(self, *args)

    def Depth(self, *args):
        """
        * Returns the current depth of the exploration. 0 is the shape to explore itself.

        :rtype: int

        """
        return _TopExp.TopExp_Explorer_Depth(self, *args)

    def Clear(self, *args):
        """
        * Clears the content of the explorer. It will return False on More().

        :rtype: None

        """
        return _TopExp.TopExp_Explorer_Clear(self, *args)

    def Destroy(self, *args):
        """
        :rtype: None

        """
        return _TopExp.TopExp_Explorer_Destroy(self, *args)

    __swig_destroy__ = _TopExp.delete_TopExp_Explorer
TopExp_Explorer.Init = new_instancemethod(_TopExp.TopExp_Explorer_Init,None,TopExp_Explorer)
TopExp_Explorer.More = new_instancemethod(_TopExp.TopExp_Explorer_More,None,TopExp_Explorer)
TopExp_Explorer.Next = new_instancemethod(_TopExp.TopExp_Explorer_Next,None,TopExp_Explorer)
TopExp_Explorer.Current = new_instancemethod(_TopExp.TopExp_Explorer_Current,None,TopExp_Explorer)
TopExp_Explorer.ReInit = new_instancemethod(_TopExp.TopExp_Explorer_ReInit,None,TopExp_Explorer)
TopExp_Explorer.Depth = new_instancemethod(_TopExp.TopExp_Explorer_Depth,None,TopExp_Explorer)
TopExp_Explorer.Clear = new_instancemethod(_TopExp.TopExp_Explorer_Clear,None,TopExp_Explorer)
TopExp_Explorer.Destroy = new_instancemethod(_TopExp.TopExp_Explorer_Destroy,None,TopExp_Explorer)
TopExp_Explorer_swigregister = _TopExp.TopExp_Explorer_swigregister
TopExp_Explorer_swigregister(TopExp_Explorer)

class TopExp_StackIteratorOfStackOfIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param S:
        :type S: TopExp_StackOfIterator &
        :rtype: None

        """
        _TopExp.TopExp_StackIteratorOfStackOfIterator_swiginit(self,_TopExp.new_TopExp_StackIteratorOfStackOfIterator(*args))
    def Initialize(self, *args):
        """
        :param S:
        :type S: TopExp_StackOfIterator &
        :rtype: None

        """
        return _TopExp.TopExp_StackIteratorOfStackOfIterator_Initialize(self, *args)

    def More(self, *args):
        """
        :rtype: bool

        """
        return _TopExp.TopExp_StackIteratorOfStackOfIterator_More(self, *args)

    def Next(self, *args):
        """
        :rtype: None

        """
        return _TopExp.TopExp_StackIteratorOfStackOfIterator_Next(self, *args)

    def Value(self, *args):
        """
        :rtype: TopoDS_Iterator

        """
        return _TopExp.TopExp_StackIteratorOfStackOfIterator_Value(self, *args)

    __swig_destroy__ = _TopExp.delete_TopExp_StackIteratorOfStackOfIterator
TopExp_StackIteratorOfStackOfIterator.Initialize = new_instancemethod(_TopExp.TopExp_StackIteratorOfStackOfIterator_Initialize,None,TopExp_StackIteratorOfStackOfIterator)
TopExp_StackIteratorOfStackOfIterator.More = new_instancemethod(_TopExp.TopExp_StackIteratorOfStackOfIterator_More,None,TopExp_StackIteratorOfStackOfIterator)
TopExp_StackIteratorOfStackOfIterator.Next = new_instancemethod(_TopExp.TopExp_StackIteratorOfStackOfIterator_Next,None,TopExp_StackIteratorOfStackOfIterator)
TopExp_StackIteratorOfStackOfIterator.Value = new_instancemethod(_TopExp.TopExp_StackIteratorOfStackOfIterator_Value,None,TopExp_StackIteratorOfStackOfIterator)
TopExp_StackIteratorOfStackOfIterator_swigregister = _TopExp.TopExp_StackIteratorOfStackOfIterator_swigregister
TopExp_StackIteratorOfStackOfIterator_swigregister(TopExp_StackIteratorOfStackOfIterator)

class TopExp_StackNodeOfStackOfIterator(OCC.TCollection.TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param I:
        :type I: TopoDS_Iterator &
        :param n:
        :type n: TCollection_MapNodePtr &
        :rtype: None

        """
        _TopExp.TopExp_StackNodeOfStackOfIterator_swiginit(self,_TopExp.new_TopExp_StackNodeOfStackOfIterator(*args))
    def Value(self, *args):
        """
        :rtype: TopoDS_Iterator

        """
        return _TopExp.TopExp_StackNodeOfStackOfIterator_Value(self, *args)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_TopExp_StackNodeOfStackOfIterator(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _TopExp.delete_TopExp_StackNodeOfStackOfIterator
TopExp_StackNodeOfStackOfIterator.Value = new_instancemethod(_TopExp.TopExp_StackNodeOfStackOfIterator_Value,None,TopExp_StackNodeOfStackOfIterator)
TopExp_StackNodeOfStackOfIterator_swigregister = _TopExp.TopExp_StackNodeOfStackOfIterator_swigregister
TopExp_StackNodeOfStackOfIterator_swigregister(TopExp_StackNodeOfStackOfIterator)

class Handle_TopExp_StackNodeOfStackOfIterator(OCC.TCollection.Handle_TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _TopExp.Handle_TopExp_StackNodeOfStackOfIterator_swiginit(self,_TopExp.new_Handle_TopExp_StackNodeOfStackOfIterator(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_TopExp.Handle_TopExp_StackNodeOfStackOfIterator_DownCast)
    __swig_destroy__ = _TopExp.delete_Handle_TopExp_StackNodeOfStackOfIterator
Handle_TopExp_StackNodeOfStackOfIterator.Nullify = new_instancemethod(_TopExp.Handle_TopExp_StackNodeOfStackOfIterator_Nullify,None,Handle_TopExp_StackNodeOfStackOfIterator)
Handle_TopExp_StackNodeOfStackOfIterator.IsNull = new_instancemethod(_TopExp.Handle_TopExp_StackNodeOfStackOfIterator_IsNull,None,Handle_TopExp_StackNodeOfStackOfIterator)
Handle_TopExp_StackNodeOfStackOfIterator.GetObject = new_instancemethod(_TopExp.Handle_TopExp_StackNodeOfStackOfIterator_GetObject,None,Handle_TopExp_StackNodeOfStackOfIterator)
Handle_TopExp_StackNodeOfStackOfIterator_swigregister = _TopExp.Handle_TopExp_StackNodeOfStackOfIterator_swigregister
Handle_TopExp_StackNodeOfStackOfIterator_swigregister(Handle_TopExp_StackNodeOfStackOfIterator)

def Handle_TopExp_StackNodeOfStackOfIterator_DownCast(*args):
  return _TopExp.Handle_TopExp_StackNodeOfStackOfIterator_DownCast(*args)
Handle_TopExp_StackNodeOfStackOfIterator_DownCast = _TopExp.Handle_TopExp_StackNodeOfStackOfIterator_DownCast

class TopExp_StackOfIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        """
        _TopExp.TopExp_StackOfIterator_swiginit(self,_TopExp.new_TopExp_StackOfIterator(*args))
    def Assign(self, *args):
        """
        :param Other:
        :type Other: TopExp_StackOfIterator &
        :rtype: TopExp_StackOfIterator

        """
        return _TopExp.TopExp_StackOfIterator_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: TopExp_StackOfIterator &
        :rtype: TopExp_StackOfIterator

        """
        return _TopExp.TopExp_StackOfIterator_Set(self, *args)

    def IsEmpty(self, *args):
        """
        :rtype: bool

        """
        return _TopExp.TopExp_StackOfIterator_IsEmpty(self, *args)

    def Depth(self, *args):
        """
        :rtype: int

        """
        return _TopExp.TopExp_StackOfIterator_Depth(self, *args)

    def Top(self, *args):
        """
        :rtype: TopoDS_Iterator

        """
        return _TopExp.TopExp_StackOfIterator_Top(self, *args)

    def Push(self, *args):
        """
        :param I:
        :type I: TopoDS_Iterator &
        :rtype: None

        """
        return _TopExp.TopExp_StackOfIterator_Push(self, *args)

    def Pop(self, *args):
        """
        :rtype: None

        """
        return _TopExp.TopExp_StackOfIterator_Pop(self, *args)

    def Clear(self, *args):
        """
        :rtype: None

        """
        return _TopExp.TopExp_StackOfIterator_Clear(self, *args)

    def ChangeTop(self, *args):
        """
        :rtype: TopoDS_Iterator

        """
        return _TopExp.TopExp_StackOfIterator_ChangeTop(self, *args)

    __swig_destroy__ = _TopExp.delete_TopExp_StackOfIterator
TopExp_StackOfIterator.Assign = new_instancemethod(_TopExp.TopExp_StackOfIterator_Assign,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Set = new_instancemethod(_TopExp.TopExp_StackOfIterator_Set,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.IsEmpty = new_instancemethod(_TopExp.TopExp_StackOfIterator_IsEmpty,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Depth = new_instancemethod(_TopExp.TopExp_StackOfIterator_Depth,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Top = new_instancemethod(_TopExp.TopExp_StackOfIterator_Top,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Push = new_instancemethod(_TopExp.TopExp_StackOfIterator_Push,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Pop = new_instancemethod(_TopExp.TopExp_StackOfIterator_Pop,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.Clear = new_instancemethod(_TopExp.TopExp_StackOfIterator_Clear,None,TopExp_StackOfIterator)
TopExp_StackOfIterator.ChangeTop = new_instancemethod(_TopExp.TopExp_StackOfIterator_ChangeTop,None,TopExp_StackOfIterator)
TopExp_StackOfIterator_swigregister = _TopExp.TopExp_StackOfIterator_swigregister
TopExp_StackOfIterator_swigregister(TopExp_StackOfIterator)



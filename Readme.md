## 임금 관리 프로그램


+ 클래스 상속

class myParent( object ):
    def __init__( self, parentId ):
        self.id = parentId
        self.children = []

    def createChild( self, name ):
        self.children.append( myChild( name, self ) )

    def getChildren( self ):
        return self.children

class myChild( object ):
    def __init__( self, childId, parent ):
        self.id = childId
        self.parent = parent

    def getParentId( self ):
        return self.parent.id

p = myParent( 'parent01' )
p.createChild( 'child01' )
print p.getChildren()[0].getParentId()

<https://stackoverflow.com/questions/4935587/python-getting-baseclass-values-from-derived-class>

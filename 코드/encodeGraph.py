from graph import *

def getGraph01():
    g = Graph(False)
    
    a = Vertex("a");    b = Vertex("b")
    c = Vertex("c");    d = Vertex("d")
    e = Vertex("e")

    g.addVertex(a);    g.addVertex(b)
    g.addVertex(c);    g.addVertex(d)
    g.addVertex(e)

    e1= Edge(a, b, 1);    e2= Edge(a, e, 1)
    e3= Edge(b, e, 1);    e4= Edge(b, c, 1)
    e5= Edge(c, d, 1);    e6= Edge(d, e, 1)
    
    g.addEdge(e1);    g.addEdge(e2)
    g.addEdge(e3);    g.addEdge(e4)
    g.addEdge(e5);    g.addEdge(e6)

    return g

def getGraph02():
    g = Graph(True)
    a = Vertex("a");    b = Vertex("b")
    c = Vertex("c");    d= Vertex ("d")
 
    g.addVertex(a); g.addVertex(b)
    g.addVertex(c); g.addVertex(d)
    
   
    e1= Edge(a, b, 1);  e2= Edge(b, c, 1)
    e3= Edge(c, a, 1);  e4= Edge(a, c, 1)
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3);   g.addEdge(e4)
    
    return g
def getGraph03():
    g = Graph(True)
    
    a = Vertex("1");    b = Vertex("2");  c = Vertex("3")
    d=  Vertex ("4");   e = Vertex("5");  f = Vertex("6")
    
    g.addVertex(a); g.addVertex(b); g.addVertex(c)
    g.addVertex(d); g.addVertex(e); g.addVertex(f)
    
    
    e1= Edge(a, b, 1);  e2= Edge(a, c, 1); e3= Edge(b, e, 1)
    e4= Edge(b, d, 1);  e5= Edge(c, d, 1); e6= Edge(d, e, 1)
    e7 = Edge(a,f,1);   e8 = Edge(f,e,1)
    
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3);   g.addEdge(e4)
    g.addEdge(e5);  g.addEdge(e6);  g.addEdge(e7);   g.addEdge(e8)
    return g

def getGraph04():
    g=Graph(False)
    v1=Vertex("A");v2=Vertex("B");v3=Vertex("C");v4=Vertex("D")
    v5=Vertex("E");v6=Vertex("F");v7=Vertex("G");v8=Vertex("H")
    
    g.addVertex(v1);g.addVertex(v2);g.addVertex(v3);g.addVertex(v4)
    g.addVertex(v5);g.addVertex(v6);g.addVertex(v7);g.addVertex(v8)
   
    e1= Edge(v1, v2, 1);e2= Edge(v1, v3, 1);e3= Edge(v2, v4, 1)
    e4= Edge(v3, v4, 1);e5= Edge(v4, v6, 1); e6= Edge(v3, v5, 1)
    e7= Edge(v5, v7, 1); e8= Edge(v5, v8, 1); e9= Edge(v7, v8, 1)
    
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3) 
    g.addEdge(e4);  g.addEdge(e5);  g.addEdge(e6) 
    g.addEdge(e7);  g.addEdge(e8);  g.addEdge(e9)

    return g

def getGraph05():
    g=Graph(False)
    v1=Vertex("v1");v2=Vertex("v2");v3=Vertex("v3");v4=Vertex("v4")
    v5=Vertex("v5");v6=Vertex("v6");v7=Vertex("v7")
    
    g.addVertex(v1);g.addVertex(v2);g.addVertex(v3);g.addVertex(v4)
    g.addVertex(v5);g.addVertex(v6);g.addVertex(v7)

    e1= Edge(v1, v2, 2);  e2= Edge(v1, v3, 4);  e3= Edge(v1, v4, 1)
    e4= Edge(v2, v4, 3);  e5= Edge(v2, v5, 10); e6= Edge(v3, v4, 2) 
    e7= Edge(v3, v6, 5);  e8= Edge(v4, v5, 7);  e9= Edge(v4, v6, 8) 
    e10= Edge(v4, v7, 4); e11= Edge(v5, v7, 6); e12= Edge(v6, v7, 1)
    
    
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3)
    g.addEdge(e4);  g.addEdge(e5);  g.addEdge(e6)
    g.addEdge(e7);  g.addEdge(e8);  g.addEdge(e9) 
    g.addEdge(e10); g.addEdge(e11); g.addEdge(e12)    
    return g

def getGraph06():
    g=Graph(True)
    v1=Vertex("v1");v2=Vertex("v2");v3=Vertex("v3");v4=Vertex("v4")
    v5=Vertex("v5");v6=Vertex("v6");v7=Vertex("v7")
    
    g.addVertex(v1);g.addVertex(v2);g.addVertex(v3);g.addVertex(v4)
    g.addVertex(v5);g.addVertex(v6);g.addVertex(v7)
    
    e1= Edge(v1, v2, 4);  e2= Edge(v1, v6, 10);e3= Edge(v2, v1, 3); e4= Edge(v2, v4, 18)
    e5= Edge(v3, v2, 6); e6= Edge(v4, v2, 5); e7= Edge(v4, v5, 2); e8= Edge(v4, v6, 19)
    e9= Edge(v4, v7, 5);  e10= Edge(v5, v4, 1); e11= Edge(v6, v7, 10); e12= Edge(v7, v4, 8)
    e13= Edge(v5, v3, 12); e14= Edge(v4, v3, 15)
    
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3);   g.addEdge(e4);    g.addEdge(e5)
    g.addEdge(e6);  g.addEdge(e7);  g.addEdge(e8);   g.addEdge(e9);    g.addEdge(e10)
    g.addEdge(e11); g.addEdge(e12); g.addEdge(e13);  g.addEdge(e14)
       
    return g

def getGraph07():
    g=Graph(True)
    v1=Vertex("v1");v2=Vertex("v2");v3=Vertex("v3")
    v4=Vertex("v4"); v5=Vertex("v5")
    
    g.addVertex(v1);g.addVertex(v2);g.addVertex(v3);
    g.addVertex(v4);g.addVertex(v5)
    
    e1= Edge(v1, v2, 1);  e2= Edge(v1, v4, 1);e3= Edge(v1, v5, 5); e4= Edge(v2, v1, 9)
    e5= Edge(v2, v3, 3); e6= Edge(v2, v4, 2); e7= Edge(v3, v4, 4); e8= Edge(v4, v3, 2)
    e9= Edge(v4, v5, 3);  e10= Edge(v5, v1, 3); 
    
    g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3);   g.addEdge(e4);    g.addEdge(e5)
    g.addEdge(e6);  g.addEdge(e7);  g.addEdge(e8);   g.addEdge(e9);    g.addEdge(e10)
    
       
    return g



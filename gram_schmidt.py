import numpy as np

def gs_cofficient(v1, v2):
    return np.dot(v2, v1) / np.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    print "v1 * (v2 * v1 / v1 * v1)  -->", v1, "*", np.dot(v2, v1) , "/", np.dot(v1, v1)
    return multiply(gs_cofficient(v1, v2) , v1)

def gs(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y :
            proj_vec = proj(inY, X[i])
            temp_vec = map(lambda x, y : x - y, temp_vec, proj_vec)
        Y.append(temp_vec)
    return Y

#Calcular la base ortogonal
#test = np.array([[0.0, 0.0, 1.0, 1.0], [1.0, 0.0, -1.0, 1.0 ], [-1.0, 1.0, 1.0, -1.0]])
test = np.array([[-1.0, 0.0, 1.0 ], [-2.0, 1.0, 1.0]])
print "Base:\n", test , "\n"
baseorto = np.array(gs(test))
print "Base ortogonal:\n", baseorto , "\n"

# Proyeccion
w = np.array([-3.0, 0.0, 0.0])
print "Vector w: ", w
P = []
for i in range(len(baseorto)):
    proj_vec = proj(baseorto[i], w)
    P.append(proj_vec)

print "A sumar: ", P

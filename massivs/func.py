import scipy


def Zamena(array,s1,s2):
    L = []
    array = array.replace("[", '', 2)
    array = array.replace(" ", '')
    array = array[:-2]
    for el in array.split('],['):
        l = []
        for ell in el.split(','):
            l.append(int(ell))
        L.append(l)

    a = scipy.array(L)


    A = scipy.array(a)
    a[:, s1] = a[:, s2]
    a[:, s2] = A[:, s1]
    return a

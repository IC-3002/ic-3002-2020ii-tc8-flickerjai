def contar_rutas_mas_cortas(C):

    lim = len(C)-1
    if  C[lim][lim] == 1:
        return 0
    else:
        if vefPosibilidad(C, lim) == -1:
            return 0
        C[lim][lim] = 'y'
        x = verificarMatrizColumna(C, lim, 1,0,0)+1
        if x == 3:
            return x+1
        else:
            return x


def verificarMatrizColumna(C, lim, i, posiblesRutas, iteraciones):

    if lim != -1:

        if lim == len(C)-1:

            if i> len(C)-1:
                if C[i-1][lim] == 'y':
                    return verificarMatrizColumna(C, lim-1, 1 , posiblesRutas+1, iteraciones+1 )
            
                elif C[i-1][lim] == 0:
                    C[i-1][lim] = 'b'
                    return verificarMatrizColumna(C, lim, i+1, posiblesRutas, iteraciones )
                else:
                    return verificarMatrizColumna(C, lim-1, 1 , posiblesRutas, iteraciones+1)

            elif C[i][lim] == 'y':
                return verificarMatrizColumna(C, lim-1, 1 , posiblesRutas+1, iteraciones+1 )
            
            elif C[i][lim] == 0:
                C[i][lim] = 'b'
                return verificarMatrizColumna(C, lim, i+1, posiblesRutas, iteraciones )
            else:
                return verificarMatrizColumna(C, lim-1, posiblesRutas, iteraciones+1)
        elif i <= len(C)-1:

            if C[i][lim] == 0:
                if C[i][lim+1] == 'b':
                    C[i][lim] = 'b'
                    return verificarMatrizColumna(C, lim, i+1, posiblesRutas+1*iteraciones, iteraciones)

                elif C[i][lim+1] == 'y':
                    C[i][lim] = 'b'
                    return verificarMatrizColumna(C, lim-1, 1, posiblesRutas+1*iteraciones, iteraciones+1)
                else:
                    return verificarMatrizColumna(C, lim-1, 1, posiblesRutas, iteraciones+1)
            else:
                return verificarMatrizColumna(C, lim-1, 1, posiblesRutas, iteraciones+1)
        else:
            return verificarMatrizColumna(C, lim-1, 1, posiblesRutas, iteraciones+1)

    else:
        return posiblesRutas

def vefPosibilidad(C,lim):
    i = lim
    x = False
    y = False
    while (i != -1):
        if C[i][lim] == 1:
            x = True
        i -= 1
    i = lim
    while(i != -1):
        if C[lim][i] == 1:
            y = True
        i -= 1
    if x == True and y == True:
        return -1
    else:
        return 1

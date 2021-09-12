    
    
def _integrateTest(t, n, _f):

    maxError = 0.001
    simpsonOld = 0.0
    simpsonNew = maxError
    
    lowBound = 0
    highBound = 16
    divisions = 4
    
    while (abs((simpsonNew - simpsonOld) / simpsonNew) > maxError):
        simpsonOld = simpsonNew
        width = (highBound - lowBound) / divisions
        
        total = 0
        i = 1
        currentWidth = 0
        
        for x in range(divisions):

           
            if (x == 0):
                total += _f(currentWidth, n)
                i += 1
                
            elif (x == divisions):
                total += _f(currentWidth, n)
                
            elif (i == 2):
                total += 2 * _f(currentWidth, n)
                i += 1
                
            elif(i == 3):
                total += 4 * _f(currentWidth, n)
                i = 2
                
                
            currentWidth += width
            
        simpsonNew = (width/3) * total
        
        divisions = divisions * 2
        
    return simpsonNew


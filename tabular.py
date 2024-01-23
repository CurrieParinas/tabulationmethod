
import globalVariables

def mintermsProduct(num1,num2): 
    '''
    Description:                            multiplies minterms and appends them on the list
    Arguments:
        num1, num2                          the numbers from interaction

    Returns:
        res                                 a refined list
    '''
    res = []
    for i in num1:
        if i+"'" in num2 or (len(i) == 2 and i[0] in num2):
            return []
        else:
            res.append(i)
    for i in num2:
        if i not in res:
            res.append(i)
    return res

def expressionProduct(exp1,exp2):
    '''
    Description:                           multiplies expressions and appends them on the list
    Arguments:
        exp1,exp2                          The given terms to be multiply

    Returns:
        res                                a refined list
    '''
    res = []
    for i in exp1:
        for j in exp2:
            temp = mintermsProduct(i,j)
            res.append(temp) if len(temp) != 0 else None
    return res

def findEssentialPrimeImplicants(primeChart):
    '''
    Description:                            finds essential prime implicants the chart for it to be displayed
    Arguments:
        primeChart                          prime implicants chart

    Returns:
        res                                 a refined list
    '''
    res = []
    for i in primeChart:
        if len(primeChart[i]) == 1:
            res.append(primeChart[i][0]) if primeChart[i][0] not in res else None
    return res

def removeDontCares(givenList,dontCareList):
    '''
    Description:                            removes the don't care terms from the list
    Arguments:
        givenList, dontCareList             list to be edited, dont care list

    Returns:
        res                                 a refined list
    '''
    res = []
    for i in givenList:
        if int(i) not in dontCareList:
            res.append(i)
    return res

def removeMultidimensions(groupCopy):
    '''
    Description:                            This Function removes the multidimensions in a list
    Arguments:
        groupCopy                           accepts a copy of a group and flattens the list

    Returns:
        flattened_items                     returns the a flattened list
    '''
    flattened_items = []
    for i in groupCopy:
        flattened_items.extend(groupCopy[i])
    return flattened_items

def transformMintermToVariables(iteration, variable):
    '''
    Description:                         find variables in a minterm (For example, the minterm --01 has C' and D as variables)
    Arguments:
        iteration, variable              number from an iteration. The variable that will be passed for the final output

    Returns:
        var_list                         variable list 
    '''
    ascii = ord(variable)
    var_list = []
    for i in range(len(iteration)):
        if iteration[i] == '0':
            var_list.append(chr(i+ascii)+"'")
        elif iteration[i] == '1':
            var_list.append(chr(i+ascii))
    return var_list

def findMergedMinterms(iteration):
    '''
    Description:                            finds which minterms are merged. For example, 10-1 is obtained by merging 9(1001) and 11(1011)
    Arguments:
        iteration                           Accepts the number from an iteration

    Returns:
        temp                                a temporary list
    '''
    gaps = iteration.count('-')
    if gaps == 0:
        return [str(int(iteration,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = iteration[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

def deleteCoveredMinterms(chart,terms):
    '''
    Description:                            removes minterms which are already covered from chart
    Arguments:
        chart, terms                       chart, terms to check

    Returns:
                                            chart with removed redundant minterms
    '''
    for i in terms:
        for j in findMergedMinterms(i):
            try:
                del chart[j]
            except KeyError:
                pass

def compareMinterms(minterm1,minterm2):
    '''
    Description:                          function for checking if 2 minterms that differs by 1 bit only
    Arguments:
        minterm1, minterm2                                minterm inputs to compare

    Returns:
        True, mismatch_index                boolean value (hindi ko alam)
    '''
    c = 0
    for i in range(len(minterm1)):
        if minterm1[i] != minterm2[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True, mismatch_index)

def groupMinterms(minterms, groups, size):
    '''
    Description:                            groups the primary minterms 
    Arguments:
        minterms, groups, size              the entered minterms plus dontCC, groupMintermss, get size

    Returns:
        None
    '''
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
    # Primary groupMinterms ends

def convertToString(tup):
    '''
    Description:                            This is an auxiliary Function that converts a tuple into a string 
    Arguments:
        tup                                 The tuple that will be converted

    Returns:
        str                                 Returns the prime implicants and the primary answer                                  
    '''
    st = ''.join(map(str, tup))
    return st

def printPrimaryGroup(groups):
    '''
    Description:                            print the primary groups
    Arguments:
        groups                              groupMintermss of minterms

    Returns:
        None
    '''
    
    var3 = ''
    var1 = "\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s"%('='*43)
    for i in sorted(groups.keys()):
        var3 += "\n"+"%5d:"%i+"\n" # Prints group number
        for j in groups[i]:
            var3 +="\n"+"\t\t\t    %-20d\t%s"%(int(j,2),j)+"\n" # Prints minterm and its binary representation
        var3 += "\n"+'-'*60+ "\n"
    return var1+var3

def printPrimeImplicantsChart(enter_minterms, all_prime, enter_dontCC, variable):
    '''
    Description:                            last function for printing and processing of Prime Implicant chart
    Arguments:
        enter_minterms, all_prime,          The minterms that was inputed, the dont care conditions,
        enter_dontCC, variabble             and all the prime implicants calculated 

    Returns:
        str1 + str2 + str3 +str4            Returns ina concatenated style the printed output of the tables                                  
    '''
    sz = len(str(enter_minterms[-1])) # The number of digits of the largest minterm
    chart = {}
    tuple1 = '\n\n\nPrime Implicants chart:\n\n    Minterms\n'+'='*(len(enter_minterms)*(sz+1)+16)
    str1 = convertToString(tuple1) + "\n"
    str2 = ''
    strlength = len(enter_minterms)
    str5 = []

    for i in all_prime:
        merged_minterms,y = findMergedMinterms(i), 0
        end =''    
        tuple2 ="         %-26s"%', '.join(merged_minterms), end            
        str2 += convertToString(tuple2)
        str5 = [' - ']* strlength
        for j in removeDontCares(merged_minterms,enter_dontCC):
            x = enter_minterms.index(int(j))*(sz+2) # The position where we should put 'X'
            str5[enter_minterms.index(int(j))] = ' X '
            

            y = x + sz
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
        str2 += ''.join(str5)
        str2 += '\n'+'-'*(len(enter_minterms)*(sz+1)+16)+ "\n"


    EPI = findEssentialPrimeImplicants(chart) # Finding essential prime implicants
    tuple3 = "\nEssential Prime Implicants: "+', '.join(str(i) for i in EPI)
    str3 = convertToString(tuple3)+"\n"
    
    deleteCoveredMinterms(chart,EPI) # Remove EPI related columns from chart


    if(len(chart) == 0): # If no minterms remain after removing EPI related columns
        final_result = [transformMintermToVariables(i, variable) for i in EPI] # Final result with only EPIs
    else: # go for further simplification
        P = [[transformMintermToVariables(j, variable) for j in chart[i]] for i in chart]
        J = [[transformMintermToVariables(j, variable) for j in chart[i]] for i in chart]
        while len(P)>1: # Keep multiplying until we get the Some of Peoducts form of P
            P[1] = expressionProduct(P[0],P[1])
            P.pop(0)
        try:
            final_result = [min(P[0],key=len)] # Choosing the term with minimum variables from P
            final_result.extend(transformMintermToVariables(i, variable) for i in EPI) # Adding the EPIs to final solution
        except Exception as e:
            final_result=(transformMintermToVariables(i, variable) for i in EPI) # Adding the EPIs to final solution
    
    tuple4 = '\n\nSimplified Answer: F = '+' + '.join(''.join(i) for i in final_result)
    str4 = convertToString(tuple4)+"\n"
    return str1 + str2 + str3 +str4

#Main
def driver(variable, minterms, dontCare, sizing):
    '''
    Description:                        The main function is the one responsible for setting up the
                                        tabular method program., initializing the minterms and calling
                                        the functions within the program                             
    Arguments:
        Variable, minterms,              
        dontCare, sizing         

    Returns:
        None
    '''
    try:
        #for entering given
        enter_minterms = [int(i) for i in minterms.strip().split()]
        
        enter_dontCC = [int(i) for i in dontCare.strip().split()]
        enter_minterms.sort()
        minterms = enter_minterms + enter_dontCC
        minterms.sort()
        size = int(sizing)
        groups, all_prime = {}, set()

        #Function call for primary groupMinterms of minterms
        groupMinterms(minterms, groups, size)   
        #Function call for primary group printing
        globalVariables.var4 = printPrimaryGroup(groups)

        # Process for creating tables and finding prime implicants starts
        num = 1
        while True:
            tmp = groups.copy()
            groups, key, marked, should_stop = {}, 0, set(), True
            l = sorted(list(tmp.keys()))

            for i in range(len(l)-1):
                for j in tmp[l[i]]: # Loop which iterates through current group elements
                    for k in tmp[l[i+1]]: # Loop which iterates through next group elements
                        compared = compareMinterms(j,k) # Compare the minterms
                        if compared[0]: # If the minterms differ by 1 bit only
                            try:
                                # Put a '-' in the changing bit and add it to corresponding group
                                groups[key].append(j[:compared[1]]+'-'+j[compared[1]+1:]) if j[:compared[1]]+'-'+j[compared[1]+1:] not in groups[key] else None 
                            except KeyError:
                                # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                                groups[key] = [j[:compared[1]]+'-'+j[compared[1]+1:]] 
                            should_stop = False
                            marked.add(j) # Mark element j
                            marked.add(k) # Mark element k
                key += 1

            local_unmarked = set(removeMultidimensions(tmp)).difference(marked) # Unmarked elements of each table
            all_prime = all_prime.union(local_unmarked) # Adding Prime Implicants to global list
            # Printing Prime Implicants of current table
            globalVariables.space = "\n\n"
            globalVariables.status = "STATUS OF EACH TABLE:\n"
            tuple = "\nUnmarked elements(Prime Implicants) of table "+ str(num) +":\n",None if len(local_unmarked)==0 else ', '.join(local_unmarked) +'.'
            globalVariables.unmarked1 += convertToString(tuple)+"\n"
            if (num == 1):
                globalVariables.var4 += convertToString(tuple)+"\n"
            elif (num == 2):
                globalVariables.var5 += convertToString(tuple)+"\n"
            else:
                globalVariables.var6 += convertToString(tuple)+"\n"
            

            if should_stop: # If the minterms cannot be combined further
                # Print all prime implicants
                tuple02 = "\n\nAll Prime Implicants:\n ",None if len(all_prime)==0 else ', '.join(all_prime) 
                globalVariables.txt = convertToString(tuple02)
                break

            # Printing of all the next groups 
            vari3 = ''
            vari1 = "\n\n\n\nGroup No.             Minterms            Binary of Minterms\n"
            vari2 = '='*43+"\n"
            for i in sorted(groups.keys()):
                vari3 += "     %5d:"%i+ "\n" # Prints group number
                for j in groups[i]:
                    vari3 += "\t\t\t\t%-24s     %s"%(','.join(findMergedMinterms(j)),j)+"\n" # Prints minterms and its binary representation
                vari3 +=  "\n"+'-'*43+ "\n"
            if (num == 1):
                globalVariables.var5 = vari1+vari2+vari3
            else:
                globalVariables.var6 += vari1+vari2+vari3
            
            num += 1
            # Printing of all the next groups ends
        # Process for creating tables and finding prime implicants ends



        #Function call for printing and processing of Prime Implicant chart
        globalVariables.chart = printPrimeImplicantsChart(enter_minterms, all_prime, enter_dontCC, variable)
    except Exception as e:
        globalVariables.error = "\n\n\nInput error!"
    

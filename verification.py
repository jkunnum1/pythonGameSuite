

def emailVerify(rawEmail):
    checkEmail = rawEmail.replace('@', '')
    checkEmail = checkEmail.replace('.', '')
    charsValid = checkEmail.isalnum()

    if rawEmail != '' and ' ' not in rawEmail and charsValid:

        splitSymbol = rawEmail.split('@')
        if len(splitSymbol) == 2 and splitSymbol[0] != '':
            validSymbolLen = True
        else:
            validSymbolLen = False

        splitDomain = rawEmail.split('.')
        # Index of -1 is used to get the last element of the list.
        # The list  is checked to make sure it is only 2 elements long,
        # and the use of -1 prevents an indexing error when checking the
        # length of the last element.
        # The splitDomain[0][-1] is used to ensure there is a domain name
        # in the email, that it doesnt end with @.com
        if len(splitDomain) == 2 and splitDomain[0][-1] != '@' \
           and(len(splitDomain[-1]) == 2 or len(splitDomain[-1]) == 3) \
           and splitDomain[-1].isalpha():
            validDomainLen = True
        else:
            validDomainLen = False

        valid = validDomainLen and validSymbolLen

    else:
        valid = False

    return valid

def verify(info, users):
    if info[0] in users or info[0] == '':
        validUser = False
    else:
        validUser = True
    if info[1] == info[2] and len(info[1]) > 4:
        passMatch = True
    else:
        passMatch = False
    if info[3] != '':
        validFirstName = True
    else:
        validFirstName = False
    if info[4] != '':
        validLastName = True
    else:
        validLastName = False
    validEmail = emailVerify(info[5])
    if not info[6].isdigit():
        validAge = False
    else:
        validAge = True
    results = [validUser, passMatch, validFirstName, validLastName, validEmail,
               validAge]
    return results

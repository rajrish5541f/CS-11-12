'''Converts miles to kms and vice-versa, and converts inches to feet and  vice-versa. '''

#functions
def milestokm(value:[int]):
    '''Converts given value(in miles) to kms.'''
    return (value*onemileintokms)

def kmstomiles(value:[int]):
    '''Converts given value(kms) to miles.'''
    return (value/onemileintokms)

def feettoinch(value:[int]):
    '''Converts given value(feets) to inches.'''
    return (value*onefeetintoinch)

def inchestofeet(value:[int]):
    '''Converts given value(inches) to feet.'''
    return (value/onefeetintoinch)

#constants
onemileintokms = 1.609344
onefeetintoinch = 12

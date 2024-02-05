
#can make this more complicated based on regressive tax system
def calculateTaxIncome(income):
    return income*.75

#assume contributionPercents is a dict
def calculateContribution(contributionPercents, income):
    if type(contributionPercents) != dict:
        raise TypeError("Only dictionaries are allowed for contributionPercents")
    else:
        contributions = contributionPercents['pretax']*income
        posttax = calculateTaxIncome(income)
        contributions += (contributionPercents['aftertax']+contributionPercents['roth'])*posttax
        return contributions/12
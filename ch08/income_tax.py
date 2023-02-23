''' calculate someone's federal income tax liability '''

from decimal import Decimal

brackets = {
'single': [
(10, Decimal(0), Decimal(10275), Decimal(0.0)),
(12, Decimal(10276), Decimal(41775), Decimal(1027.5)),
(22, Decimal(41776),  Decimal(89075), Decimal(4807.5)),
(24, Decimal(89076), Decimal(170050), Decimal(15213.5)),
(32, Decimal(170051), Decimal(215950), Decimal(34647.5)),
(35, Decimal(215951), Decimal(539900), Decimal(49335.5)),
(37, Decimal(539901), Decimal(5000000000000000000), Decimal(162718.0))
],
'married_jointly': [
(10,Decimal(0), Decimal(20550), Decimal(0)),
(12,Decimal(20551), Decimal(83550), Decimal(2055)),
(22,Decimal(83551), Decimal(178150), Decimal(9615)),
(24,Decimal(178151), Decimal(340100), Decimal(30427)),
(32,Decimal(340101), Decimal(431900), Decimal(69295)),
(35,Decimal(431901), Decimal(647850), Decimal(98671)),
(37,Decimal(647851), Decimal(5000000000000000000), Decimal(174253.50)) 
]
}

def calculate_income_tax(income, filing_status='single', standard_deduction=12950):
    ''' calculate total tax '''
    total_tax = Decimal('0')
    adjusted_income = Decimal(income) - Decimal(standard_deduction)
    for i in brackets[filing_status]:
        if adjusted_income > i[1] and adjusted_income < i[2]:
            total_tax += Decimal(i[3])
            total_tax += Decimal(i[0]/100) * Decimal(adjusted_income - i[1])
    return total_tax
 

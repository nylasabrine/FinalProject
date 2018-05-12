'''
Created on Mar 10, 2018

@author: ITAUser
'''
def tax(filing_status, income):
    if filing_status == 'single':
        if (income >= 0) and (income <=9275):
            tax = (0.1*income)
        elif (income > 9276) and (income <= 36750):
            tax = (0.1*9275) + (0.15*(income - 9275))
        elif (income > 37651) and (income <= 91150):
            tax = (0.1*9275) + (0.15*(37650-9275)) + (0.25*(income - 37650))
        elif (income > 91151) and (income<=190150):
            tax = (0.1*9275) + (0.15*(37650-9275)) + (0.25*(91150-37651)) + (0.28*(income - 91151))
        elif (income > 190151) and (income<=413350):
            tax = (0.1*9275) + (0.15*(37650-9275)) + (0.25*(91150-37651)) + (0.28*(190150 - 91151)) + (0.33*(income - 190151))
        elif (income > 413351) and (income<=415040):
            tax = (0.1*9275) + (0.15*(37650-9275)) + (0.25*(91150-37651)) + (0.28*(190150 - 91151)) + (0.33*(413350 - 190151)) + (0.35*(income - 413351))
        elif (income > 415051): 
            tax = (0.1*9275) + (0.15*(37650-9275)) + (0.25*(91150-37651)) + (0.28*(190150 - 91151)) + (0.33*(413350 - 190151)) + (0.35*(415050 - 413351)) + (0.396*(income - 415051))
    
    elif filing_status == 'married filing jointly':
        if (income >= 0) and (income <=18550):
            tax = (0.1*income)
        elif (income > 18551) and (income <= 75300):
            tax = (0.1*18550) + (0.15*(income - 18551))
        elif (income > 75301) and (income <= 151900):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(income - 75301))
        elif (income > 151901) and (income<=23140):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(income - 151901))
        elif (income > 231451) and (income<=413350):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(income - 231451))
        elif (income > 143351) and (income<=466950):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(413350 - 231451)) + (0.35*(income - 413351))
        elif (income > 466951): 
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(413350 - 231451)) + (0.35*(466950 - 413351) + (0.396*(income -466951))
        
    elif filing_status == 'qualifying widower':
        if (income >= 0) and (income <=18550):
        tax = (0.1*income)
        elif (income > 18551) and (income <= 75300):
            tax = (0.1*18550) + (0.15*(income - 18551))
        elif (income > 75301) and (income <= 151900):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(income - 75301))
        elif (income > 151901) and (income<=23140):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(income - 151901))
        elif (income > 231451) and (income<=413350):
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(income - 231451))
        elif (income > 143351) and (income<=466950)
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(413350 - 231451)) + (0.35*(income - 413351)
        elif (income > 466951) 
            tax = (0.1*18550) + (0.15*(75300 - 18551)) + (0.25*(151901 - 75301)) + (0.28*(231450 - 151901)) + (0.33*(413350 - 231451)) + (0.35*(466950 - 413351) + (0.396*(income -466951))  
            
    elif filing_status == 'Married filing separately':
        if (income >= 0) and (income <=9275):
        tax = (0.1*income)
        elif (income > 9276) and (income <= 37650):
            tax = (0.1*9275) + (0.15*(income - 9276))
        elif (income > 37651) and (income <= 75950):
            tax = (0.1*9275) + (0.15*(37650 - 9276)) + (0.25*(income - 37651))
        elif (income > 75951) and (income<=115725):
            tax = (0.1*9275) + (0.15*(37650 - 9276)) + (0.25*(75950 - 37651)) + (0.28*(income - 75951))
        elif (income > 115726) and (income<=206675):
            tax = (0.1*9275) + (0.15*(37650 - 9276)) + (0.25*(75950 - 37651)) + (0.28*(115725 - 75951)) + (0.33*(income - 115726))
        elif (income > 206676) and (income<=233475)
            tax = (0.1*9275) + (0.15*(37650 - 9276)) + (0.25*(75950 - 37651)) + (0.28*(115725 - 75951)) + (0.33*(206675 - 115726)) + (0.35*(income - 206676)
        elif (income > 233476) 
            tax = (0.1*9275) + (0.15*(37650 - 9276)) + (0.25*(75950 - 37651)) + (0.28*(115725 - 75951)) + (0.33*(206675 - 115726)) + (0.35*(233475 - 206676) + (0.396*(income - 233476))
                                                                                                                                      
    elif filing_status == 'head of household':
        if (income >= 0) and (income <=13250):
        tax = (0.1*income)
        elif (income > 13251) and (income <= 50400):
            tax = (0.1*13250) + (0.15*(income - 13251))
        elif (income > 50401) and (income <= 130150):
            tax = (0.1*13250) + (0.15*(50400 - 13251)) + (0.25*(income - 50401))
        elif (income > 130151) and (income<=210800):
            tax = (0.1*13250) + (0.15*(50400 - 13251)) + (0.25*(130150 - 50401)) + (0.28*(income - 130151))
        elif (income > 210801) and (income<=413350):
            tax = (0.1*13250) + (0.15*(50400 - 13251)) + (0.25*(130150 - 50401)) + (0.28*(210800 - 130151)) + (0.33*(income - 210801))
        elif (income > 413351) and (income<=441000)
            tax = (0.1*13250) + (0.15*(50400 - 13251)) + (0.25*(130150 - 50401)) + (0.28*(210800 - 130151)) + (0.33*(413350 - 210801)) + (0.35*(income - 413351)
        elif (income > 441001) 
            tax = (0.1*13250) + (0.15*(50400 - 13251)) + (0.25*(130150 - 50401)) + (0.28*(210800 - 130151)) + (0.33*(413350 - 210801)) + (0.35*(441000 - 413351) + (0.396*(income - 441001))                                                                                                                              
    return tax
def percentage_of_tax(tax, income):
    return((tax/income)*100)
def is_valid(filing_status, income):

    if(income < 0):
        return False
    elif (filing_status != "single") and 
    (filing_status != "married filing jointly")
    (filing_status != "qualifying widower")
    (filing_status != "married filing separately")
    (filing_status != "head of household"))
        return False
    return True
def main(filing_status, income):
    if is_valid(filing_status, income):
        tax_value = tax(filing_status, income)
        percent_value = percent_of_income(tax_value,income)
        print ('Tax: $' str(tax_value))
        print('Tax as % of income:' + str(percent_value + "%"))
    else:
        print ("invalid filing status")
        print ("Income must be greater than or equal to zero")
        
filing_status: input ("What is your filing status?")
income :(int(input("What is your income?")))
if(is_valid(filing_status, income)):
    print(tax(filing_status,income))
        
    
    
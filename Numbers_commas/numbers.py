def remove_float(number):
    number= float(number)
    num = float("{:.2f}".format(number))
    number_str= str(num)
    return number_str[-3:]


def set_commas_nep(number): #1223456
    temp= number
    #number= number%1000
    temp=temp/1000
    nepali_num= str(int(number)%1000)
    while(int(temp)!=0):
        temp2= temp%100
        temp= temp/100
        int_val= int(temp2)
        string_val= str(int_val)
        nepali_num= string_val+","+nepali_num
    #to store the string in rev order
    # nepali_rep=""
    # nepali_rep= nepali_num[::-1]
    return nepali_num

def set_commas_inter(number): #1223456
    temp= number
    #number= number%1000
    temp=temp/1000
    inter_num= str(int(number)%1000)
    while(int(temp)!=0):
        temp2= temp%1000
        temp= temp/1000
        int_val= int(temp2)
        string_val= str(int_val)
        inter_num= string_val+","+inter_num
    #to store the string in rev order
    # nepali_rep=""
    # nepali_rep= nepali_num[::-1]
    return inter_num    
    
        
    
input_number= float( input('Enter a number:'))
number_float_removed= remove_float(input_number)
nepali_number= set_commas_nep(input_number)
inter_number= set_commas_inter(input_number)
print(number_float_removed)

#concatenation of results
result_nep= nepali_number+number_float_removed
print(result_nep)
result_inter= inter_number+number_float_removed
print(result_inter)

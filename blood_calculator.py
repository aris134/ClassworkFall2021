def interface():
    print("Blood Calculator:")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("3 - TC Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        elif choice == 3:
            TC_Driver()
            
    print(choice)
    return choice
    

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)
    
def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value
    
def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_answer))
    return

def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)
    
def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value
    
def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"

def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))
    return

def TC_Driver():
    TC_value = tc_input()
    TC_character = tc_analysis(TC_value)
    tc_output(TC_value, TC_character)
    
def tc_input():
    tc_value = int(input("Enter TC Value: "))
    return tc_value
    
def tc_analysis(TC_value):
    if TC_value < 200:
        return "Normal"
    elif 200 <= TC_value <= 239:
        return "Borderline High"
    else:
        return "High"

def tc_output(TC_value, TC_answer):
    print("The TC value of {} is considered {}".format(TC_value, TC_answer))
    return    
    
interface()
   
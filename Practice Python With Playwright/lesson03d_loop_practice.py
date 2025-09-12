test_results = ["Pass", "Pass", "Fail", "Pass", "Fail", "Fail"]
for i in range (len(test_results)):
    if test_results[i]=="Pass":
        print("testcase" ,i+1,"!", test_results[i])
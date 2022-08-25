import numbers


def arithmetic_arranger(problems,outcome=False):
  print(problems)

  all_problem_list = []
  
  #Test zuviele Probleme
  if len(problems)>5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  
  for problem in problems:
    section_problem = problem.split()
    math = section_problem[1]
  
    #Test falscher Matheoperator
    if (math != "+" or math == "-") and (math == "+" or math != "-"):
      all_problem_list = "Error: Operator must be '+' or '-'."
      return all_problem_list
    
    #Test zuviele Zahlen
    if len(section_problem[0])>4 or len(section_problem[2])>4:
      all_problem_list = "Error: Numbers cannot be more than four digits."
      return all_problem_list
    
    #Test Zeichen in einer Zahl
    if section_problem[0].isnumeric() == False or section_problem[2].isnumeric() == False:
      all_problem_list = "Error: Numbers must only contain digits."
      return all_problem_list
    
    
    num1 = int(section_problem[0])
    num2 = int(section_problem[2])
        
    if math == "+":
      result = num1 + num2
    else:
      result = num1 - num2
      
    #Separierung der Einzelnen Zahlen abgeschlossen
    
    max = len(section_problem[0])+2
    if len(section_problem[2])+2 > max:
      max = len(section_problem[2])+2
    elif len(str(int(result))) > max and outcome==True:
      max = str(int(result))
    
    #Zusammenfügung in Liste
    problem_list = [int(num1),str(math),int(num2),int(result),int(max)] 
    
    
    all_problem_list.append(problem_list)
    
  print("Problemliste:\n"+str(problem_list))
  num_all_elements = len(all_problem_list)
  
  #Alles in eigene Listen verpacken
  list_num1 = []
  list_math= []
  list_num2 = []
  list_results = []
  list_length = []
   
  for i in range (0, num_all_elements):
    list_num1.append(all_problem_list[i][0])
    list_math.append(all_problem_list[i][1])
    list_num2.append(all_problem_list[i][2])
    list_results.append(all_problem_list[i][3])
    list_length.append(all_problem_list[i][4])
  
  #print(list_math)
  line_1 = []
  line_2 = []
  line_3 = []
  line_4 = []
  
  #Einzelne reihen erstellen
  for i in range (0, num_all_elements):
        
    if list_length[i] > len(str(list_num1[i])):
      line_1.append(' '*(list_length[i]-len(str(list_num1[i]))) + str(list_num1[i]))
    else:
      line_1.append(str(list_num1[i]))
    
    if list_length[i] > len(str(list_num2[i]))+2:    
      line_2.append(list_math[i]+" "+" "*(list_length[i]-(len(str(list_num2[i]))+2))+str(list_num2[i]))
    else:
      line_2.append(list_math[i]+" "+str(list_num2[i]))
      
    line_3.append("-"*list_length[i])
    
    if list_length[i] > len(str(list_results[i])):
      line_4.append(" "*(list_length[i]-len(str(list_results[i])))+str(list_results[i]))
    else:
      line_4.append(str(list_results[i]))
      
  line_1 = "    ".join(line_1)
  line_2 = "    ".join(line_2)
  line_3 = "    ".join(line_3)
  line_4 = "    ".join(line_4)
  
  arranged_problems = line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4 if outcome == True else line_1+'\n'+line_2+'\n'+line_3
  return arranged_problems
def arithmetic_arranger(problems, is_include_results=False):
    if not isinstance(problems, list):
        return "Error: Argument 'problems' should be of type list."
    if len(problems) > 5:
        return "Error: Too many problems."
    

    # Check and extract the values from 'problems'
    operand_Xs = list()
    operators = list()
    operand_Ys = list()
    base_lens = list()
    results = list()
    
    for problem in problems:
        pieces = problem.split()

        if not len(pieces) == 3:
            return "Error: The format of expression '" + problem + "' is invalid."
        if pieces[1] not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        if not pieces[0].isdigit() or not pieces[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(pieces[0]) > 4 or len(pieces[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        base_len = 0
        if len(pieces[0]) > len(pieces[2]):
            base_len = len(pieces[0])
        else:
            base_len = len(pieces[2])

        operand_X = int(pieces[0])
        operand_Y = int(pieces[2])
        result = 0
        if pieces[1] == "+":
            result = operand_X + operand_Y
        else:
            result = operand_X - operand_Y
        str_result = str(result)

        operand_Xs.append(pieces[0])
        operators.append(pieces[1])
        operand_Ys.append(pieces[2])
        base_lens.append(base_len)
        results.append(str_result)
    

    # Arrange the problems and optional results
    arranged_problems = ""
    
    for i in range(len(problems)):
        arranged_problems = arranged_problems + operand_Xs[i].rjust(base_lens[i] + 2)
        if i < len(problems) - 1:
            arranged_problems = arranged_problems + "    "
    arranged_problems = arranged_problems + "\n"

    for i in range(len(problems)):
        arranged_problems = arranged_problems + operators[i]
        arranged_problems = arranged_problems + operand_Ys[i].rjust(base_lens[i] + 1)
        if i < len(problems) - 1:
            arranged_problems = arranged_problems + "    "
    arranged_problems = arranged_problems + "\n"

    for i in range(len(problems)):
        arranged_problems = arranged_problems + "-" * (base_lens[i] + 2)
        if i < len(problems) - 1:
            arranged_problems = arranged_problems + "    "
    if is_include_results:
        arranged_problems = arranged_problems + "\n"

    if is_include_results:
        for i in range(len(problems)):
            arranged_problems = arranged_problems + results[i].rjust(base_lens[i] + 2)
            if i < len(problems) - 1:
                arranged_problems = arranged_problems + "    "


    return arranged_problems

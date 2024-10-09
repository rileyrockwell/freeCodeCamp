def arithmetic_arranger(problems, show_answers=True):
    for expression in problems:
        split = expression.split(" ")
        a = int(split[0])
        b = int(split[-1])
        operator = split[1]

        if operator == "+":
            result = a + b

        if operator == "-":
            result = a - b

        total_digits = max(len(list(str(a))), len(list(str(b))))

        divider = total_digits + 2
        divider = "-"*divider

        first_line = ""
        second_line = ""
        third_line = ""
        fourth_line = ""

        for expression in problems:
            split = expression.split(" ")
            a = split[0]
            b = split[-1]
            operator = split[1]

            total_digits = max(len(a), len(b))
            width = total_digits + 2

            first_line += str(a).rjust(width) + "    "
            second_line += operator + " " + str(b).rjust(total_digits) + "    "
            third_line += "-" * width + "    "
            if show_answers:
                result = str(eval(expression))
                fourth_line += result.rjust(width) + "    "

        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
        if show_answers:
            arranged_problems += "\n" + fourth_line.rstrip()

        return arranged_problems


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print()
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

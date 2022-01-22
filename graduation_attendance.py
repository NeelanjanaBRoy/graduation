def get_graduation_absent_prob(n):
    """
        This function calculates the probability of a student missing graduation

        When the student is absent at the graduation ceremony itself that means we need to check
        whether the last combination is A or Absent (for n < 4 , we can use 2 ^ (n - 1))

        There is  1 combination 'AAAA' which will not allow graduation to occur, hence we will subtract 1 from total
        combination [A= Absent, P = Present] (for n = 4 , we can use 2 ^ (n - 1) - 1)

        For n > 5, we can divide the problem into sub problems and use recursion to reach probability for each iteration

        Parameters:
        n (int): Total number of days in an academic year

        Returns:
        int: Returns total probability a student will miss graduation

    """
    if n < 4:
        return 2 ** (n-1)
    if n == 4:
        return (2 ** (n-1)) - 1
    if n in miss:
        return miss[n]
    else:
        miss[n] = get_graduation_absent_prob(n - 4) + get_graduation_absent_prob(n - 3) + get_graduation_absent_prob(
            n - 2) + get_graduation_absent_prob(n - 1)
    return miss[n]


def get_graduation_attend_prob(n):
    """
         This function calculates the number of ways to attend classes over N days

         As per problem we cannot allow any student to miss more than or equal to 4 consecutive days
         which means that when n is less than 4, there is no way a student would miss his/her graduation
         (for n < 4, we can use 2 ^ n )

        There is  1 combination 'AAAA' which will not allow graduation to occur, hence we will subtract 1 from total
        combination [A= Absent, P = Present] (for n == 4, we can use 2 ^ n - 1)

        For n > 5, we can divide the problem into sub problems and use recursion to reach probability for each
        iteration

        Parameters:
        n (int): Total number of days in an academic year

        Returns:
        int: Returns number of ways to attend classes over N days

    """
    if n < 4:
        return 2 ** n
    if n == 4:
        return (2 ** n) - 1
    if n in attend:
        return attend[n]
    else:
        attend[n] = get_graduation_attend_prob(n - 4) + get_graduation_attend_prob(n - 3) + get_graduation_attend_prob(
            n - 2) + get_graduation_attend_prob(n - 1)
    return attend[n]


def get_graduation_probability(days):
    """
         This function returns the solution of get_graduation_absent_prob(n) / get_graduation_attend_prob(n) as a string

        Parameters:
        days (string): Total number of days in an academic year, as read from input.txt, line by line

        Prints:
        get_graduation_absent_prob(n) / get_graduation_attend_prob(n) as a string (not reducing fraction as a decimal)

    """
    for n in days:
        print(str(get_graduation_absent_prob(int(n))) + "/" + str(get_graduation_attend_prob(int(n))))


if __name__ == "__main__":
    miss = dict()
    attend = dict()
    input_file = open("input.txt", "r")
    days_in_academic_year_list = input_file.readlines()
    get_graduation_probability(days_in_academic_year_list)

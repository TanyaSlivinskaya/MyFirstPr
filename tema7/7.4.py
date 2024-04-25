"""Дан список строк. С помощью filter() получить список тех
строк из исходного списка, которые являются палиндромами
(читаются в обе стороны одинаково, например, ’abcсba’)"""

def polind(s):
    if s == s[::-1]:
        return True


print(list(filter(polind, ["lol", "mvdjvndf", "fvdbvfdvbd", "mem"] )))
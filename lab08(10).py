s ='+7 (812) 134-12-324'
chars='()- '
res=s.translate(str.maketrans('','', chars))
print(res)
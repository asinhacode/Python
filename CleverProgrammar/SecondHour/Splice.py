problems = 'b, a, t, t, e, r'
print(problems)

l = problems.split(", ")  # convert into a list
print(l)

# convert list into String
joined = ' and '.join(l)
print(joined)

joined2 = ' and a, '.join(l);
print(joined2)
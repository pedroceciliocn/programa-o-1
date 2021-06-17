from pytictoc import TicToc
t = TicToc()
t.tic()
squares = [value**2 for value in range(33550336)]
t.toc()
print(t)
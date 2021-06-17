from pytictoc import TicToc
t = TicToc()
squares = []
t.tic()
for value in range(1, 33550336):
    squares.append(value)
t.toc()
print(t)
"""
.upper() até o primeiro espaço e depois .upper() iniciando da última letra até o primeiro espaço

.rfind() encontra começando da direita


s = "On the other hand, you have different fingers."
s. find("hand")
13  #The results tell us that “hand” begins at the 13th position in the sequence.

But if we want to find the second “o” we need to specify a range.
s.find("o", 8)
20

This begins searching at the 8th element and finds “o” at 20. You can also specificy an end to the range, and, like
slicing, we can do so backwards:
s.find("e", 20, -5)
26
"""
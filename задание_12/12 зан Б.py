def find_second_largest(seq):
    if len(seq) <= 1:
        return None

    max_num = max(seq)
    seq.remove(max_num)
seq=[]
print(max_num)

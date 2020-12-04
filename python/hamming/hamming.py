def distance(strand_a, strand_b):
    if strand_a == strand_b:
        return 0
    elif len(strand_a) != len(strand_b):
        raise ValueError("Strands must be same length.")
    else:
        index = 0
        count = 0
        for char_a in strand_a:
            if char_a != strand_b[index]:
                count += 1
                index += 1
            else:
                index += 1        
        return count
 
            


        
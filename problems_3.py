def count_char_freq(input):
    output = {}
    for i in input:
        if i in output:
            output[i] = output[i] + 1
        else:
            output.update({i : 1})
    return output

def is_anagram(input_1, input_2):
    output_1 = count_char_freq(input_1)
    output_2 = count_char_freq(input_2)

    if len(output_1) != len(output_2):
        return False
    for o in output_1:
        if o not in output_2:
            return False 
        if output_1[o] != output_2[o]:
            return False
    return True

def invert_dict(input):
    output = {}
    for k, v in input.items():
        output.update({v:k})
    return output
    
def merge_dict(d1,d2):
    merged_dict = {}
    for k,v in d1.items():
        merged_dict[k] = v
    for k,v in d2.items():
        merged_dict[k] = v
    return merged_dict
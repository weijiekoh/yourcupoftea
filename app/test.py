from qns_parties_positions import questions

def remove_duplicates(all_responses):
    fixed = []
    r = "radio_"
    for qn_id in reversed(questions.keys()):
        for n, v in reversed(all_responses):
            if n == "qn_id" and int(v[0]) == qn_id:
                fixed.append((n,v))
                break

    for qn_id in reversed(questions.keys()):
        for n, v in reversed(all_responses):
            if n.startswith(r):
                if int(n[len(r):]) == qn_id:
                    fixed.append((n,v))
                    break

    fixed.reverse()
    return fixed

if __name__ == "__main__":
    sample_data = [('qn_id', [u'0']), ('radio_0', [u'1']), 
                   ('qn_id', [u'0']), ('radio_0', [u'3']), 
                   ('qn_id', [u'1']), ('radio_1', [u'2']), 
                   ('qn_id', [u'1']), ('radio_1', [u'3']), 
                   ('radio_2', [u'3']), ('qn_id', [u'2'])]
    
    print remove_duplicates(sample_data)


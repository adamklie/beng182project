#grabs data from the file "pfam2go" and creates a dictionary for all the
#pfam numbers with their corresponding GO indentifiers
def parsePfamGO (filename):
    p2go = {}
    pfam2go = open(filename, 'r')
    for line in pfam2go:
        if line[0:4] == 'Pfam':
            header_array = line.split(' ')
            p_string = header_array[0]
            p_num = ''

            go_num = header_array[-1].strip()

            for index in range(0, len(p_string)):
                if p_string[index] == ':':
                    p_num = p_string[index+1:]

            go_term = ''
            for index in range(3, len(header_array) - 2):
                temp = header_array[index]
                if index == 3:
                    go_term += temp[3:].strip() + ' '
                elif index != 3:
                    go_term += temp.strip() + ' '

            go_final = go_term + '[' + go_num + ']'
            #print(go_final)

            p2go.setdefault(p_num, []).append(go_final)
    pfam2go.close()
    return p2go

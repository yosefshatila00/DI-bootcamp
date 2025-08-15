def trans_2d():
    MATRIX_STR = '''7ir
                    Tsi
                    h%x
                    i ?
                    sM# 
                    $a 
                    #t%'''

    matrix = []
    for line in MATRIX_STR.split('\n'):
        if line.strip(): 
            row = list(line.lstrip())  
            matrix.append(row)
    return matrix

def process_col(matrix):
    decoded_chars = []
    num_cols = len(matrix[0]) if matrix else 0
    
    for col in range(num_cols):
        for row in range(len(matrix)):
            char = matrix[row][col]
            if char.isalpha():
                decoded_chars.append(char)
            else:
                if decoded_chars and decoded_chars[-1].isalpha():
                    decoded_chars.append(' ')
    
    decoded_message = "".join(decoded_chars).strip()
    decoded_message = " ".join(decoded_message.split())
    return decoded_message


matrix = trans_2d()
print("Matrix structure:")
for row in matrix:
    print(row)

message = process_col(matrix)
print("\nDecoded message:", message)

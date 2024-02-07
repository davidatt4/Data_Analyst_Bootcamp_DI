#MATRIX
def decrypt_matrix(matrix):
    rows=matrix.split('\n')
    matrix_list=[list(row)for row in rows]
    
    num_rows=len(matrix_list)
    num_cols=max(len(row) for row in matrix_list)
    for row in matrix_list:
        row.extend(['']*(num_cols-len(row)))
        decrypted_message = ''
    for col in range(num_cols):
        for row in range(num_rows):
            char = matrix_list[row][col]
            if char.isalnum():
                decrypted_message += char
            else:
                # Replace symbols between two alpha characters with a space
                if decrypted_message and decrypted_message[-1] != ' ':
                    decrypted_message += ' '

    return decrypted_message

matrix_string="""7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

decrypted_message=decrypt_matrix(matrix_string)
print("Decrypted Message:",decrypted_message)

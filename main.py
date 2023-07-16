from geda_read import geda_read as gr
'''
Read the geda2 files and convert to kicad_sym files
Steps:
Read the files --done 
catagorise it to different symbol property
From the symbol property parse the symbol to a kicad readable s-expression

'''
# main()
if __name__ == '__main__':
    # print("hello world ")
    gread = gr()
    file = "R-0805.sym"
    lines = gread.read_sym_file(file)
    # gread.display(lines)
    gread.parse_file(file_name=file,line_arr=lines)
    gread.add_to_dictionary(line_arr=lines)

    
import os
import glob


index_path = os.path.join('.', "index.html")
input_dir = './images'
output_dir = '.'


def append_index():
    index = open(index_path, "w")
    index.write("<html><body><table><tr>")
    index.write("<th>name</th><th>#</th><th>input</th><th>output</th>\n")

    input_paths = glob.glob(os.path.join(input_dir, '*inputs.png'))
    input_paths = sorted(input_paths)
    
    print('input path num: ', len(input_paths))
    num = 1
    for input_path in input_paths:
        index.write("<tr>")
        
        basename = os.path.splitext(os.path.basename(input_path))[0][:6]
        
        output_path = os.path.join(input_dir, basename + 'outputs.png')

        

        print(input_path)
        print(output_path)

        if not (os.path.exists(input_path) 
                and os.path.exists(output_path) 
                ):
            continue        
        index.write("<td>%s</td>\n" % basename)
        index.write("<td>---[%d]---</td>\n" % num)
        num += 1
        index.write("<td><img src=\'%s\'></td>"  % input_path)
        index.write("<td><img src=\'%s\'></td>"  % output_path)


        index.write("</tr>\n")
    return index_path
    
append_index()
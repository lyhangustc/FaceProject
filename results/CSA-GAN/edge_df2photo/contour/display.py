import os
import glob


index_path = os.path.join('.', "index.html")
input_dir = './images'
output_dir = '.'
filename_patten = ['*targets.png']

def append_index():
    index = open(index_path, "w")
    index.write("<html><body><table><tr>")

    index.write("<th>name</th><th>#</th><th>edge</th><th>distance_field</th><th>output</th>\n")

    edge_paths = []
    for pat in filename_patten:
        edge_paths += glob.glob(os.path.join(input_dir, pat))
    edge_paths = sorted(edge_paths)
    
    num = 1
    for edge_path in (edge_paths):
        index.write("<tr>")
        
        basename = os.path.splitext(os.path.basename(edge_path))[0][:8]
        output_path = os.path.join(input_dir, basename + 'outputs.png')
        df_path = os.path.join(input_dir, basename + 'inputs.png')
        
        if not (os.path.exists(edge_path) and os.path.exists(output_path) and os.path.exists(df_path)):
            continue
        
        
        #index.write("<td>%s</td>\n" % basename)
        index.write("<td>---[%d]---</td>\n" % num)
        num += 1
        index.write("<td><img src=\'%s\'></td>"  % edge_path)
        index.write("<td><img src=\'%s\'></td>" % df_path)
        index.write("<td><img src=\'%s\'></td>" % output_path)

        index.write("</tr>\n")
    return index_path
    
append_index()
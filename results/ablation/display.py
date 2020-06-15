import os
import glob


index_path = os.path.join('.', "index.html")
baseline_dir = './exp0011_baseline/test_latest/images'
baseline_deform_dir = './exp0011_baseline_deform/test_latest/images'
full_dir = './exp0013_base/test_latest/images'


def append_index():
    index = open(index_path, "w")
    index.write("<html><body><table><tr>")
    index.write("<th>name</th>\
                <th>#</th>\
                <th>full_sketch</th>\
                <th>full_synthesized</th>\
                <th>full_sketch_deform</th>\
                <th>full_synthesized_deform</th>\
                <th>baseline_sketch</th>\
                <th>baseline_synthesized</th>\
                <th>baseline_sketch_deform</th>\
                <th>baseline_synthesized_deform</th>\
                <th>baseline_deform_sketch</th>\
                <th>baseline_deform_synthesized</th>\
                <th>baseline_deform_sketch_deform</th>\
                <th>baseline_deform_synthesized_deform</th>\
                \n")

    full_paths = glob.glob(os.path.join(full_dir, '*sketch.png'))
    full_paths = sorted(full_paths)
    
    print('input path num: ', len(full_paths))
    num = 1
    num_images = 3 # for test
    for full_path in full_paths[:num_images]:
        index.write("<tr>")
        
        basename = os.path.splitext(os.path.basename(full_path))[0][:6]  # 151415_sketch.png
        full_sketch = full_path
        full_sketch_deform = os.path.join(full_dir, basename + '_sketch_deform.png')
        full_synthesized = os.path.join(full_dir, basename + '_synthesized.png')
        full_synthesized_deform = os.path.join(full_dir, basename + '_synthesized_deform.png')
        
        baseline_sketch = os.path.join(baseline_dir, basename + '_sketch.png')
        baseline_sketch_deform = os.path.join(baseline_dir, basename + '_sketch_deform.png')
        baseline_synthesized = os.path.join(baseline_dir, basename + '_synthesized.png')
        baseline_synthesized_deform = os.path.join(baseline_dir, basename + '_synthesized_deform.png')

        baseline_deform_sketch = os.path.join(baseline_deform_dir, basename + '_sketch.png')
        baseline_deform_sketch_deform = os.path.join(baseline_deform_dir, basename + '_sketch_deform.png')
        baseline_deform_synthesized = os.path.join(baseline_deform_dir, basename + '_synthesized.png')
        baseline_deform_synthesized_deform = os.path.join(baseline_deform_dir, basename + '_synthesized_deform.png')

        

        print(full_sketch)
        print(baseline_sketch)
        print(baseline_deform_sketch)

        if not (os.path.exists(full_sketch) 
                and os.path.exists(baseline_sketch) 
                and os.path.exists(baseline_deform_sketch) 
                ):
            continue        
        index.write("<td>%s</td>\n" % basename)
        index.write("<td>---[%d]---</td>\n" % num)
        num += 1
        index.write("<td><img src=\'%s\'></td>"  % full_sketch)
        index.write("<td><img src=\'%s\'></td>"  % full_synthesized)
        index.write("<td><img src=\'%s\'></td>"  % full_sketch_deform)
        index.write("<td><img src=\'%s\'></td>"  % full_synthesized_deform)
        
        index.write("<td><img src=\'%s\'></td>"  % baseline_sketch)
        index.write("<td><img src=\'%s\'></td>"  % baseline_synthesized)
        index.write("<td><img src=\'%s\'></td>"  % baseline_sketch_deform)
        index.write("<td><img src=\'%s\'></td>"  % baseline_synthesized_deform)
        
        index.write("<td><img src=\'%s\'></td>"  % baseline_deform_sketch)
        index.write("<td><img src=\'%s\'></td>"  % baseline_deform_synthesized)
        index.write("<td><img src=\'%s\'></td>"  % baseline_deform_sketch_deform)
        index.write("<td><img src=\'%s\'></td>"  % baseline_deform_synthesized_deform)


        index.write("</tr>\n")
    return index_path
    
append_index()
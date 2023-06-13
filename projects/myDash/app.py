from flask import Flask, render_template
import os

#CREATES THE FLASK APPLICATION OBJECT CALLED 'app'. THE '__name__' variable is
#   A SPECIAL VARIBALE IN PYTHON THAT REPERESENTS THE CURRENT MODULE, WE SET OUR TO '__main__'
app = Flask(__name__)

#DEFINE A ROUTE AND VIEW FUNCTION
@app.route('/')
def index():
    root_dir = r"D:\\autopy"
    file_tree = get_file_tree(root_dir)
    return render_template('dashboard.html', file_tree=file_tree)

def get_file_tree(root_dir):
    file_tree = {}
    for root, dirs, files in os.walk(root_dir):
        sub_dirs = []
        for directory in dirs:
            sub_dirs.append({
                'name': directory,
                'path': os.path.join(root, directory),
            })
            sub_files = []
            for file in files:
                sub_files.append({
                    'name': file,
                    'path': os.path.join(root, file),
                })
                folder_name = os.path.basename(root)
                file_tree[folder_name] = {
                    'sub_dirs': sub_dirs,
                    'sub_files': sub_files
                }
    return file_tree

if __name__ == '__main__':
    app.run(debug=True)

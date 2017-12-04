import os
import glob

def import_by_string(full_name):
    module_name, unit_name = full_name.rsplit('.', 1)
    return getattr(__import__(module_name, fromlist=['']), unit_name)

cwd = os.path.dirname(__file__)
py_files = glob.glob(cwd + '//[!__init__]*.py')

for py_file_path in py_files:
    py_file_path = os.path.splitext(py_file_path)[0]
    py_file = os.path.basename(py_file_path)
    import_by_string('jumputils.commands.' + py_file + '.main')

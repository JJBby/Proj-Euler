import os
"""
    Currently configured to rename Python files with _ over - and add .py to the end as file extension.

    Also some random path to avoid running on a working directory unintended as well as
    Commented out the rewrite line too.

"""
os.chdir('/home/j/Desktop/ProjectEuler/problems12341234')

for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)
    f_replace = f_name.replace('-', '_')

    f_ext = '.py'
    new_name = f'{f_replace}{f_ext}'

    # os.rename(f, new_name)


with open('../README.md','r') as rex:
    with open('../README_copy.md', 'w') as dash:
        data=rex.read()
        

        new = data.replace('-', '_')

        dash.write(new)
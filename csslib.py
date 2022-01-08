def header():
    return '''@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&family=Poppins:wght@100;200;300;400;500;600;700;800;900&family=Roboto:wght@100;300;400;500;700;900&display=swap');

* {
    padding: 0;
    margin: 0;
    text-decoration: none;
    list-style: none;
}

'''
def param_start():
    return "body {\n"

def defaults(weight,size,color):
    return f"\tfont-weight: {weight};\n\tfont-size: {size};\n\tcolor: {color};\n"

def param_end():
    return "}\n"
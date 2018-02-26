p_template = """
interface {}
ip address {}
"""
int = 'EtherNet101/13/1' 
ip = '10.1.1.1/24' 
print(p_template.format(int, ip))


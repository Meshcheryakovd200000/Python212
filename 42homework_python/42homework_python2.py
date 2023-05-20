from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about2.html')

msg = tm.render()
print(msg)

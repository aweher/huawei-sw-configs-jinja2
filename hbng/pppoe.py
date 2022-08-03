import yaml
import jinja2

yaml_file = 'pppoe.yml'
jinja_template = 'pppoe.j2'

def generate_config(vars):
    with open(jinja_template) as f:
        tfile = f.read()
        template = jinja2.Template(tfile)
        cfg_list = template.render(vars)

        print('-' * 80)
        print(cfg_list)
        print('-' * 80)

with open(yaml_file) as f:
    read_yaml = yaml.safe_load(f)

    for hosts, vars in read_yaml.items():
        generate_config(vars)
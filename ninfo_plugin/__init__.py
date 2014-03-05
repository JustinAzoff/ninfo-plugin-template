from paste.util.template import paste_script_template_renderer
from paste.script.templates import Template, var



vars = [
    var('version', 'Version (like 0.1)', default="0.1"),
    var('description', 'One-line description of the plugin'),
    var('long_description', 'Multi-line description (in reST)'),
    var('keywords', 'Space-separated keywords/tags'),
    var('author', 'Author name'),
    var('author_email', 'Author email'),
    var('url', 'URL of homepage'),
    var('license_name', 'License name'),
]

class NinfoPluginTemplate(Template):
    _template_dir = 'templates'
    summary = 'nInfo Plugin template'
    vars = vars

    def pre(self, command, output_dir, vars):
        vars['plugin'] = vars['package'].replace("ninfo-plugin-", "")
        vars['project_dir'] = vars['project'].replace("-","_")

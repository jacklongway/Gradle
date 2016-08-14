#!/usr/bin/python
import os

vars = {'local.dir': '', 'minSdkVersion': '12', 'targetSdkVersion': '23',
        'compileSdkVersion': '23', 'buildToolsVersion': '23.0.3', 'apps': '', 'javaLib': '',
        'aar': '',
        'nativeLib': '', 'debug': 'true',
        'debug.keystore': '',
        'release.keystore': '',
        'debug.storePassword': '', 'debug.keyAlias': '',
        'debug.keyPassword': '',
        'release.storePassword': '', 'release.keyAlias': '', 'release.keyPassword': ''}
templates = ['project.properties']

currentDir = os.path.dirname(os.path.realpath(__file__))
print currentDir
srcDir = currentDir + "/template/"
desDir = currentDir + "/"


def generate_template(f, regex):
    "generate_template"
    print f, regex
    template_file = open(srcDir + f, 'r')
    out_file = open(desDir + f, 'w')
    for line in template_file:
        print line
        for src, target in regex.iteritems():
            print src, target
            line = line.replace(src, target)
        out_file.write(line)
        print line
    template_file.close()
    out_file.close()


real_vars = {}
for key, value in vars.iteritems():
    print key, value
    real_vars['{' + key + '}'] = value

print real_vars

for template in templates:
    generate_template(template, real_vars)

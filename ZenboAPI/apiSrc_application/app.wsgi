import sys

sys.path.insert(0, "/var/www/ElderMedManagement/ZenboAPI/")

activate_this = '/home/pi/.local/share/virtualenvs/apiSrc_application--FjrzVKE/bin/activate_this.py'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from apiSrc_application.apiSrcApplication import app as application

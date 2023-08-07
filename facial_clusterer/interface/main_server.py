import sys

from app_config_provider import AppConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY="4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh",
    IGNORABLE_404_URLS=[r"^favicon\.ico$"],
    ROOT_URLCONF=sys.modules[__name__],
)


def getHello(request):
    return HttpResponse("<h1>Hello from server!</h1>")


def getFaceClusters(request, faces_dir):
    json_result = app.get_clusters(faces_dir)
    return HttpResponse(json_result)


urlpatterns = [
    path(r"hello", getHello),
    path(r"clusters/<faces_dir>", getFaceClusters, name="some-name"),
]

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    argsProvider = ArgsProvider()

    image_input_dir = app_config["image_input_dir"]
    json_output_dir = app_config["json_output_dir"]

    app = AppLogic(image_input_dir, json_output_dir)

    execute_from_command_line(sys.argv)

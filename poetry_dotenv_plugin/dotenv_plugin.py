import os

from cleo.events.console_events import COMMAND
import dotenv
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

class DotenvPlugin(ApplicationPlugin):
    def activate(self, application):
        application.event_dispatcher.add_listener(COMMAND, self.load_dotenv)

    def load_dotenv(
        self,
        event,
        event_name,
        dispatcher
    ):
        POETRY_DONT_LOAD_ENV = bool(os.environ.get("POETRY_DONT_LOAD_ENV"))
        command = event.command

        if not isinstance(command, EnvCommand) or POETRY_DONT_LOAD_ENV:
            return

        POETRY_DOTENV_LOCATION = os.environ.get("POETRY_DOTENV_LOCATION")
        io = event.io

        if io.is_debug():
            io.write_line("<debug>Loading environment variables.</debug>")

        path = POETRY_DOTENV_LOCATION or dotenv.find_dotenv(usecwd=True)
        POETRY_DOTENV_DONT_OVERRIDE = os.environ.get("POETRY_DOTENV_DONT_OVERRIDE", "")
        DOTENV_OVERRIDE = not POETRY_DOTENV_DONT_OVERRIDE.lower() in (
            "true",
            "1",
        )
        dotenv.load_dotenv(dotenv_path=path, override=DOTENV_OVERRIDE)

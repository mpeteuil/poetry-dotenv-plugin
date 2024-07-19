import os

import dotenv
from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from cleo.events.event_dispatcher import EventDispatcher
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin


class DotenvPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        application.event_dispatcher.add_listener(COMMAND, self.load_dotenv)  # type:ignore

    def load_dotenv(
        self, event: ConsoleCommandEvent, event_name: str, dispatcher: EventDispatcher
    ) -> None:
        POETRY_DONT_LOAD_ENV = bool(os.environ.get("POETRY_DONT_LOAD_ENV"))

        if POETRY_DONT_LOAD_ENV or not isinstance(event.command, EnvCommand):
            return

        POETRY_DOTENV_LOCATION = os.environ.get("POETRY_DOTENV_LOCATION")
        io = event.io

        if io.is_debug():
            io.write_line("<debug>Loading environment variables.</debug>")

        path = POETRY_DOTENV_LOCATION or dotenv.find_dotenv(usecwd=True)
        POETRY_DOTENV_DONT_OVERRIDE = os.environ.get("POETRY_DOTENV_DONT_OVERRIDE", "")
        DOTENV_OVERRIDE = POETRY_DOTENV_DONT_OVERRIDE.lower() not in (
            "true",
            "1",
        )
        dotenv.load_dotenv(dotenv_path=path, override=DOTENV_OVERRIDE)

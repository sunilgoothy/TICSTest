import logging
import webview

from contextlib import redirect_stdout
from io import StringIO
from ToDo import app

logger = logging.getLogger(__name__)


if __name__ == '__main__':

    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('ToDo App', app)
        webview.start(debug=True)
        # webview.start()

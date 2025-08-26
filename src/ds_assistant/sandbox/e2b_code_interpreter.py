import os, sys

from e2b_code_interpreter import Sandbox
from typing import List, Optional, Any

from io import BytesIO
import io

import streamlit as ui
import contextlib


import warnings
from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings(
    "ignore", 
    category=UserWarning, 
    module="pydantic"
)

def e2b_sandbox_code_interpret(e2b_code_interpreter: Sandbox, code: str) -> Optional[List[Any]]:

    try:
        with ui.spinner('Executing code in E2B sandbox...'):
            
            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()

            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")

                    exec = e2b_code_interpreter.run_code(code)

            if stderr_capture.getvalue():
               print("[Code Interpreter Warnings/Errors]", file=sys.stderr)
               print(stderr_capture.getvalue(), file=sys.stderr)

            if stdout_capture.getvalue():
                print("[Code Interpreter Output]", file=sys.stdout)
                print(stdout_capture.getvalue(), file=sys.stdout)

            if exec.error:
                print(f"[Code Interpreter ERROR] {exec.error}", file=sys.stderr)
                return None
            
            return exec.results
        

    except Exception as e:
        print(f"[ERROR in e2b_sandbox_code_interpret]: {e}")
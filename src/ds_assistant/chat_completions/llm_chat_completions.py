import os, sys
from groq import Groq
from e2b_code_interpreter import Sandbox
from src.ds_assistant.sandbox.e2b_code_interpreter import e2b_sandbox_code_interpret
from src.ds_assistant.utils.some_utils import match_code_blocks
from typing import List, Literal, Optional, Any, Tuple
import streamlit as ui



def chat_with_large_language_model(e2b_code_interpreter: Sandbox, user_message: str, dataset_path: str) -> Tuple[Optional[List[Any]], str]:

    try:
        system_prompt = f"""
        You're a Python data scientist and data visualization expert. 
        You are given a dataset at path '{dataset_path}' and also the user's query.
        You need to analyze the dataset and answer the user's query with a response 
        and you run Python code to solve them.
        IMPORTANT: Always use the dataset path variable '{dataset_path}' in your code when reading the CSV file.
        """

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]

        with ui.spinner('Getting response from Together AI LLM model...'):

            client = Groq(
                api_key=ui.session_state.groq_api_key
            )

            completion = client.chat.completions.create(
                model=ui.session_state.model_name,
                messages=messages,
                temperature=0.7,
                max_completion_tokens=1024,
                top_p=1,
                stream=False
            )

            response_message = completion.choices[0].message

            python_code = match_code_blocks(
                llm_response=response_message.content
            )

            if python_code:

                code_interpreter_results = e2b_sandbox_code_interpret(
                    e2b_code_interpreter, 
                    python_code
                )
                return code_interpreter_results, response_message.content
            
            else:
                 ui.warning(f"Failed to match any Python code in model's response")
                 return None, response_message.content


    except Exception as e:
        print(f"[ERROR in chat_with_large_language_model]: {e}")
        raise e
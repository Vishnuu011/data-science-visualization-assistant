from src.ds_assistant.sandbox.e2b_code_interpreter import e2b_sandbox_code_interpret
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv
load_dotenv()

# code = """"
# import matplotlib.pyplot as plt

# # Data for plotting
# x_values = [1, 2, 3, 4, 5]
# y_values = [2, 4, 1, 5, 3]

# # Create the plot
# plt.plot(x_values, y_values)

# # Add labels and title for clarity
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.title('Simple Line Plot Demo')

# # Display the plot
# plt.show()

# """""
# sandbox_var=Sandbox() 
# e2b_sandbox_code_interpret(
#     e2b_code_interpreter=sandbox_var,
#     code=code
# )
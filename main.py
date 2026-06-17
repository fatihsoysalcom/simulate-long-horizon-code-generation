
def simulate_long_horizon_planning(project_description):
    """
    Simulates a long-horizon LLM's planning phase.
    It breaks down a complex project into manageable, interconnected modules.
    """
    print(f"--- Simulating Long-Horizon Planning for: '{project_description}' ---")
    plan = {
        "overall_goal": project_description,
        "modules": [
            {"name": "input_validation", "description": "Validate user input to ensure it's a non-negative integer."},
            {"name": "factorial_calculation", "description": "Calculate the factorial of a given non-negative integer."},
            {"name": "main_interface", "description": "Provide a command-line interface to get input, call calculation, and display results."}
        ],
        "dependencies": {
            "main_interface": ["input_validation", "factorial_calculation"]
        }
    }
    print("Identified Modules and Dependencies:")
    for module in plan["modules"]:
        print(f"- {module['name']}: {module['description']}")
    print(f"Dependencies: {plan['dependencies']}")
    print("\n")
    return plan

def generate_module_code(module_name, module_description):
    """
    Simulates an LLM generating code for a specific module,
    considering its role in the overall project.
    """
    print(f"--- Generating Code for Module: '{module_name}' ---")
    code = ""
    if module_name == "input_validation":
        code = """
def validate_input(user_input_str):
    try:
        num = int(user_input_str)
        if num < 0:
            return None, "Input must be a non-negative integer."
        return num, None
    except ValueError:
        return None, "Invalid input. Please enter an integer."
"""
        # This comment illustrates the LLM's 'understanding' of the module's purpose
        print("Generated validation function to ensure non-negative integer input.")
    elif module_name == "factorial_calculation":
        code = """
def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
"""
        # This comment illustrates the LLM's 'understanding' of the module's purpose
        print("Generated factorial calculation function (iterative approach).")
    elif module_name == "main_interface":
        code = """
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python generated_program.py <number>")
        sys.exit(1)

    input_str = sys.argv[1]
    num, error = validate_input(input_str) # Calls the validation module
    if error:
        print(f"Error: {error}")
        sys.exit(1)

    # Calls the calculation module
    result = calculate_factorial(num)
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
"""
        # This comment illustrates the LLM's 'understanding' of the module's purpose
        print("Generated main interface, integrating validation and calculation modules.")
    else:
        print(f"Warning: No specific code generation logic for module '{module_name}'.")
    print("\n")
    return code

def integrate_generated_code(module_codes, filename="generated_program.py"):
    """
    Simulates an LLM integrating all generated module codes into a single, runnable file.
    It ensures dependencies are correctly ordered and combined.
    """
    print(f"--- Integrating Generated Code into '{filename}' ---")
    final_code_parts = []

    # Ensure validation and calculation are defined before main uses them
    # This simulates the LLM's understanding of code structure and dependencies
    if "input_validation" in module_codes:
        final_code_parts.append(module_codes["input_validation"])
    if "factorial_calculation" in module_codes:
        final_code_parts.append(module_codes["factorial_calculation"])
    if "main_interface" in module_codes:
        final_code_parts.append(module_codes["main_interface"])

    full_code = "\n".join(final_code_parts)

    with open(filename, "w") as f:
        f.write(full_code)

    print(f"Successfully integrated and saved the program to '{filename}'.")
    print("You can now run it: python generated_program.py 5")
    print("\n")
    return full_code

# --- Main simulation execution ---
if __name__ == "__main__":
    project_description = "Create a command-line utility to calculate the factorial of a non-negative integer, including input validation."

    # Step 1: Simulate planning (long-horizon aspect)
    project_plan = simulate_long_horizon_planning(project_description)

    # Step 2: Simulate code generation for each module
    generated_module_codes = {}
    for module in project_plan["modules"]:
        generated_module_codes[module["name"]] = generate_module_code(module["name"], module["description"])

    # Step 3: Simulate integration into a final runnable program
    final_program_code = integrate_generated_code(generated_module_codes)

    print("--- Simulation Complete ---")
    print("The 'generated_program.py' file has been created.")
    print("To run the generated program, execute:")
    print("  python generated_program.py 5")
    print("  python generated_program.py -3")
    print("  python generated_program.py hello")

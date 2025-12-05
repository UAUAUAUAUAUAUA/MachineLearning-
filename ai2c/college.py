# ==============================================================================
# PROJECT: College Major Advisor
# TEAM MEMBERS: [Ben] and [Yaroslav]
#
# BRIEF EXPLANATION:
# Choosing a college major can be overwhelming for students due to the vast 
# number of academic options. This program solves that problem by acting as a 
# preliminary filter. It systematically analyzes a user’s favorite subjects, 
# career goals, and work environments to map them to specific degree 
# recommendations, helping reduce decision paralysis.
# Now obvioulsy its simple and not super complex with like every single possible input/output.
# TEST PLAN:
# 1. Input: math -> solve -> (any)      | Output: Engineering or CS
# 2. Input: science -> help -> (any)    | Output: Nursing or Pre-Med
# 3. Input: arts -> create -> (any)     | Output: Graphic Design or Fine Arts
# 4. Input: humanities -> help -> office| Output: Education or Social Work
# 5. Input: sports -> win -> outside    | Output: General Studies (Catch-all)
# ==============================================================================

def show_tree_diagram():
    """Prints a text-based map of the decision logic."""
    print("\n" * 2)
    print("                      Is Subject Math or Science?                      ")
    print("                                   |                                   ")
    print("                 +-----------------+-----------------+                 ")
    print("                 |                                   |                 ")
    print("                YES                                  NO                ")
    print("                 |                                   |                 ")
    print("      Goal is to Solve Problems?         Is Subject Arts or Humanities?")
    print("       +---------+---------+                 +-------+-------+         ")
    print("       |                   |                 |               |         ")
    print("      YES                  NO               YES              NO        ")
    print("       |                   |                 |               |         ")
    print("Engineering or CS    Goal is to Help?    Goal: Create?   General Studies")
    print("                     +-----+-----+       +---+---+                     ")
    print("                     |           |       |       |                     ")
    print("                    YES          NO     YES      NO                    ")
    print("                     |           |       |       |                     ")
    print("                  Nursing      Data   Graphic   Goal: Help?            ")
    print("                 or Pre-Med   Science  Design    +---+---+             ")
    print("                                                 |       |             ")
    print("                                                YES      NO            ")
    print("                                                 |       |             ")
    print("                                            Env:Office?  Comm/Law      ")
    print("                                            +----+----+                ")
    print("                                            |         |                ")
    print("                                           YES        NO               ")
    print("                                            |         |                ")
    print("                                        Education  Business            ")
    print("\n" * 2)

# --- Program Execution Starts Here ---
print("=" * 60)
print(" Welcome to the College Major Advisor! ")
print("=" * 60)

# Option to see the map
see_map = input("Would you like to see the decision logic map? (y/n): ").lower()
if see_map == "y":
    show_tree_diagram()

print("Please answer the following three questions to get your recommendation.")
print("-" * 60)

# --- Gather Information ---
# .lower() handles capitalization differences
subject = input("1. Favorite subject type? (math/science, arts/humanities): ").lower()
goal = input("2. Primary career goal? (solve problems, create art, help people): ").lower()
environment = input("3. Preferred environment? (office, lab, outdoors, remote): ").lower()

print()
print("Analyzing your answers...")
print("-" * 60)
print("RECOMMENDATION:")
print("-" * 60)

# --- Decision Tree Logic ---
if "math" in subject or "science" in subject:
    # Level 2: STEM Branch
    if "solve" in goal:
        print(">> Engineering or Computer Science")
        print("Reason: You enjoy math/science and like solving problems.")
    elif "help" in goal:
        print(">> Nursing or Pre-Med")
        print("Reason: You enjoy science and want to help people directly.")
    else:
        # Default for STEM
        print(">> Data Science or Analytics")
        print("Reason: You enjoy math/science, and this field analyzes patterns.")

elif "arts" in subject or "humanities" in subject or "writing" in subject or "social" in subject:
    # Level 2: Arts Branch
    if "create" in goal:
        print(">> Graphic Design or Fine Arts")
        print("Reason: You enjoy the arts and want to create.")
    elif "help" in goal:
        # Level 3: Nested check for environment
        if "office" in environment or "remote" in environment:
            print(">> Education or Social Work")
            print("Reason: You want to help people in a structured environment.")
        else:
            print(">> Business or Marketing")
            print("Reason: You enjoy working with people and understanding clients.") 
    else:
        # Default for Humanities
        print(">> Communications or Law")
        print("Reason: You enjoy humanities/writing, which are core skills here.")

else:
    # Catch-all if input didn't match keywords
    print(">> General Studies")
    print("Reason: Your interests are broad! This is a great way to explore.")

# --- Footer ---
print("=" * 60)
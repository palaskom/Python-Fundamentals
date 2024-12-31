# Continue
Moves to the next breakpoint (if exist)

# Step Over
Moves to the next line in the current scope (current area)
Step Over = One step in the current scope
Exception to the rule: If I am in the file-scope and have set a breakpoint  in another scope (e.g., inside a function), it will move from the file scope to the other scope. When it moves to the last line of the function, it will move to the next line of the file (after the function call)

# Step Into/Out
Step into moves into a lower scope (e.g., from file to a function)
Step out moves back to the higher scope (e.g., from function back to file where the function was invoked)

# Debug Console
Use it to check or perform operations on objects

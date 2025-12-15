INPUT_PATH = "Day1/input.txt"

# 1. Read the puzzle input
input_data = []
with open(INPUT_PATH, "r") as file:
    lines = file.readlines()
    for line in lines:
        input_data.append(line.strip())

# 2. Initialize variables
NUM_POSITIONS = 100 # The dial has 100 positions (0-99)
total_zero_clicks = 0
current_position = 50 # The dial starts at 50

# 3. Process each rotation
for rotation in input_data:
    # 3a. Parse the rotation string
    direction = rotation[0]
    distance = int(rotation[1:])
    
    zero_clicks_in_rotation = 0

    if direction == 'R':
        # --- Right Rotation (R) ---
        
        # Count 0-hits: Number of times (current_position + d) crosses a multiple of 100
        # This is equivalent to floor((current_position + distance) / 100)
        zero_clicks_in_rotation = (current_position + distance) // NUM_POSITIONS
        
        # Update position
        current_position = (current_position + distance) % NUM_POSITIONS
        
    elif direction == 'L':
        # --- Left Rotation (L) ---
        
        # Calculate distance to the next 0 counter-clockwise
        if current_position == 0:
            # If at 0, the first click L1 goes to 99, so it takes 100 clicks to hit 0 again.
            dist_to_next_zero = NUM_POSITIONS
        else:
            # If at P, it takes P clicks to hit 0 (P -> 0)
            dist_to_next_zero = current_position
        
        # Count 0-hits: 1 for the first hit, plus 1 for every subsequent 100 clicks
        if distance >= dist_to_next_zero:
            zero_clicks_in_rotation = 1 + (distance - dist_to_next_zero) // NUM_POSITIONS
        # else: zero_clicks_in_rotation remains 0
        
        # Update position
        # Modular arithmetic for negative results: (P - D) % 100
        current_position = (current_position - distance) % NUM_POSITIONS
    # 4. Update the total count
    total_zero_clicks += zero_clicks_in_rotation


print(f"The actual password (total zero clicks) is: {total_zero_clicks}")

# Output: The actual password (total zero clicks) is: 5994
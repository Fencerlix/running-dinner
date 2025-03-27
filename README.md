# Running Dinner Group Combinations

## Description
This project solves the "Running Dinner" problem, where groups of participants meet for different courses (starter, main course, dessert) and must not meet the same group twice. The goal is to count all valid arrangements where each group appears exactly once per stage and hosts one course.

## Problem Statement
- There are $n$ groups for each course: starters $(S_1 ... S_n)$, main courses $(M_1 ... M_n)$, and desserts $(D_1 ... D_n)$.
- Each group must host their respective course and invite two other groups.
- No two groups should meet more than once across all three stages.
- Each group must be present exactly once per stage.

## Solution Approach
- The program recursively generates valid groupings for each stage while ensuring no duplicate encounters.
- The `generate_valid_groups` function ensures that each group is assigned uniquely within a stage.
- The `is_valid` function checks if the newly formed groups meet the constraints.
- A backtracking approach is used to explore all valid possibilities and count them.

## Installation & Usage
### Requirements
- Python 3.x

### Run the script
```
python main.py
```

### Example Output
```
Number of valid combinations: XXXX
```

## File Structure
```
├── main.py  # Main script implementing the algorithm
├── README.md  # Project documentation
```

## Future Improvements
- Optimize performance by reducing redundant calculations.
- Of all possible combinations, find the optimal one (e.g. include a distance matrix and minimize total distances)
- Further optimization by including more constraints (e.g. allergies, availability of bike/car which changes the weighting of given matrix distances)

## License
This project is open-source and available under the MIT License.


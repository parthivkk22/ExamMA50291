###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

###
## To test cluster_maker
## J. Foadi - University of Bath - 2024
###

## Import cluster_maker
import cluster_maker as cm

## Main
if __name__ == '__main__':
    # Create input for define_dataframe_structure
    column_specs = [
        {'name': 'height', 'reps': [180, 160, 120]},
        {'name': 'weight', 'reps': [80, 60, 30]},
        {'name': 'age', 'reps': [40, 35, 10]}
    ]
    
    # Create the dataframe, based on the above info
    df = cm.define_dataframe_structure(column_specs)
    print(df)

    # Simulate 20 data points per group
    data = cm.simulate_data(df, 20)

    # Try this first
    try:
        crr = cm.corre1ation_matrix(data)
    except AttributeError as a:
        pass

    # Conclusion
    print("Is everything really working?")
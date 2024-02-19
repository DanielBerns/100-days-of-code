from models import Society

def main():
    # Example usage
    society = Society(1000, 0.1, None)  
    # Create society with 1000 agents and 10% connection probability
    society.run_simulation(100)  
    # Run simulation for 100 steps
    clusters = society.analyze_clusters()  
    # Group agents into clusters
    total_resources, gini_coefficient = society.get_macro_stats()  
    # Get overall statistics
    
    print("Number of clusters:", len(clusters))
    print("Total resources:", total_resources)
    print("Gini coefficient:", gini_coefficient)

 
if __name__ == "__main__":
    main()

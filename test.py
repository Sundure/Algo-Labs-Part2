from lab4 import PriorityQueue

def run_priority_test():
    pq = PriorityQueue()
    
    tasks_to_add = [
        ("Task A (Priority 5)", 5),
        ("Task B (Priority 15)", 15),
        ("Task C (Priority 2)", 2),
        ("Urgent Task D (Priority 50)", 50),
        ("Task E (Priority 10)", 10),
        ("Task F (Priority 25)", 25),
        ("Another Task G (Priority 25)", 25)
    ]
    
    print("Inserting elements into the queue...")
    print("-" * 40)
    for value, priority in tasks_to_add:
        pq.insert(value, priority)
        print(f"Added: '{value}'")
        
    print("\nExtracting elements by priority:")
    print("-" * 40)
    
    position = 1
    while True:
        popped_value = pq.pop()
        
        if popped_value is None:
            break
            
        print(f"{position}. {popped_value.value}")
        position += 1
        
    print("-" * 40)
    print("Queue is empty!")

if __name__ == "__main__":
    run_priority_test()

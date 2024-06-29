import csv

def get_input(prompt):
    return input(prompt).strip()

def create_csv():
    filename = "events.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'content', 'place', 'start', 'end', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        
        writer.writeheader()
        
        id_counter = 0
        
        while True:
            content = get_input("Enter content (or type 'exit' to finish): ")
            if content.lower() == 'exit':
                break
            place = get_input("Enter place: ")
            start = get_input("Enter start: ")
            end = get_input("Enter end: ")
            description = get_input("Enter description: ")
            
            writer.writerow({
                'id': id_counter,
                'content': content,
                'place': place,
                'start': start,
                'end': end,
                'description': description
            })
            
            id_counter += 1
            
    print(f"CSV file '{filename}' created successfully.")

if __name__ == "__main__":
    create_csv()

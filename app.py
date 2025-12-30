from services.request_service import create_service_request
from services.technician_service import assign_technician
from services.status_service import update_status

def main():
    print("\nSmart Home Services Management System")
    print("1. Create Service Request")
    print("2. Assign Technician")
    print("3. Update Request Status")

    choice = input("Enter choice: ")

    if choice == "1":
        user_id = int(input("Enter User ID: "))
        issue = input("Describe the issue: ")

        category, priority = create_service_request(user_id, issue)

        print("Service request created successfully.")
        print(f"AI Detected Category: {category}")
        print(f"AI Predicted Priority: {priority}")

    elif choice == "2":
        request_id = int(input("Enter Request ID: "))
        tech_id = int(input("Enter Technician ID: "))
        assign_technician(request_id, tech_id)
        print("Technician assigned successfully.")

    elif choice == "3":
        request_id = int(input("Enter Request ID: "))
        status = input("Enter new status (Resolved / In Progress): ")
        update_status(request_id, status)
        print("Status updated successfully.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

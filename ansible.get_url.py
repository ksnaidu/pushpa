import os
import json
import ansible_runner

def download_file_with_ansible(url, destination_path, host="localhost"):
    """
    Downloads a file using the ansible.builtin.get_url module via the Python API.
    """
    # Define the module arguments
    module_args = {
        "url": url,
        "dest": destination_path,
        "mode": "0644",         # Sets file permissions
        "force": True           # Overwrite file if the content changed
    }

    print(f"Running ansible.builtin.get_url on {host}...")

    # Run the module programmatically
    result = ansible_runner.run(
        host_pattern=host,
        module="ansible.builtin.get_url",
        module_args=json.dumps(module_args),
        quiet=True  # Suppresses standard Ansible screen output
    )

    # Process and evaluate execution status
    for event in result.events:
        if event.get("event") == "runner_on_ok":
            res_data = event["event_data"]["res"]
            print("\n--- Download Successful ---")
            print(f"Status: {res_data.get('msg', 'Success')}")
            print(f"Changed: {res_data.get('changed')}")
            print(f"Destination Path: {res_data.get('dest')}")
            return res_data
            
        elif event.get("event") == "runner_on_failed":
            res_data = event["event_data"]["res"]
            print("\n--- Download Failed ---")
            print(f"Error Message: {res_data.get('msg')}")
            return res_data

    print("Execution finished with no explicit success or failure event.")
    return None

# Example Usage
if __name__ == "__main__":
    target_url = "https://google.com"
    save_path = os.path.expanduser("~/google_homepage.html")
    
    download_file_with_ansible(target_url, save_path)

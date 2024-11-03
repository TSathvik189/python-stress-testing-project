import subprocess
import logging
import google.generativeai as genai
from twilio.rest import Client

# Configure logging
logging.basicConfig(filename='ans.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure the Gemini API
genai.configure(api_key="AIzaSyCisxBm-vNHL5tLZwz7smw")

# Twilio account credentials (replace with yours)
account_sid = "AC5b7d165c90b42b"
auth_token = "4a7706"
twilio_number = "whatsapp:+14155238"
recipient_number = "whatsapp:+91939"  # Phone number in E.164 format

def get_gemini_suggestions(test_output):
    """Get suggestions from the Gemini API based on the test output."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Log output: {test_output}")

        # Check for a valid response
        if response and hasattr(response, 'text'):
            return response.text  # Return the generated content
        else:
            print("Error retrieving suggestions.")
            return None
    except Exception as e:
        logging.error(f"Error in Gemini API call: {e}")
        return None

def send_whatsapp_message(message):
    """Send a WhatsApp message using Twilio, splitting if necessary."""
    client = Client(account_sid, auth_token)
    max_length = 1600  # WhatsApp message limit

    # Split message into chunks if necessary
    messages = [message[i:i + max_length] for i in range(0, len(message), max_length)]

    # Log the total number of messages and their lengths
    logging.info(f"Total messages to send: {len(messages)}")
    for idx, msg in enumerate(messages):
        logging.info(f"Message {idx + 1} length: {len(msg)}")

    for idx, msg in enumerate(messages):
        try:
            # Use a different variable for the Twilio response
            twilio_message = client.messages.create(
                body=msg,
                from_=twilio_number,
                to=recipient_number
            )
            logging.info(f"Sent WhatsApp message {idx + 1}/{len(messages)}: {twilio_message.sid}")
        except Exception as e:
            logging.error(f"Failed to send WhatsApp message: {e}")

def memory_stress():
    """Perform a memory stress test."""
    logging.info("Starting memory stress test")
    try:
        result = subprocess.run("stress-ng --vm 1 --vm-bytes 80% -t 30s", shell=True, check=True, capture_output=True, text=True)
        logging.info("Memory stress test completed")
        logging.info(f"Memory stress test output: {result.stdout}")
        print(f"Memory stress test output: {result.stdout}")

        suggestions = get_gemini_suggestions(result.stdout)
        if suggestions:
            logging.info(f"Suggestions from Gemini: {suggestions}")
            print(f"Suggestions from Gemini: {suggestions}")
            send_whatsapp_message(suggestions)
        else:
            logging.warning("Could not retrieve suggestions from Gemini.")
            print("Could not retrieve suggestions from Gemini.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Memory stress test failed: {e}")
        print(f"Memory stress test failed: {e}")

def disk_stress():
    """Perform a disk stress test."""
    logging.info("Starting disk stress test")
    try:
        result = subprocess.run("stress-ng -v --hdd 1 --hdd-method callfunc --verify -t 10s", shell=True, check=True, capture_output=True, text=True)
        logging.info("Disk stress test completed")
        logging.info(f"Disk stress test output: {result.stdout}")

        suggestions = get_gemini_suggestions(result.stdout)
        if suggestions:
            logging.info(f"Suggestions from Gemini: {suggestions}")
            print(f"Suggestions from Gemini: {suggestions}")
            send_whatsapp_message(suggestions)
        else:
            logging.warning("Could not retrieve suggestions from Gemini.")
            print("Could not retrieve suggestions from Gemini.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Disk stress test failed: {e}")
        print(f"Disk stress test failed: {e}")

def network_stress():
    """Perform a network stress test."""
    logging.info("Starting network stress test")
    try:
        result = subprocess.run("iperf3 -s & iperf3 -c 192.168.1 -t 30", shell=True, check=True, capture_output=True, text=True)
        logging.info("Network stress test completed")
        logging.info(f"Network stress test output: {result.stdout}")

        suggestions = get_gemini_suggestions(result.stdout)
        if suggestions:
            logging.info(f"Suggestions from Gemini: {suggestions}")
            print(f"Suggestions from Gemini: {suggestions}")
            send_whatsapp_message(suggestions)
        else:
            logging.warning("Could not retrieve suggestions from Gemini.")
            print("Could not retrieve suggestions from Gemini.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Network stress test failed: {e}")
        print(f"Network stress test failed: {e}")

def cpu_stress():
    """Perform a CPU stress test."""
    logging.info("Starting CPU stress test")
    try:
        result = subprocess.run("stress-ng -v --cpu 1 --cpu-method callfunc --verify -t 10s", shell=True, check=True, capture_output=True, text=True)
        logging.info("CPU stress test completed")
        logging.info(f"CPU stress test output: {result.stdout}")

        suggestions = get_gemini_suggestions(result.stdout)
        if suggestions:
            logging.info(f"Suggestions from Gemini: {suggestions}")
            print(f"Suggestions from Gemini: {suggestions}")
            send_whatsapp_message(suggestions)
        else:
            logging.warning("Could not retrieve suggestions from Gemini.")
            print("Could not retrieve suggestions from Gemini.")
    except subprocess.CalledProcessError as e:
        logging.error(f"CPU stress test failed: {e}")
        print(f"CPU stress test failed: {e}")

def mysql_stress():
    """Perform a MySQL stress test."""
    logging.info("Starting MySQL stress test")
    try:
        result = subprocess.run(
            "sysbench --mysql-host=192.168.1 --mysql-user=root "
            "--mysql-password=Sathv --db-driver=mysql oltp_read_write "
            "--tables=10 --table-size=1000 --threads=4 --time=60 run",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        logging.info("MySQL stress test completed")
        logging.info(f"MySQL stress test output: {result.stdout}")

        suggestions = get_gemini_suggestions(result.stdout)
        if suggestions:
            logging.info(f"Suggestions from Gemini: {suggestions}")
            print(f"Suggestions from Gemini: {suggestions}")
            send_whatsapp_message(suggestions)
        else:
            logging.warning("Could not retrieve suggestions from Gemini.")
            print("Could not retrieve suggestions from Gemini.")
    except subprocess.CalledProcessError as e:
        logging.error(f"MySQL stress test failed: {e}")
        print(f"MySQL stress test failed: {e}")

# Main menu function
def main_menu():
    """Display the main menu for stress tests."""
    while True:
        print("\nStress Testing Menu:")
        print("1. Memory Stress Testing")
        print("2. Disk Stress Testing")
        print("3. Network Stress Testing")
        print("4. CPU Stress Testing")
        print("5. MySQL Stress Testing")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            memory_stress()
        elif choice == '2':
            disk_stress()
        elif choice == '3':
            network_stress()
        elif choice == '4':
            cpu_stress()
        elif choice == '5':
            mysql_stress()
        elif choice == '6':
            logging.info("Exiting stress test script")
            print("Exiting...")
            break
        else:
            logging.warning("Invalid choice selected")
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()

import pyautogui
import time

def is_image_found(image_path, region=None):
    """
    Check if the image is found on the screen within the specified region.
    
    :param image_path: Path to the image file.
    :param region: A tuple of (left, top, width, height) to search within a specific region.
                   If None, search the entire screen.
    :return: True if the image is found, False otherwise.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, region=region, grayscale=True, confidence=0.65)
        return location is not None
    except pyautogui.ImageNotFoundException:
        return False

def main():
    image_path = "thiev.png"  # Replace with the path to your image
    region = None  # Define the search area, e.g., (0, 0, 1920, 1080) or leave as None to search the whole screen
    time.sleep(5)

    while True:
        if not is_image_found(image_path, region):
            time.sleep(60)  # Wait for X seconds
            if not is_image_found(image_path, region):
                print("No image found")
                pyautogui.hotkey('ctrl', 'w')
                break  # Exit the loop after displaying the message
        time.sleep(20)  # Adjust the delay between checks as needed

if __name__ == "__main__":
    main()
